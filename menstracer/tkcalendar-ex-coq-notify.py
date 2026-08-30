from tkcalendar import DateEntry
from plyer import notification
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
import threading
import time


def schedule_notification(notify_date):
    def notify():
        # Continuously check until the specified notification time
        while True:
            now = datetime.datetime.now()
            if now >= notify_date:
                notification.notify(
                    title="Reminder",
                    message="28 days have passed since the selected date! Time: 08:45 AM",
                    timeout=10  # Notification will stay for 10 seconds
                )
                break
            time.sleep(60)  # Check every minute if the time has reached

    # Run the notification checker in a separate thread
    threading.Thread(target=notify, daemon=True).start()


def set_notification():
    # Get the selected date from the DateEntry widget
    selected_date = date_entry.get_date()
    # Calculate the notification date (28 days from selected date)
    notify_date = selected_date + datetime.timedelta(days=28)
    
    # Set the notification time to 08:45 (8:45 AM Indonesian time)
    notify_time = datetime.time(15, 39)
    
    # Combine the notify date and notify time
    notify_datetime = datetime.datetime.combine(notify_date, notify_time)
    
    # Schedule the notification
    schedule_notification(notify_datetime)

    # Show a message that the notification has been set using messagebox
    messagebox.showinfo("Notification Set", f"Notification set for {notify_datetime.strftime('%Y-%m-%d %H:%M')} (08:45 AM)")
    
    # Update the confirmation label as well
    confirmation_label.config(
        text=f"Notification set for {notify_datetime.strftime('%Y-%m-%d %H:%M')} (08:45 AM)"
    )


# Main application window
root = tk.Tk()
root.title("Set Notification in 28 Days")
root.configure(bg='#ffe6f2')  # Light pink background

style = ttk.Style()
style.configure('TButton', background='#ff99cc', foreground='#6a006a', font=('Arial', 12, 'bold'))

# DateEntry widget to pick the date
ttk.Label(root, text="Select a date:", background='#ffe6f2', font=('Arial', 12)).pack(padx=10, pady=5)
date_entry = DateEntry(root, width=12, background='darkblue',
                       foreground='white', borderwidth=2, year=2023)
date_entry.pack(padx=10, pady=10)

# Button to set the notification
ttk.Button(root, text='Set Notification', command=set_notification).pack(padx=10, pady=10)

# Confirmation label to display the scheduled notification date
confirmation_label = ttk.Label(root, text="", background='#ffe6f2', font=('Arial', 12))
confirmation_label.pack(pady=10)

root.mainloop()
