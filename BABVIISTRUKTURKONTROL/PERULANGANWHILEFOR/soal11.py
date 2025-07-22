import tkinter as tk
from tkinter import messagebox

def hitung_jumlah():
    try:
        n = int(entry.get())
        if n < 1:
            raise ValueError
        total = sum(range(1, n + 1))
        hasil_label.config(text=f"Jumlah dari 1 sampai {n} adalah {total}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan bilangan bulat positif!")

root = tk.Tk()
root.title("Jumlah Bilangan")

tk.Label(root, text="Masukkan angka N:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Hitung", command=hitung_jumlah).pack(pady=5)
hasil_label = tk.Label(root, text="")
hasil_label.pack(pady=5)

root.mainloop()
