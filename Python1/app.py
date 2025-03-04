import string
import tkinter as tk
from tkinter import messagebox
import random

def generate_password(length=12):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_password_button():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for the password length.")
            return
        password = generate_password(length)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")

# Length label and entry
label_length = tk.Label(root, text="Enter the length of the password:")
label_length.pack(pady=10)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

# Generate button
button_generate = tk.Button(root, text="Generate Password", command=generate_password_button)
button_generate.pack(pady=10)

# Password entry
label_password = tk.Label(root, text="Generated Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=5)

# Run the application
root.mainloop()