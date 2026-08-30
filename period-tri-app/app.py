from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import datetime, timedelta
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import google.oauth2.credentials

app = Flask(__name__)
app.secret_key = 'ffrrd' 
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1" 

SCOPES = ['https://www.googleapis.com/auth/calendar']
CLIENT_SECRETS_FILE = "credentials.json"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/choose_menu')
def choose_menu():
    return render_template('choose_menu.html')

@app.route('/input_form', methods=['GET', 'POST'])
def input_form():
    if request.method == 'POST':
        # Collect data from the form
        name = request.form['name']
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        avg_cycle_duration = int(request.form['duration'])

        # Store data in the session for later use
        session['name'] = name
        session['height'] = height
        session['weight'] = weight
        session['start_date'] = start_date
        session['end_date'] = end_date
        session['duration'] = avg_cycle_duration

        return redirect(url_for('result'))
    return render_template('input_form.html')

@app.route('/result')
def result():
    # Retrieve data from the session
    name = session.get('name')
    height = session.get('height')
    weight = session.get('weight')
    start_date = session.get('start_date')
    end_date = session.get('end_date')
    avg_cycle_duration = session.get('duration')

    if not all([name, height, weight, start_date, end_date, avg_cycle_duration]):
        return redirect(url_for('index'))

    # Convert dates
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # Calculate BMI
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        weight_status = "underweight"
    elif 18.5 <= bmi <= 25:
        weight_status = "normal weight"
    else:
        weight_status = "overweight"

    # Calculate the cycle length
    cycle_length = (end_date - start_date).days + 1

    # Condition
    if 18.5 <= bmi <= 25:
        if avg_cycle_duration < 28:
            next_period_start = end_date + timedelta(days=28)
        elif 28 <= avg_cycle_duration < 35:
            next_period_start = end_date + timedelta(days=28)
        else:
            next_period_start = end_date + timedelta(days=32)
    else:
        if avg_cycle_duration == 28:
            next_period_start = end_date + timedelta(days=35)
        else:
            next_period_start = end_date + timedelta(days=38)


    # Calculate and save calculation
    days_left = (next_period_start - datetime.now()).days
    session['next_period_date'] = next_period_start.strftime('%Y-%m-%d')

    return render_template(
        'result.html',
        name=name,
        bmi=round(bmi, 1),
        weight_status=weight_status,
        days=days_left,
        next_period_date=next_period_start.strftime('%Y-%m-%d')
    )

@app.route('/authorize')
def authorize():
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES)

    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true')

    session['state'] = state
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('oauth2callback', _external=True)

    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)

    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    return redirect(url_for('add_event'))

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

@app.route('/add_event')
def add_event():
    credentials = google.oauth2.credentials.Credentials(
        **session['credentials'])

    service = googleapiclient.discovery.build(
        'calendar', 'v3', credentials=credentials)

    next_period_date = session.get('next_period_date')
    event = {
        'summary': 'Next Period Start',
        'description': 'Predicted start date of the next period.',
        'start': {
            'date': next_period_date,
            'timeZone': 'UTC',
        },
        'end': {
            'date': next_period_date,
            'timeZone': 'UTC',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return render_template('event_confirmation.html', event_link=event.get('htmlLink'))

@app.route('/tips')
def tips():
    return render_template('tips.html')

@app.route('/tips2')
def tips2():
    return render_template('tips2.html')

@app.route('/tips3')
def tips3():
    return render_template('tips3.html')

@app.route('/tips4')
def tips4():
    return render_template('tips4.html')

if __name__ == '__main__':
    app.run(debug=True)
