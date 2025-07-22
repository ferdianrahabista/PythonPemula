import tkinter as tk
from tkinter import messagebox

def submit_data():
    nama = entry_nama.get()
    nim = entry_nim.get()
    prodi = entry_prodi.get()
    
    if not nama or not nim or not prodi:
        messagebox.showerror("Error", "Semua field harus diisi!")
        return
    
    messagebox.showinfo("Data Mahasiswa", f"Nama: {nama}\nNIM: {nim}\nProdi: {prodi}")

# Setup Window
root = tk.Tk()
root.title("Form Mahasiswa")

tk.Label(root, text="Nama").grid(row=0, column=0, sticky="w")
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1)

tk.Label(root, text="NIM").grid(row=1, column=0, sticky="w")
entry_nim = tk.Entry(root)
entry_nim.grid(row=1, column=1)

tk.Label(root, text="Program Studi").grid(row=2, column=0, sticky="w")
entry_prodi = tk.Entry(root)
entry_prodi.grid(row=2, column=1)

tk.Button(root, text="Submit", command=submit_data).grid(row=3, columnspan=2, pady=10)

root.mainloop()
