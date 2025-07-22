import tkinter as tk

def cek_ganjil_genap():
    try:
        angka = int(entry.get())
        if angka % 2 == 0:
            hasil = f"{angka} adalah bilangan GENAP"
        else:
            hasil = f"{angka} adalah bilangan GANJIL"
        hasil_label.config(text=hasil)
    except ValueError:
        hasil_label.config(text="Masukkan angka yang valid!")

root = tk.Tk()
root.title("Cek Ganjil atau Genap")

tk.Label(root, text="Masukkan Angka:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Cek", command=cek_ganjil_genap).pack(pady=5)
hasil_label = tk.Label(root, text="")
hasil_label.pack()

root.mainloop()
