import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from utils import calculate_next_menstruation
from welcome_page import create_welcome_page
from input_page import create_input_page
from tips_page import create_tips_page
from countdown_page import create_countdown_page

class MenstruationTrackerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Menstruation Tracker App")
        self.geometry("500x400")
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")  # Default theme, but we will override with pink elements
        # Frames for each page
        self.frames = {}
        self.create_frames()
        self.show_frame("welcome_page")

    def create_frames(self):
        self.frames["welcome_page"] = create_welcome_page(self)
        self.frames["input_page"] = create_input_page(self)
        self.frames["tips_page"] = create_tips_page(self)
        self.frames["countdown_page"] = create_countdown_page(self)

    def show_frame(self, frame_name):
        # Hide all frames then show the selected frame
        for frame in self.frames.values():
            frame.pack_forget()
        self.frames[frame_name].pack(fill="both", expand=True)

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
