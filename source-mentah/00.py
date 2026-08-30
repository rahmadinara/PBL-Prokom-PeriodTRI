import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime, timedelta

# Function to calculate the next menstruation date
def calculate_next_menstruation(start_date, end_date):
    cycle_length = 28
    next_start_date = end_date + timedelta(days=cycle_length)
    return next_start_date

# Main Application Class
class MenstruationTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menstruation Tracker App")
        self.geometry("500x400")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Frames for each page
        self.frames = {}
        self.create_frames()
        self.show_frame("welcome_page")

    def create_frames(self):
        self.frames["welcome_page"] = self.create_welcome_page()
        self.frames["input_page"] = self.create_input_page()
        self.frames["tips_page"] = self.create_tips_page()
        self.frames["countdown_page"] = self.create_countdown_page()

    def show_frame(self, frame_name):
        # Hide all frames then show the selected frame
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)

    def create_navbar(self, parent):
        # Create navigation bar at the top of each page
        navbar = ctk.CTkFrame(parent)
        navbar.pack(side="top", fill="x")
        ctk.CTkButton(navbar, text="Input Kondisi", command=lambda: self.show_frame("input_page")).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(navbar, text="Tips Hidup Sehat", command=lambda: self.show_frame("tips_page")).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(navbar, text="Countdown", command=lambda: self.show_frame("countdown_page")).pack(side="left", padx=5, pady=5)
        ctk.CTkButton(navbar, text="Keluar", command=self.quit).pack(side="right", padx=5, pady=5)
        return navbar

    def create_welcome_page(self):
        frame = ctk.CTkFrame(self)
        ctk.CTkLabel(frame, text="Selamat Datang di Aplikasi Menstruation Tracker", font=("Arial", 16)).pack(pady=20)
        ctk.CTkButton(frame, text="Mulai", command=lambda: self.show_frame("input_page")).pack(pady=10)
        return frame

    def create_input_page(self):
        frame = ctk.CTkFrame(self)
        self.create_navbar(frame)
        ctk.CTkLabel(frame, text="Masukkan Data Kondisi", font=("Arial", 14)).pack(pady=10)

        # Input fields
        self.entry_start_date = ctk.CTkEntry(frame, placeholder_text="Start Date (YYYY-MM-DD)")
        self.entry_start_date.pack(pady=5)
        self.entry_end_date = ctk.CTkEntry(frame, placeholder_text="End Date (YYYY-MM-DD)")
        self.entry_end_date.pack(pady=5)

        ctk.CTkButton(frame, text="Cek Prediksi", command=self.calculate_prediction).pack(pady=20)
        self.prediction_label = ctk.CTkLabel(frame, text="")
        self.prediction_label.pack(pady=10)

        # Back to welcome page button
        ctk.CTkButton(frame, text="Kembali ke Halaman Awal", command=lambda: self.show_frame("welcome_page")).pack(pady=5)
        return frame

    def create_tips_page(self):
        frame = ctk.CTkFrame(self)
        self.create_navbar(frame)
        ctk.CTkLabel(frame, text="Tips Hidup Sehat", font=("Arial", 14)).pack(pady=10)

        tips = [
            "Minum air yang cukup setiap hari.",
            "Tidur yang cukup dan berkualitas.",
            "Makan makanan bergizi seimbang.",
            "Lakukan olahraga secara teratur."
        ]
        
        for tip in tips:
            ctk.CTkLabel(frame, text=f"• {tip}").pack(anchor="w", padx=20)

        # Back to welcome page button
        ctk.CTkButton(frame, text="Kembali ke Halaman Awal", command=lambda: self.show_frame("welcome_page")).pack(pady=5)
        return frame

    def create_countdown_page(self):
        frame = ctk.CTkFrame(self)
        self.create_navbar(frame)
        ctk.CTkLabel(frame, text="Countdown Menuju Menstruasi Berikutnya", font=("Arial", 14)).pack(pady=10)

        self.countdown_label = ctk.CTkLabel(frame, text="")
        self.countdown_label.pack(pady=10)
        self.update_countdown()

        # Back to welcome page button
        ctk.CTkButton(frame, text="Kembali ke Halaman Awal", command=lambda: self.show_frame("welcome_page")).pack(pady=5)
        return frame

    def calculate_prediction(self):
        # Calculate next menstruation prediction
        try:
            start_date = datetime.strptime(self.entry_start_date.get(), "%Y-%m-%d")
            end_date = datetime.strptime(self.entry_end_date.get(), "%Y-%m-%d")
            next_start_date = calculate_next_menstruation(start_date, end_date)
            self.prediction_label.configure(text=f"Prediksi Tanggal Menstruasi Selanjutnya: {next_start_date.strftime('%Y-%m-%d')}")
            self.predicted_date = next_start_date
            self.update_countdown()
        except ValueError:
            messagebox.showerror("Format Tanggal Salah", "Gunakan format YYYY-MM-DD untuk tanggal.")

    def update_countdown(self):
        # Update countdown label based on the predicted date
        if hasattr(self, "predicted_date"):
            days_remaining = (self.predicted_date - datetime.now()).days
            if days_remaining > 0:
                self.countdown_label.configure(text=f"{days_remaining} hari tersisa menuju menstruasi berikutnya.")
            else:
                self.countdown_label.configure(text="Sudah melewati tanggal prediksi.")
        else:
            self.countdown_label.configure(text="Belum ada prediksi tanggal.")

if __name__ == "__main__":
    app = MenstruationTrackerApp()
    app.mainloop()
