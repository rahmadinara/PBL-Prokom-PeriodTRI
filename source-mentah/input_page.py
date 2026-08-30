import customtkinter as ctk
from datetime import datetime
from tkinter import messagebox
from utils import calculate_next_menstruation

def create_input_page(app):
    frame = ctk.CTkFrame(app)
    create_navbar(app, frame)
    ctk.CTkLabel(frame, text="Masukkan Data Kondisi", font=("Arial", 14)).pack(pady=10)
    # Input fields
    app.entry_start_date = ctk.CTkEntry(frame, placeholder_text="Start Date (YYYY-MM-DD)")
    app.entry_start_date.pack(pady=5)
    app.entry_end_date = ctk.CTkEntry(frame, placeholder_text="End Date (YYYY-MM-DD)")
    app.entry_end_date.pack(pady=5)
    ctk.CTkButton(frame, text="Cek Prediksi", command=app.calculate_prediction).pack(pady=20)
    app.prediction_label = ctk.CTkLabel(frame, text="")
    app.prediction_label.pack(pady=10)
    # Back to welcome page button
    ctk.CTkButton(frame, text="Kembali ke Halaman Awal", command=lambda: app.show_frame("welcome_page")).pack(pady=5)
    return frame

def create_navbar(app, parent):
    # Create navigation bar at the top of each page
    navbar = ctk.CTkFrame(parent)
    navbar.pack(side="top", fill="x")
    ctk.CTkButton(navbar, text="Input Kondisi", command=lambda: app.show_frame("input_page")).pack(side="left", padx=5, pady=5)
    ctk.CTkButton(navbar, text="Tips Hidup Sehat", command=lambda: app.show_frame("tips_page")).pack(side="left", padx=5, pady=5)
    ctk.CTkButton(navbar, text="Countdown", command=lambda: app.show_frame("countdown_page")).pack(side="left", padx=5, pady=5)
    ctk.CTkButton(navbar, text="Keluar", command=app.quit).pack(side="right", padx=5, pady=5)
    return navbar
