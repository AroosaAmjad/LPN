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
            
            # Display the top 5 matched categories
            result_label.config(text="Top 5 matched categories:")
            for i, (index, row) in enumerate(top_5_categories.iterrows(), start=1):
                result_label.config(text=result_label.cget("text") + f"\n{i}. {row['Category Path']}")
        else:
            result_label.config(text="LPN number not found", foreground="red")
    except FileNotFoundError:
        result_label.config(text="Mixed Lot file not found", foreground="red")
    except pd.errors.EmptyDataError:
        result_label.config(text="Mixed Lot file is empty", foreground="red")
    except Exception as e:
        result_label.config(text=f"An error occurred: {str(e)}", foreground="red")

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
