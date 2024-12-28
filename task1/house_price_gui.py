import joblib
from tkinter import Tk, Label, Entry, Button, Frame, messagebox, PhotoImage, StringVar
from tkinter import ttk

# Load the model
model = joblib.load("house_price_model.pkl")

# Function to predict price
def predict_price():
    try:
        # Get user inputs
        square_footage = float(entry_square_footage.get())
        num_bedrooms = int(entry_num_bedrooms.get())
        num_bathrooms = int(entry_num_bathrooms.get())
        location = int(entry_location.get())  # Urban: 1, Suburban: 2, Rural: 3
        year_built = int(entry_year_built.get())
        quality = int(entry_quality.get())
        amenities = int(entry_amenities.get())

        # Prepare data for prediction
        user_input = [[square_footage, num_bedrooms, num_bathrooms, location, year_built, quality, amenities]]

        # Predict price
        house_price = model.predict(user_input)
        price_var.set(f"${house_price[0]:,.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Function to toggle themes
def toggle_theme():
    if theme_var.get() == "Light":
        theme_var.set("Dark")  # Update the variable to Dark
        root.configure(bg="#2b2b2b")
        frame_main.configure(bg="#2b2b2b")
        style.configure("TLabel", background="#2b2b2b", foreground="#ffffff")
        style.configure("TEntry", fieldbackground="#3b3b3b", foreground="#ffffff")
        style.configure("TButton", background="#4caf50", foreground="#ffffff")
    else:
        theme_var.set("Light")  # Update the variable to Light
        root.configure(bg="#f0f4f8")
        frame_main.configure(bg="#f0f4f8")
        style.configure("TLabel", background="#f0f4f8", foreground="#333333")
        style.configure("TEntry", fieldbackground="#ffffff", foreground="#000000")
        style.configure("TButton", background="#4caf50", foreground="#000000")


# Create GUI
root = Tk()
root.title("House Price Predictor")

# Set screen dimensions dynamically
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width, window_height = 800, 600
x_pos = (screen_width - window_width) // 2
y_pos = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_pos}+{y_pos}")

root.iconphoto(False, PhotoImage(file="C:/Users/zyper/Downloads/unnamed (1).png"))  # Add your icon file here

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12))
style.map("TButton", background=[("active", "#45a049")])

# Main Frame
frame_main = Frame(root, bg="#f0f4f8")
frame_main.pack(expand=True)  # Center the frame in the window

# Inputs
inputs = [
    ("Square Footage:", Entry(frame_main)),
    ("Number of Bedrooms:", Entry(frame_main)),
    ("Number of Bathrooms:", Entry(frame_main)),
    ("Location (Urban=1, Suburban=2, Rural=3):", Entry(frame_main)),
    ("Year Built:", Entry(frame_main)),
    ("Quality (1-5):", Entry(frame_main)),
    ("Amenities (Score 1-5):", Entry(frame_main)),
]

entry_vars = []
for i, (label_text, entry) in enumerate(inputs):
    ttk.Label(frame_main, text=label_text).grid(row=i, column=0, sticky="e", padx=10, pady=5)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    entry_vars.append(entry)

# Unpack entries into variables for easier access
entry_square_footage, entry_num_bedrooms, entry_num_bathrooms, entry_location, entry_year_built, entry_quality, entry_amenities = entry_vars

# Predict Button
predict_button = ttk.Button(frame_main, text="Predict Price", command=predict_price)
predict_button.grid(row=len(inputs), column=0, columnspan=2, pady=15)

# Result Display
price_var = StringVar(value="")
result_frame = Frame(frame_main, bg="#007acc", pady=10, padx=10)
result_frame.grid(row=len(inputs) + 1, column=0, columnspan=2, pady=20, sticky="ew")
Label(result_frame, textvariable=price_var, font=("Helvetica", 16, "bold"), bg="#007acc", fg="white").pack()

# Theme Toggle
theme_var = StringVar(value="Light")
theme_button = ttk.Button(frame_main, text="Toggle Theme", command=toggle_theme)
theme_button.grid(row=len(inputs) + 2, column=0, columnspan=2, pady=10)

root.mainloop()
