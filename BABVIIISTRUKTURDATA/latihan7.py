import tkinter as tk

# Operasi Set:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
gabungan = set1 | set2
irisan = set1 & set2
beda = set1 - set2

# GUI
root = tk.Tk()
root.title("Operasi Set")

output = tk.Text(root, height=10, width=40)
output.pack(padx=10, pady=10)

output.insert(tk.END, f"Gabungan: {gabungan}\n")
output.insert(tk.END, f"Irisan: {irisan}\n")
output.insert(tk.END, f"Selisih: {beda}\n")

root.mainloop()
