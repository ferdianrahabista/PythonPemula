import tkinter as tk

def kuadratkan():
    try:
        angka = int(entry.get())
        kuadrat = lambda x: x**2
        hasil = kuadrat(angka)
        output.config(text=f"Kuadrat: {hasil}")
    except ValueError:
        output.config(text="Masukkan angka!")

root = tk.Tk()
root.title("Lambda - Pangkat Dua")

tk.Label(root, text="Angka:").grid(row=0, column=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)

tk.Button(root, text="Hitung Kuadrat", command=kuadratkan).grid(row=1, columnspan=2)
output = tk.Label(root, text="")
output.grid(row=2, columnspan=2)

root.mainloop()
