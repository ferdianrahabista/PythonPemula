import tkinter as tk
from tkinter import messagebox

angka_valid = []

def proses_input():
    try:
        angka = int(entry.get())
        entry.delete(0, tk.END)

        if angka == 0:
            simpan_data()  # simpan ke file saat keluar
            tampilkan_ringkasan()
            window.destroy()
        elif angka < 0:
            messagebox.showwarning("Peringatan", "Angka negatif diabaikan!")
            return
        else:
            angka_valid.append(angka)

            # Tentukan ganjil/genap
            if angka % 2 == 0:
                status = f"{angka} adalah GENAP"
            else:
                status = f"{angka} adalah GANJIL"

            status_label.config(text=status)
            hasil_label.config(text=f"Angka valid: {angka_valid}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def tampilkan_ringkasan():
    if angka_valid:
        max_val = max(angka_valid)
        min_val = min(angka_valid)
        messagebox.showinfo("Ringkasan", f"Total: {len(angka_valid)}\nMaks: {max_val}\nMin: {min_val}")
    else:
        messagebox.showinfo("Ringkasan", "Tidak ada angka valid yang dimasukkan.")

def simpan_data():
    with open("data_angka.txt", "w") as file:
        file.write("Data Angka Valid:\n")
        for angka in angka_valid:
            file.write(str(angka) + "\n")
        file.write(f"\nMax: {max(angka_valid) if angka_valid else 'N/A'}")
        file.write(f"\nMin: {min(angka_valid) if angka_valid else 'N/A'}")

# GUI
window = tk.Tk()
window.title("Validasi Angka Ganjil/Genap")
window.geometry("400x300")

judul = tk.Label(window, text="Masukkan Angka (0 untuk keluar)", font=("Arial", 14))
judul.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

submit_btn = tk.Button(window, text="Kirim", command=proses_input)
submit_btn.pack(pady=10)

status_label = tk.Label(window, text="", font=("Arial", 12), fg="blue")
status_label.pack()

hasil_label = tk.Label(window, text="Angka valid: []", font=("Arial", 12))
hasil_label.pack(pady=10)

window.mainloop()
