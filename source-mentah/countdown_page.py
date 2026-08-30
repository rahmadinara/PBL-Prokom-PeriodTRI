import customtkinter as ctk

def create_countdown_page(app):
    frame = ctk.CTkFrame(app, bg_color="pink")  # Pink background
    create_navbar(app, frame)
    ctk.CTkLabel(frame, text="Countdown Menuju Menstruasi Berikutnya", font=("Comic Sans MS", 14), bg_color="pink").pack(pady=10)
    app.countdown_label = ctk.CTkLabel(frame, text="", font=("Comic Sans MS", 12), bg_color="pink")
    app.countdown_label.pack(pady=10)
    app.update_countdown()
    # Back to welcome page button
    ctk.CTkButton(frame, text="Kembali ke Halaman Awal", font=("Comic Sans MS", 12), command=lambda:
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
