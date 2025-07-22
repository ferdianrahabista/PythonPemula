import tkinter as tk

# Data contoh
data_mahasiswa = {
    "123": {"nama": "Andi", "jurusan": "Informatika"},
    "124": {"nama": "Budi", "jurusan": "Sistem Informasi"},
}

# Fungsi
def tampilkan_data():
    output.delete("1.0", tk.END)
    for nim, info in data_mahasiswa.items():
        output.insert(tk.END, f"NIM: {nim}, Nama: {info['nama']}, Jurusan: {info['jurusan']}\n")

# GUI
root = tk.Tk()
root.title("Data Mahasiswa")

tk.Button(root, text="Tampilkan Data", command=tampilkan_data).grid(row=4, columnspan=2)
output = tk.Text(root, height=10, width=40)
output.grid(row=5, columnspan=2)

root.mainloop()
