import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv
# Load category data
category_data = pd.read_csv("category1.csv", encoding='latin1')

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Vectorize the category paths
category_vectors = vectorizer.fit_transform(category_data["Category Path"])

# Function to save LPN and category paths
def save_lpn_category(lpn, categories):
    try:
        with open("lpn_category_mapping.csv", "a") as file:
            for category in categories:
                file.write(f"{lpn},{category}\n")
    except Exception as e:
        print(f"Error occurred while saving data: {str(e)}")
def search_lpn():
    lpn_number = str(lpn_entry.get().strip())
    try:
        mixed_lot_data = pd.read_csv("MIXED_LOT.csv")
        lpn_row = mixed_lot_data[mixed_lot_data["LPN"] == lpn_number]
        
        if not lpn_row.empty:
            category = lpn_row.iloc[0]["CATEGORY"]
            subcategory = lpn_row.iloc[0]["SUBCATEGORY"]
            
            # Display LPN category and subcategory
            lpn_details_label.config(text=f"LPN Category: {category}\nLPN Subcategory: {subcategory}")
            
            # Save LPN and category path to CSV
            save_lpn_category(lpn_number, f"{category} {subcategory}")
            
            # Rest of your code for displaying top 5 matched categories...
        else:
            result_label.config(text="LPN number not found", foreground="red")
    except FileNotFoundError:
        result_label.config(text="Mixed Lot file not found", foreground="red")
    except pd.errors.EmptyDataError:
        result_label.config(text="Mixed Lot file is empty", foreground="red")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}", foreground="red")



# def search_lpn():
#     lpn_number = str(lpn_entry.get().strip())
#     try:
#         mixed_lot_data = pd.read_csv("MIXED_LOT.csv")
#         lpn_row = mixed_lot_data[mixed_lot_data["LPN"] == lpn_number]
        
#         if not lpn_row.empty:
#             category = lpn_row.iloc[0]["CATEGORY"]
#             subcategory = lpn_row.iloc[0]["SUBCATEGORY"]
            
#             # Display LPN category and subcategory
#             lpn_details_label.config(text=f"LPN Category: {category}\nLPN Subcategory: {subcategory}")
            
#             # Save LPN and category path to CSV
#             with open("lpn_category.csv", mode="a", newline="") as file:
#                 writer = csv.writer(file)
#                 writer.writerow([lpn_number, f"{category} {subcategory}"])
            
#             # Rest of your code for displaying top 5 matched categories...
#         else:
#             result_label.config(text="LPN number not found", foreground="red")
#     except FileNotFoundError:
#         result_label.config(text="Mixed Lot file not found", foreground="red")
#     except pd.errors.EmptyDataError:
#         result_label.config(text="Mixed Lot file is empty", foreground="red")
#     except Exception as e:
#         result_label.config(text=f"An error occurred: {str(e)}", foreground="red")

# Create the main window
window = tk.Tk()
window.title("LPN Number Search")

# Set window background color
window.config(bg="lightblue")

# Create a frame for better organization and styling
frame = ttk.Frame(window, padding="20")
frame.pack(fill=tk.BOTH, expand=True)

# Create a label for LPN details
lpn_details_label = ttk.Label(frame, text="", font=("Helvetica", 12))
lpn_details_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Create a label for instructions
instruction_label = ttk.Label(frame, text="Enter LPN Number:", font=("Helvetica", 12))
instruction_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Create an entry field for LPN number input
lpn_entry = ttk.Entry(frame, width=20, font=("Helvetica", 12))
lpn_entry.grid(row=2, column=0, padx=10, pady=5)

# Create a submit button
submit_button = ttk.Button(frame, text="Search", command=search_lpn)
submit_button.grid(row=3, column=0, padx=10, pady=10)

# Create a label to display the top 5 matched categories
result_label = ttk.Label(frame, text="", font=("Helvetica", 12), wraplength=600, justify='left', anchor='w')
result_label.grid(row=5, column=0, padx=10, pady=5)

# Run the main event loop
window.mainloop()
