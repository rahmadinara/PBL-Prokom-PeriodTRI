import customtkinter as ctk
from datetime import datetime, timedelta
from notifypy import Notify

# Function to calculate the next menstruation date
def calculate_next_menstruation(start_date, end_date):
    cycle_length = 28  # Average cycle length in days
    next_start_date = end_date + timedelta(days=cycle_length)
    return next_start_date

# Function to estimate delay in menstruation
def estimate_delay(weight, height, mental_health):
    delay = 0
    if weight > 75:  # Assuming weight in kg
        delay += 1
    if height < 160:  # Assuming height in cm
        delay += 1
    if mental_health.lower() in ["stress", "anxiety"]:
        delay += 2
    return delay

class MenstruationTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menstruation Tracker")
        self.geometry("400x400")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("pink")

        # Create layout
        self.label_name = ctk.CTkLabel(self, text="Enter your name:")
        self.label_name.pack(pady=10)
        self.entry_name = ctk.CTkEntry(self)
        self.entry_name.pack(pady=10)

        self.label_start_date = ctk.CTkLabel(self, text="Enter last start date (YYYY-MM-DD):")
        self.label_start_date.pack(pady=10)
        self.entry_start_date = ctk.CTkEntry(self)
        self.entry_start_date.pack(pady=10)

        self.label_end_date = ctk.CTkLabel(self, text="Enter last end date (YYYY-MM-DD):")
        self.label_end_date.pack(pady=10)
        self.entry_end_date = ctk.CTkEntry(self)
        self.entry_end_date.pack(pady=10)

        self.label_weight = ctk.CTkLabel(self, text="Enter your weight (kg):")
        self.label_weight.pack(pady=10)
        self.entry_weight = ctk.CTkEntry(self)
        self.entry_weight.pack(pady=10)

        self.label_height = ctk.CTkLabel(self, text="Enter your height (cm):")
        self.label_height.pack(pady=10)
        self.entry_height = ctk.CTkEntry(self)
        self.entry_height.pack(pady=10)

        self.label_mental_health = ctk.CTkLabel(self, text="Enter your mental health condition:")
        self.label_mental_health.pack(pady=10)
        self.entry_mental_health = ctk.CTkEntry(self)
        self.entry_mental_health.pack(pady=10)

        self.button_calculate = ctk.CTkButton(self, text="Calculate Next Menstruation", command=self.calculate)
        self.button_calculate.pack(pady=20)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=10)

    def calculate(self):
        name = self.entry_name.get()
        start_date_str = self.entry_start_date.get()
        end_date_str = self.entry_end_date.get()
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())
        mental_health = self.entry_mental_health.get()

        try:
            # Parse dates
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            # Calculate next menstruation date
            next_start_date = calculate_next_menstruation(start_date, end_date)

            # Estimate delay
            delay = estimate_delay(weight, height, mental_health)

            # Final predicted date
            predicted_date = next_start_date + timedelta(days=delay)

            # Display result in the GUI
            self.result_label.configure(text=f"{name}, your next menstruation is predicted to start on: {predicted_date.strftime('%Y-%m-%d')}")

            # Send desktop notification
            self.send_notification(name, predicted_date)

        except ValueError as e:
            self.result_label
            self.result_label.configure(text="Error in date format. Please use YYYY-MM-DD.")

    def send_notification(self, name, predicted_date):
        # Create notifications for 3 days, 2 days, and 1 day before the predicted date
        notification_dates = [
            predicted_date - timedelta(days=3),
            predicted_date - timedelta(days=2),
            predicted_date - timedelta(days=1)
        ]

        for notify_date in notification_dates:
            # Schedule the notification
            self.schedule_notification(name, notify_date)

    def schedule_notification(self, name, notify_date):
        # Calculate the time until the notification should be sent
        now = datetime.now()
        time_until_notification = notify_date - now

        # Check if the notification date is in the future
        if time_until_notification.total_seconds() > 0:
            # Schedule the notification using a callback after the required time
            self.after(int(time_until_notification.total_seconds() * 1000), lambda: self.show_notification(name, notify_date))

    def show_notification(self, name, notify_date):
        # Create and display the notification
        notification = Notify()
        notification.title = "Menstruation Reminder"
        notification.message = f"Hi {name}, your menstruation is predicted to start tomorrow on {notify_date.strftime('%Y-%m-%d')}."
        notification.send()

if __name__ == "__main__":
    app = MenstruationTrackerApp()
    app.mainloop()