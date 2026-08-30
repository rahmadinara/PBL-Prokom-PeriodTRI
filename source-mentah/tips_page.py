import customtkinter as ctk

def create_tips_page(app):
    frame = ctk.CTkFrame(app)
    create_navbar(app, frame)
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
