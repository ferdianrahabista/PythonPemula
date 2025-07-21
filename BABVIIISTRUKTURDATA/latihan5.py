import tkinter as tk
from tkinter import messagebox

data_mahasiswa = {}

def simpan_data():
    nama = entry_nama.get()
    nim = entry_nim.get()
    jurusan = entry_jurusan.get()
    
    if nama and nim and jurusan:
        data_mahasiswa[nim] = {"nama": nama, "jurusan": jurusan}
        messagebox.showinfo("Berhasil", f"Data {nama} disimpan.")
        entry_nama.delete(0, tk.END)
        entry_nim.delete(0, tk.END)
        entry_jurusan.delete(0, tk.END)
    else:
        messagebox.showwarning("Gagal", "Semua kolom wajib diisi!")

root = tk.Tk()
root.title("Form Input Mahasiswa")

tk.Label(root, text="Nama").grid(row=0, column=0)
tk.Label(root, text="NIM").grid(row=1, column=0)
tk.Label(root, text="Jurusan").grid(row=2, column=0)

entry_nama = tk.Entry(root)
entry_nim = tk.Entry(root)
entry_jurusan = tk.Entry(root)

entry_nama.grid(row=0, column=1)
entry_nim.grid(row=1, column=1)
entry_jurusan.grid(row=2, column=1)

tk.Button(root, text="Simpan", command=simpan_data).grid(row=3, columnspan=2)

root.mainloop()
