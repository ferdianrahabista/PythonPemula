import tkinter as tk
from tkinter import messagebox

def simpan_data():
    data = {
        "Nama": entry_nama.get(),
        "NIM": entry_nim.get(),
        "Prodi": entry_prodi.get(),
        "Semester": entry_semester.get(),
        "Email": entry_email.get(),
        "No. HP": entry_hp.get()
    }
    
    if any(v == "" for v in data.values()):
        messagebox.showwarning("Peringatan", "Semua data wajib diisi.")
    else:
        hasil = "\n".join([f"{k}: {v}" for k, v in data.items()])
        messagebox.showinfo("Data Mahasiswa", hasil)

# GUI Setup
root = tk.Tk()
root.title("Form Lengkap Mahasiswa")

fields = [
    ("Nama", "entry_nama"),
    ("NIM", "entry_nim"),
    ("Program Studi", "entry_prodi"),
    ("Semester", "entry_semester"),
    ("Email", "entry_email"),
    ("No. HP", "entry_hp")
]

entries = {}
for idx, (label_text, var_name) in enumerate(fields):
    tk.Label(root, text=label_text).grid(row=idx, column=0, sticky="w", padx=5, pady=2)
    entries[var_name] = tk.Entry(root, width=30)
    entries[var_name].grid(row=idx, column=1)

entry_nama = entries["entry_nama"]
entry_nim = entries["entry_nim"]
entry_prodi = entries["entry_prodi"]
entry_semester = entries["entry_semester"]
entry_email = entries["entry_email"]
entry_hp = entries["entry_hp"]

tk.Button(root, text="Simpan", command=simpan_data).grid(row=len(fields), columnspan=2, pady=10)

root.mainloop()
