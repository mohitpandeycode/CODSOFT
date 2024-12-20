import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    if length <= 0:
        return "Invalid length. Must be greater than 0."
    return ''.join(random.choice(characters) for _ in range(length))

# Function for Generate Password
def on_generate_Pass():

    try:
        # Get the length entered by the user
        length = int(input_length.get())
        
        if length <= 0:
            result.config(text="Password length must be greater than 0!", fg="red")
        else:
            # Generate password and display
            password = generate_password(length)
            result.config(text=f"Generated Password: {password}", fg="green")
            copy_button.config(state="normal")  # Enable the copy button
    except ValueError:
        result.config(text="Please enter a valid number for the length.", fg="red")

# Function for Copy to Clipboard
def click_copy():

    password = result.cget("text").replace("Generated Password: ", "")
    
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Update clipboard content
        result.config(text="Password copied to clipboard!", fg="blue")


root = tk.Tk()
root.title("Password Genrator")
root.geometry("500x400")

heading = tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), fg="#333", bg="#f7f7f7")
heading.pack(pady=15)


enter_pass = tk.Label(root, text="Enter the password length:", font=("Arial", 14), fg="#555", bg="#f7f7f7")
enter_pass.pack(pady=10)

# input for password length
input_length = tk.Entry(root, font=("Arial", 14), width=15, justify="center")
input_length.pack(pady=10)

# generate password button
generate_Pass = tk.Button(root, text="Generate Password", font=("Arial", 14), bg="#4CAF50", fg="white", command=on_generate_Pass)
generate_Pass.pack(pady=15)

# display the generated password
result = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="#f7f7f7", wraplength=400)
result.pack(pady=10)

# Button to copy password
copy_button = tk.Button(root, text="Copy Password", font=("Arial", 14), bg="#4CAF50", fg="white", command=click_copy, state="disabled")
copy_button.pack(pady=15)


root.mainloop()
