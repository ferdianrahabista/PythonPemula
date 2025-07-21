import tkinter as tk

def cetak_segitiga():
    try:
        n = int(entry.get())
        if n < 1:
            raise ValueError
        hasil = ""
        for i in range(1, n + 1):
            hasil += "*" * i + "\n"
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, hasil)
    except ValueError:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, "Masukkan angka bulat positif!")

root = tk.Tk()
root.title("Segitiga Bintang")

tk.Label(root, text="Masukkan jumlah baris:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Cetak", command=cetak_segitiga).pack(pady=5)
text_area = tk.Text(root, height=10, width=30)
text_area.pack()

root.mainloop()
