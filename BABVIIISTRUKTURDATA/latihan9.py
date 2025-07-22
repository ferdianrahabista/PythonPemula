import tkinter as tk
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
from collections import Counter

kontak = {}

def simpan_kontak():
    nama = entry_nama.get().strip()
    hp = entry_hp.get().strip()
    if not nama or not hp:
        messagebox.showwarning("Peringatan", "Nama dan HP harus diisi.")
    else:
        kontak[nama] = hp
        messagebox.showinfo("Berhasil", f"Kontak '{nama}' disimpan.")
        entry_nama.delete(0, tk.END)
        entry_hp.delete(0, tk.END)

def tampilkan_kontak():
    output.delete("1.0", tk.END)
    for nama, hp in kontak.items():
        output.insert(tk.END, f"{nama} - {hp}\n")

def ekspor_ke_file():
    if not kontak:
        messagebox.showwarning("Peringatan", "Tidak ada data untuk diekspor.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for nama, hp in kontak.items():
                file.write(f"{nama}:{hp}\n")
        messagebox.showinfo("Berhasil", f"Data berhasil diekspor ke {file_path}")

def tampilkan_grafik():
    if not kontak:
        messagebox.showwarning("Peringatan", "Belum ada data kontak.")
        return
    awalan = [nama[0].upper() for nama in kontak.keys()]
    jumlah = Counter(awalan)
    plt.figure(figsize=(6, 4))
    plt.bar(jumlah.keys(), jumlah.values(), color="skyblue")
    plt.title("Jumlah Kontak Berdasarkan Awalan Nama")
    plt.xlabel("Awalan Huruf")
    plt.ylabel("Jumlah Kontak")
    plt.tight_layout()
    plt.show()

# UI
root = tk.Tk()
root.title("Aplikasi Manajemen Kontak")

tk.Label(root, text="Nama").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(root, text="No. HP").grid(row=1, column=0, padx=5, pady=5, sticky="e")

entry_nama = tk.Entry(root, width=30)
entry_hp = tk.Entry(root, width=30)
entry_nama.grid(row=0, column=1, padx=5, pady=5)
entry_hp.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Simpan", command=simpan_kontak, width=20).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(root, text="Tampilkan Kontak", command=tampilkan_kontak, width=20).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Export ke File", command=ekspor_ke_file, width=20).grid(row=4, column=0, columnspan=2, pady=5)
tk.Button(root, text="Tampilkan Grafik", command=tampilkan_grafik, width=20).grid(row=5, column=0, columnspan=2, pady=5)

output = tk.Text(root, height=10, width=50)
output.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
