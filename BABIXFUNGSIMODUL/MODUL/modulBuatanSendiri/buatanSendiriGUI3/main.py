import tkinter as tk
import modul_mathku

def hitung():
    x = int(entry1.get())
    y = int(entry2.get())
    hasil.set(f"x^2 = {modul_mathku.kuadrat(x)}, x^y = {modul_mathku.pangkat(x, y)}")

root = tk.Tk()
root.title("Kalkulator Modular")

tk.Label(root, text="Nilai x:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Nilai y:").pack()
entry2 = tk.Entry(root)
entry2.pack()

hasil = tk.StringVar()
tk.Button(root, text="Hitung", command=hitung).pack()
tk.Label(root, textvariable=hasil).pack()

root.mainloop()
