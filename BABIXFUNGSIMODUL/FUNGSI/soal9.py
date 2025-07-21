import tkinter as tk

def hitung_luas():
    try:
        sisi = int(entry.get())
        def luas_persegi(s):
            return s * s
        hasil = luas_persegi(sisi)
        output.config(text=f"Luas: {hasil}")
    except ValueError:
        output.config(text="Masukkan angka!")

root = tk.Tk()
root.title("Luas Persegi")

tk.Label(root, text="Masukkan sisi:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Button(root, text="Hitung", command=hitung_luas).grid(row=1, columnspan=2)
output = tk.Label(root, text="")
output.grid(row=2, columnspan=2)

root.mainloop()
