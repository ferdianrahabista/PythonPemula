import tkinter as tk
from tkinter import messagebox

def hitung_total():
    try:
        harga1 = int(entry_harga1.get())
        harga2 = int(entry_harga2.get())
        if harga1 < 0 or harga2 < 0:
            messagebox.showerror("Error", "Harga tidak boleh negatif")
            return
        total = harga1 + harga2
        label_hasil.config(text=f"Total: Rp{total:,}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid")

# GUI setup
root = tk.Tk()
root.title("Hitung Total Belanja")

tk.Label(root, text="Harga Barang 1:").grid(row=0, column=0)
entry_harga1 = tk.Entry(root)
entry_harga1.grid(row=0, column=1)

tk.Label(root, text="Harga Barang 2:").grid(row=1, column=0)
entry_harga2 = tk.Entry(root)
entry_harga2.grid(row=1, column=1)

tk.Button(root, text="Hitung", command=hitung_total).grid(row=2, columnspan=2, pady=10)

label_hasil = tk.Label(root, text="Total: Rp0")
label_hasil.grid(row=3, columnspan=2)

root.mainloop()
