# encryptor_gui.py
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox


def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generation", "Secret key generated and saved as secret.key")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    try:
        key = load_key()
        f = Fernet(key)
        with open(filename, "rb") as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(filename, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Encryption", f"File '{filename}' encrypted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_file(filename):
    try:
        key = load_key()
        f = Fernet(key)
        with open(filename, "rb") as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
        messagebox.showinfo("Decryption", f"File '{filename}' decrypted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def browse_file_encrypt():
    filename = filedialog.askopenfilename()
    if filename:
        encrypt_file(filename)

def browse_file_decrypt():
    filename = filedialog.askopenfilename()
    if filename:
        decrypt_file(filename)

app = tk.Tk()
app.title("File Encryptor")
label = tk.Label(app, text="Welcome to My Application!" ,font=("Helvetica", 16), fg="darkblue")
label.pack()



generate_key_button = tk.Button(app, text="Generate Key", command=generate_key)
generate_key_button.pack(pady=10)

encrypt_button = tk.Button(app, text="Encrypt File", command=browse_file_encrypt)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(app, text="Decrypt File", command=browse_file_decrypt)
decrypt_button.pack(pady=10)

app.mainloop()
