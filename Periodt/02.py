import tkinter as tk
from tkinter import font, messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta

class PeriodApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PeriodTRI")
        self.geometry("500x650")
        self.configure(bg="#FFC0CB")
        
        # Load Poppins font
        self.poppins_font = font.Font(family="Poppins", size=12)
        self.title_font = font.Font(family="Poppins", size=24, weight="bold")
        self.button_font = font.Font(family="Poppins", size=14, weight="bold")
        
        # Main Page
        self.main_frame = tk.Frame(self, bg="#FFC0CB")
        self.create_main_page()

    def create_main_page(self):
        self.clear_frame()
        
        # Logo and Title
        title = tk.Label(self.main_frame, text="PeriodTRI", font=self.title_font, bg="#FF69B4", fg="white", padx=20, pady=10)
        title.pack(pady=(20, 0))
        
        # Description Text
        description = tk.Label(self.main_frame, text="Track your period estimates with a counter and explore helpful women's health tips!",
                               font=self.poppins_font, bg="#FFC0CB", fg="white", wraplength=400, justify="center")
        description.pack(pady=30)
        
        # Start Button
        start_button = tk.Button(self.main_frame, text="Start Here!", command=self.show_menu_page,
                                 font=self.button_font, bg="white", fg="#FF69B4", relief="flat", 
                                 padx=20, pady=10, borderwidth=0)
        start_button.pack(pady=10)

        self.main_frame.pack(expand=True)

    def show_menu_page(self):
        self.clear_frame()
        
        # Title
        title = tk.Label(self.main_frame, text="Where would you like to start?", font=self.title_font, bg="#FFC0CB", fg="white")
        title.pack(pady=20)

        # Calculator and Tips Buttons
        menu_frame = tk.Frame(self.main_frame, bg="#FFC0CB")
        calculator_button = tk.Button(menu_frame, text="Period Calculator", command=self.show_input_form,
                                      font=self.button_font, bg="#FF69B4", fg="white", relief="flat", width=20, height=2)
        calculator_button.grid(row=0, column=0, padx=10, pady=10)

        tips_button = tk.Button(menu_frame, text="Period Tips", command=self.show_tips_page,
                                font=self.button_font, bg="#FF69B4", fg="white", relief="flat", width=20, height=2)
        tips_button.grid(row=0, column=1, padx=10, pady=10)
        
        menu_frame.pack(pady=20)

        # Exit Button to go back to the main welcome page
        exit_button = tk.Button(self.main_frame, text="Exit to Home", command=self.create_main_page,
                                font=self.button_font, bg="white", fg="#FF69B4", relief="flat",
                                padx=20, pady=10, borderwidth=0)
        exit_button.pack(pady=10)

    def show_input_form(self):
        self.clear_frame()
        
        # Title
        title = tk.Label(self.main_frame, text="Enter your details", font=self.title_font, bg="#FFC0CB", fg="white")
        title.pack(pady=20)

        # Form Entries
        self.name_entry = self.create_entry("Your Name")
        self.height_entry = self.create_entry("Height (cm)")
        self.weight_entry = self.create_entry("Weight (kg)")
        self.start_date_entry = self.create_date_picker("Start Date of Last Period")
        self.end_date_entry = self.create_date_picker("End Date of Last Period")
        self.duration_entry = self.create_entry("Average Menstrual Duration (days)")

        # Calculate Button
        calculate_button = tk.Button(self.main_frame, text="Calculate", command=self.calculate_results,
                                     font=self.button_font, bg="white", fg="#FF69B4", relief="flat",
                                     padx=20, pady=10, borderwidth=0)
        calculate_button.pack(pady=10)

        # Back Button to go back to the menu
        back_button = tk.Button(self.main_frame, text="Back to Menu", command=self.show_menu_page,
                                font=self.button_font, bg="white", fg="#FF69B4", relief="flat",
                                padx=20, pady=10, borderwidth=0)
        back_button.pack(pady=10)

    def create_entry(self, label_text):
        label = tk.Label(self.main_frame, text=label_text, font=self.poppins_font, bg="#FFC0CB", fg="white")
        label.pack(pady=(10, 5))
        entry = tk.Entry(self.main_frame, font=self.poppins_font, width=30)
        entry.pack(pady=5)
        return entry

    def create_date_picker(self, label_text):
        label = tk.Label(self.main_frame, text=label_text, font=self.poppins_font, bg="#FFC0CB", fg="white")
        label.pack(pady=(10, 5))
        date_entry = DateEntry(self.main_frame, font=self.poppins_font, width=28, background='pink', foreground='white', date_pattern='yyyy-mm-dd')
        date_entry.pack(pady=5)
        return date_entry

    def calculate_results(self):
        try:
            name = self.name_entry.get()
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            start_date = datetime.strptime(self.start_date_entry.get(), "%Y-%m-%d")
            end_date = datetime.strptime(self.end_date_entry.get(), "%Y-%m-%d")
            duration = int(self.duration_entry.get())

            # Calculate BMI
            bmi = weight / ((height / 100) ** 2)
            weight_status = "underweight" if bmi < 18.5 else "normal weight" if bmi < 24.9 else "overweight"

            # Estimate days to next period
            cycle_length = (end_date - start_date).days + duration
            next_period_start = start_date + timedelta(days=cycle_length)
            days_until_next_period = (next_period_start - datetime.now()).days

            # Show results
            self.show_result_page(name, round(bmi, 1), weight_status, days_until_next_period)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid data for all fields.")

    def show_result_page(self, name, bmi, weight_status, days):
        self.clear_frame()
        
        # Result Page Texts
        greeting = tk.Label(self.main_frame, text=f"Hi {name}!", font=self.title_font, bg="#FFC0CB", fg="white")
        greeting.pack(pady=10)

        bmi_text = tk.Label(self.main_frame, text=f"Your BMI is {bmi}, which suggests that you are {weight_status}.",
                            font=self.poppins_font, bg="#FFC0CB", fg="white", wraplength=400, justify="center")
        bmi_text.pack(pady=10)

        days_text = tk.Label(self.main_frame, text=f"You're estimated to be {days} days away from your period.",
                             font=self.button_font, bg="#FF69B4", fg="white", padx=20, pady=10, relief="flat", width=30)
        days_text.pack(pady=20)

        # Back Button
        back_button = tk.Button(self.main_frame, text="Back to Home Page", command=self.create_main_page,
                                font=self.button_font, bg="white", fg="#FF69B4", relief="flat",
                                padx=20, pady=10, borderwidth=0)
        back_button.pack(pady=10)

    def show_tips_page(self):
        self.clear_frame()
        
        # Tips Page
        title = tk.Label(self.main_frame, text="Health Tips", font=self.title_font, bg="#FFC0CB", fg="white")
        title.pack(pady=20)

        tips_text = tk.Label(self.main_frame, text="Here are some helpful tips for maintaining a healthy cycle...",
                             font=self.poppins_font, bg="#FFC0CB", fg="white", wraplength=400, justify="center")
        tips_text.pack(pady=20)

        # Back to Menu Button
        back_button = tk.Button(self.main_frame, text="Back to Menu", command=self.show_menu_page,
                                font=self.button_font, bg="white", fg="#FF69B4", relief="flat",
                                padx=20, pady=10, borderwidth=0)
        back_button.pack(pady=10)

    def clear_frame(self):
        """Clear all widgets in the main frame."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = PeriodApp()
    app.run()
