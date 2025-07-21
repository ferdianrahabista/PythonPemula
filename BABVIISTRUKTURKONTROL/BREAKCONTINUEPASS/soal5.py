import tkinter as tk
from tkinter import messagebox

angka_valid = []

def proses_input():
    try:
        angka = int(entry.get())
        entry.delete(0, tk.END)

        if angka == 0:
            messagebox.showinfo("Selesai", f"Program berhenti.\nAngka valid: {angka_valid}")
            window.destroy()  # keluar dari aplikasi
        elif angka < 0:
            messagebox.showwarning("Peringatan", "Angka negatif diabaikan!")
            return  # continue
        else:
            angka_valid.append(angka)
            hasil_label.config(text=f"Angka valid: {angka_valid}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang benar!")

# GUI Setup
window = tk.Tk()
window.title("Latihan Break & Continue")
window.geometry("350x250")

judul = tk.Label(window, text="Masukkan Angka (0 untuk keluar)", font=("Arial", 14))
judul.pack(pady=10)

entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

submit_btn = tk.Button(window, text="Kirim", command=proses_input)
submit_btn.pack(pady=10)

hasil_label = tk.Label(window, text="Angka valid: []", font=("Arial", 12))
hasil_label.pack(pady=20)

window.mainloop()
