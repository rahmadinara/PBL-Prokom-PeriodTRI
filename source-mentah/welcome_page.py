import customtkinter as ctk

def create_welcome_page(app):
    frame = ctk.CTkFrame(app)
    ctk.CTkLabel(frame, text="Selamat Datang di Aplikasi Menstruation Tracker", font=("Arial", 16)).pack(pady=20)
    ctk.CTkButton(frame, text="Mulai", command=lambda: app.show_frame("input_page")).pack(pady=10)
    return frame
