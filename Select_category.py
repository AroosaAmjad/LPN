# import tkinter as tk
# from tkinter import ttk
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Load category data
# category_data = pd.read_csv("category1.csv", encoding='latin1')

# # Create a TF-IDF vectorizer
# vectorizer = TfidfVectorizer()

# # Vectorize the category paths
# category_vectors = vectorizer.fit_transform(category_data["Category Path"])

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
            
#             # Create a string representation of the LPN category and subcategory
#             lpn_category_str = f"{category} {subcategory}"
            
#             # Vectorize the LPN category
#             lpn_vector = vectorizer.transform([lpn_category_str])
            
#             # Calculate similarity scores using cosine similarity
#             similarity_scores = cosine_similarity(category_vectors, lpn_vector)
            
#             # Sort categories based on similarity scores
#             category_data["Similarity"] = similarity_scores
#             top_5_categories = category_data.sort_values(by="Similarity", ascending=False).head(5)
            
#             # Display the top 5 matched categories in the result label
#             result_label.config(text="Top 5 matched categories:\n" + "\n".join(top_5_categories["Category Path"]))
            
#             # Enable the category dropdown menu
#             category_dropdown['values'] = list(top_5_categories["Category Path"])
#             category_dropdown.config(state="readonly")
#         else:
#             result_label.config(text="LPN number not found", foreground="red")
#     except FileNotFoundError:
#         result_label.config(text="Mixed Lot file not found", foreground="red")
#     except pd.errors.EmptyDataError:
#         result_label.config(text="Mixed Lot file is empty", foreground="red")
#     except Exception as e:
#         result_label.config(text=f"An error occurred: {str(e)}", foreground="red")

# def save_category():
#     lpn_number = str(lpn_entry.get().strip())
#     selected_category = category_dropdown.get()
    
#     if selected_category:
#         # Extract category code from selected category path
#         category_code = category_data[category_data['Category Path'] == selected_category]['Category Code'].values[0]
        
#         # Save LPN and category code to CSV file
#         with open('lpn_category_mapping.csv', 'a') as file:
#             file.write(f"{lpn_number},{category_code}\n")
#         result_label.config(text="LPN and category code saved successfully", foreground="green")
#     else:
#         result_label.config(text="Please select a category path first", foreground="red")

# # Create the main window
# window = tk.Tk()
# window.title("LPN Number Search")

# # Set window background color
# window.config(bg="lightblue")

# # Create a frame for better organization and styling
# frame = ttk.Frame(window, padding="20")
# frame.pack(fill=tk.BOTH, expand=True)

# # Create a label for LPN details
# lpn_details_label = ttk.Label(frame, text="", font=("Helvetica", 12))
# lpn_details_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# # Create a label for instructions
# instruction_label = ttk.Label(frame, text="Enter LPN Number:", font=("Helvetica", 12))
# instruction_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# # Create an entry field for LPN number input
# lpn_entry = ttk.Entry(frame, width=20, font=("Helvetica", 12))
# lpn_entry.grid(row=2, column=0, padx=10, pady=5)

# # Create a submit button
# submit_button = ttk.Button(frame, text="Search", command=search_lpn)
# submit_button.grid(row=3, column=0, padx=10, pady=10)

# # Create a label for the top 5 matched categories
# result_label = ttk.Label(frame, text="", font=("Helvetica", 12), wraplength=600, justify='left', anchor='w')
# result_label.grid(row=5, column=0, padx=10, pady=5)

# # Create a dropdown menu for selecting category
# category_dropdown = ttk.Combobox(frame, state="disabled", font=("Helvetica", 12), width=50)
# category_dropdown.grid(row=6, column=0, padx=10, pady=5)

# # Create a button to save LPN and category code
# save_button = ttk.Button(frame, text="Save Category", command=save_category)
# save_button.grid(row=7, column=0, padx=10, pady=10)

# # Run the main event loop
# window.mainloop()

import tkinter as tk
from tkinter import ttk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load category data
category_data = pd.read_csv("category1.csv", encoding='latin1')

# Create a TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Vectorize the category paths
category_vectors = vectorizer.fit_transform(category_data["Category Path"])

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
            
            # Create a string representation of the LPN category and subcategory
            lpn_category_str = f"{category} {subcategory}"
            
            # Vectorize the LPN category
            lpn_vector = vectorizer.transform([lpn_category_str])
            
            # Calculate similarity scores using cosine similarity
            similarity_scores = cosine_similarity(category_vectors, lpn_vector)
            
            # Sort categories based on similarity scores
            category_data["Similarity"] = similarity_scores
            top_5_categories = category_data.sort_values(by="Similarity", ascending=False).head(5)
            
            # Display the top 5 matched categories in the result label
            result_label.config(text="Top 5 matched categories:")
            category_dropdown['values'] = list(top_5_categories["Category Path"])
            category_dropdown.config(state="readonly")
        else:
            result_label.config(text="LPN number not found", foreground="red")
    except FileNotFoundError:
        result_label.config(text="Mixed Lot file not found", foreground="red")
    except pd.errors.EmptyDataError:
        result_label.config(text="Mixed Lot file is empty", foreground="red")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}", foreground="red")

def save_category():
    lpn_number = str(lpn_entry.get().strip())
    selected_category = category_dropdown.get()
    
    if selected_category:
        # Extract category code from selected category path
        category_code = category_data[category_data['Category Path'] == selected_category]['CategoryID'].values[0]
        
        # Save LPN and category code to CSV file
        with open('lpn_category_mapping.csv', 'a') as file:
            file.write(f"{lpn_number},{category_code}\n")
        result_label.config(text="LPN and category code saved successfully", foreground="green")
    else:
        result_label.config(text="Please select a category path first", foreground="red")

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

# Create a dropdown menu for selecting category
category_dropdown = ttk.Combobox(frame, state="disabled", font=("Helvetica", 12), width=50)
category_dropdown.grid(row=6, column=0, padx=10, pady=5)

# Create a button to save LPN and category code
save_button = ttk.Button(frame, text="Save Category", command=save_category)
save_button.grid(row=7, column=0, padx=10, pady=10)

# Run the main event loop
window.mainloop()
