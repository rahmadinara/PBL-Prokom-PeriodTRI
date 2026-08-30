from datetime import timedelta

# Function to calculate the next menstruation date
def calculate_next_menstruation(start_date, end_date):
    cycle_length = 28
    next_start_date = end_date + timedelta(days=cycle_length)
    return next_start_date
