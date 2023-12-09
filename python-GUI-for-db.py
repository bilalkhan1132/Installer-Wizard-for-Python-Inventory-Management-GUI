import tkinter as tk
import sqlite3

def search_component(event=None):
    part_number = entry.get()
    
    conn = sqlite3.connect('components.db')
    cursor = conn.cursor()
    
    # Search for the part number in the database with partial matching
    cursor.execute("SELECT * FROM components_table WHERE `Part No` LIKE ?", (f'%{part_number}%',))
    results = cursor.fetchall()
    
    conn.close()
    
    display_text = ""
    if results:
        for result in results:
            display_text += f"Part Number: {result[1]}\n Quantity: {result[2]}\n"
    else:
        display_text = "Component not found"
    
    display_label.config(text=display_text)

# Create the GUI window
root = tk.Tk()
root.title("Component Search")

# Increase GUI window size and add padding
root.geometry("500x400")
root.configure(bg='#ECECEC')  # Set background color for the whole GUI

# Customize fonts, sizes, and colors
font_bold = ("Arial", 12, "bold")
font_large = ("Arial", 14)

# Create a frame for better organization and styling
frame = tk.Frame(root, bg='#ECECEC')  # Set background color for the frame
frame.pack(expand=True, padx=50, pady=30)  # Add padding around the frame

# Create and place widgets with customized appearance
label = tk.Label(frame, text="Enter Part Number ", font=font_bold, bg='#ECECEC')
label.grid(row=0, column=0, padx=10, pady=10)  # Add padding around the label

entry = tk.Entry(frame, font=font_large, bd=2)  # Add border to the entry field
entry.grid(row=1, column=0, padx=10, pady=10)  # Add padding around the entry field

search_button = tk.Button(frame, text="Search", command=search_component, font=font_bold, bg="#4CAF50", fg="white")
search_button.grid(row=2, column=0, padx=10, pady=10)  # Add padding around the search button

display_label = tk.Label(frame, text="", wraplength=380, font=font_large, bg='#ECECEC')
display_label.grid(row=3, column=0, padx=10, pady=10)  # Add padding around the display label

# Bind the Enter key to trigger the search
root.bind('<Return>', search_component)

root.mainloop()
