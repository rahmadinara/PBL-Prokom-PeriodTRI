import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("PeriodTRI")
root.state("zoomed")  # Make the window fullscreen
root.configure(bg="#FF66C4")  # Pink background

# Font styling with Poppins
title_font = font.Font(family="Poppins", size=36, weight="bold")  # Larger, bolder font for the title
subtitle_font = font.Font(family="Poppins", size=24, weight="bold")  # Larger, bold font for the subtitle
button_font = font.Font(family="Poppins", size=24, weight="bold")  # Larger font for the button

# Load and place the logo image
logo_path = "E:/Semester 1/prokom/Periodt/logo-sementara.png"  # Update with actual logo path
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((70, 70), Image.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Header frame
header_frame = tk.Frame(root, bg="#f9e0f2", height=100)
header_frame.pack(fill="x")

# Logo label
logo_label = tk.Label(header_frame, image=logo_photo, bg="#f9e0f2")
logo_label.image = logo_photo  # Keep reference to prevent garbage collection
logo_label.pack(side="left", padx=(20, 10))

# Title label
title_label = tk.Label(
    header_frame,
    text="PeriodTRI",
    bg="#f9e0f2",
    fg="#FF66C4",
    font=title_font
)
title_label.pack(side="left", padx=(10, 0))

# Content frame
content_frame = tk.Frame(root, bg="#FF66C4")
content_frame.place(relx=0.05, rely=0.4, anchor="w", relwidth=0.9, relheight=0.5)

# Subtitle label with left alignment and larger font
subtitle_label = tk.Label(
    content_frame,
    text="Track your period estimates with a counter and explore helpful women's health tips!",
    bg="#FF66C4",
    fg="white",
    font=subtitle_font,
    wraplength=800,
    justify="left",  # Align text to the left
    anchor="w"       # Align within the label to the left
)
subtitle_label.pack(anchor="w", padx=20, pady=20)

# Create a rounded button using Canvas
def create_rounded_button(parent, text, command):
    text_width = button_font.measure(text)
    button_width = text_width + 40
    
    # Canvas for rounded button
    canvas = tk.Canvas(parent, width=button_width, height=70, bg="#FF66C4", highlightthickness=0)
    canvas.pack(anchor="w", padx=20, pady=20)  # Left alignment with padding
    
    # Rounded rectangle
    canvas.create_oval(10, 10, 50, 60, fill="white", outline="white")
    canvas.create_oval(button_width-50, 10, button_width-10, 60, fill="white", outline="white")
    canvas.create_rectangle(30, 10, button_width-30, 60, fill="white", outline="white")
    
    # Text label on button
    canvas.create_text(button_width/2, 35, text=text, fill="#FF66C4", font=button_font)
    
    # Bind click event to the canvas for button functionality
    canvas.bind("<Button-1>", lambda e: command())

# Add the Start Here button
create_rounded_button(content_frame, "START HERE!", lambda: print("Start button clicked"))

# Run the application
root.mainloop()
