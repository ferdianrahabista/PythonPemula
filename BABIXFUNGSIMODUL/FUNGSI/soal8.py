import tkinter as tk

def tambah():
    try:
        a = int(entry1.get())
        b = int(entry2.get())
        hasil = a + b
        output.config(text=f"Hasil: {hasil}")
    except ValueError:
        output.config(text="Masukkan angka yang valid")

root = tk.Tk()
root.title("Penjumlahan")

tk.Label(root, text="Bilangan 1").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Bilangan 2").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

tk.Button(root, text="Jumlahkan", command=tambah).grid(row=2, columnspan=2)
output = tk.Label(root, text="")
output.grid(row=3, columnspan=2)

root.mainloop()
