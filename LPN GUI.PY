import tkinter as tk
from tkinter import ttk
import pandas as pd

def search_lpn():
    lpn_number = str(lpn_entry.get().strip())
    try:
        # Load the Mixed Lot file
        mixed_lot_data = pd.read_csv("MIXED_LOT.csv") 
        
        # Search for the LPN number in the "LPN" column
        lpn_row = mixed_lot_data[mixed_lot_data["LPN"] == lpn_number]
        
        if not lpn_row.empty:
            # LPN number found, retrieve Category and Subcategory values
            category = lpn_row.iloc[0]["CATEGORY"]
            subcategory = lpn_row.iloc[0]["SUBCATEGORY"]
            result_label.config(text=f"Details found\nCategory: {category}\nSubcategory: {subcategory}", foreground="#0000FF")
        else:
            # LPN number not found
            result_label.config(text="LPN number not found", foreground="red")
    except Exception as e:
        result_label.config(text="An error occurred", foreground="red")
        print("An error occurred:", e)

# Create the main window
window = tk.Tk()
window.title("LPN Number Search")

# Calculate the center of the screen
window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))

# Set window size and position
window.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Set window background color
window.config(bg="lightblue")

# Create a frame for better organization and styling
frame = ttk.Frame(window, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Create a label for instructions
instruction_label = ttk.Label(frame, text="Enter LPN Number:", font=("Helvetica", 12))
instruction_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

# Create an entry field for LPN number input
lpn_entry = ttk.Entry(frame, width=20, font=("Helvetica", 12))
lpn_entry.grid(row=1, column=0, padx=10, pady=5)

# Create a submit button
submit_button = ttk.Button(frame, text="Search", command=search_lpn)
submit_button.grid(row=2, column=0, padx=10, pady=10)

# Create a label to display the result
result_label = ttk.Label(frame, text="", font=("Helvetica", 12))
result_label.grid(row=3, column=0, padx=10, pady=5)

# Run the main event loop
window.mainloop()
