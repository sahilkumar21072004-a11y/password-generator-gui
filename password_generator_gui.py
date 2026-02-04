import tkinter as tk
import random
import string
from tkinter import messagebox

# -------- Password Generator Logic --------
def generate_password():
    try:
        length = int(length_entry.get())
        complexity = complexity_var.get()

        letters = string.ascii_letters
        numbers = string.digits
        symbols = string.punctuation

        if complexity == "Letters Only":
            characters = letters
        elif complexity == "Letters + Numbers":
            characters = letters + numbers
        elif complexity == "Letters + Numbers + Symbols":
            characters = letters + numbers + symbols
        else:
            messagebox.showerror("Error", "Select complexity level")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a number")

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def clear_all():
    length_entry.delete(0, tk.END)
    result_entry.delete(0, tk.END)

# -------- GUI Window --------
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# -------- Title --------
tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
).pack(pady=15)

# -------- Length Input --------
tk.Label(root, text="Password Length", bg="#1e1e1e", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# -------- Complexity --------
tk.Label(root, text="Complexity Level", bg="#1e1e1e", fg="white").pack(pady=5)

complexity_var = tk.StringVar()
complexity_var.set("Letters Only")

tk.OptionMenu(
    root,
    complexity_var,
    "Letters Only",
    "Letters + Numbers",
    "Letters + Numbers + Symbols"
).pack()

# -------- Generate Button --------
tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12),
    bg="#4caf50",
    fg="white",
    command=generate_password
).pack(pady=15)

# -------- Result --------
result_entry = tk.Entry(root, font=("Arial", 14), justify="center", width=30)
result_entry.pack(pady=5)

# -------- Action Buttons --------
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Copy", width=10, command=copy_password).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear", width=10, command=clear_all).grid(row=0, column=1, padx=5)

# -------- Run App --------
root.mainloop()
