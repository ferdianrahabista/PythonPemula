import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading

def scan_port(target_host, port, result_text_widget):
    """
    Fungsi untuk memindai satu port dan menampilkan hasilnya.
    """
    try:
        # Membuat objek socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Timeout 1 detik

        # Mencoba terhubung ke port
        result = s.connect_ex((target_host, port))

        if result == 0:
            # Port terbuka
            service_name = "Tidak diketahui"
            try:
                # Coba dapatkan nama layanan jika port umum
                service_name = socket.getservbyport(port)
            except OSError:
                pass # Biarkan "Tidak diketahui" jika tidak ada layanan terdaftar

            result_text_widget.insert(tk.END, f"Port {port} - Terbuka ({service_name})\n")
            result_text_widget.see(tk.END) # Scroll otomatis ke bawah
        s.close()
    except socket.gaierror:
        # Host tidak ditemukan
        result_text_widget.insert(tk.END, f"Error: Host '{target_host}' tidak dapat diresolusi.\n")
        result_text_widget.see(tk.END)
    except socket.error as e:
        # Error koneksi lainnya (misalnya, jaringan tidak dapat dijangkau)
        result_text_widget.insert(tk.END, f"Error koneksi untuk {target_host}:{port} - {e}\n")
        result_text_widget.see(tk.END)

def start_scan(host_entry, start_port_entry, end_port_entry, result_text_widget, scan_button):
    """
    Fungsi utama untuk memulai proses pemindaian.
    Jalankan dalam thread terpisah agar GUI tidak macet.
    """
    target_host = host_entry.get().strip()
    
    # Validasi input host
    if not target_host:
        messagebox.showerror("Input Error", "Masukkan alamat IP atau nama host target.")
        return

    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Rentang port harus angka.")
        return

    # Validasi rentang port
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port <= end_port):
        messagebox.showerror("Input Error", "Rentang port tidak valid (1-65535).")
        return
    
    # Nonaktifkan tombol scan saat pemindaian berlangsung
    scan_button.config(state=tk.DISABLED)
    result_text_widget.delete(1.0, tk.END) # Bersihkan area hasil sebelumnya
    result_text_widget.insert(tk.END, f"Memulai pemindaian pada {target_host} dari port {start_port} ke {end_port}...\n")
    result_text_widget.see(tk.END)

    # Resolusi host di luar thread scan_port untuk menghindari error threading pada socket.gethostbyname
    try:
        target_ip = socket.gethostbyname(target_host)
        result_text_widget.insert(tk.END, f"Target IP: {target_ip}\n\n")
        result_text_widget.see(tk.END)
    except socket.gaierror:
        result_text_widget.insert(tk.END, f"Error: Host '{target_host}' tidak dapat diresolusi.\n")
        result_text_widget.see(tk.END)
        scan_button.config(state=tk.NORMAL) # Aktifkan kembali tombol
        return
        
    def threaded_scan():
        """Fungsi yang akan dijalankan di thread terpisah."""
        total_ports = end_port - start_port + 1
        scanned_count = 0
        open_ports_count = 0

        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=scan_port, args=(target_ip, port, result_text_widget))
            thread.start()
            # Opsional: batas jumlah thread aktif untuk mencegah kelebihan beban
            # if threading.active_count() > 100: # Contoh batas 100 thread
            #     thread.join() # Tunggu sampai beberapa thread selesai
            
            # Update progress atau status jika diinginkan
            # Misalnya, tambahkan label progres di GUI

        # Tunggu semua thread selesai (penting untuk mengetahui kapan scan selesai)
        # Ini bisa memakan waktu jika jumlah port banyak dan timeout tinggi
        for thread in threading.enumerate():
            if thread != threading.current_thread() and thread.name.startswith("Thread-"):
                thread.join()
        
        result_text_widget.insert(tk.END, "\nPemindaian selesai.\n")
        result_text_widget.see(tk.END)
        scan_button.config(state=tk.NORMAL) # Aktifkan kembali tombol setelah selesai

    # Jalankan pemindaian di thread terpisah
    scan_thread = threading.Thread(target=threaded_scan)
    scan_thread.start()


def create_gui():
    """
    Fungsi untuk membuat dan menjalankan GUI utama.
    """
    root = tk.Tk()
    root.title("Python Port Scanner")
    root.geometry("600x500") # Ukuran jendela

    # Frame untuk input
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.pack(pady=5)

    tk.Label(input_frame, text="Target Host (IP/Domain):").grid(row=0, column=0, sticky=tk.W, pady=2)
    host_entry = tk.Entry(input_frame, width=40)
    host_entry.grid(row=0, column=1, pady=2)
    host_entry.insert(0, "localhost") # Nilai default

    tk.Label(input_frame, text="Port Mulai:").grid(row=1, column=0, sticky=tk.W, pady=2)
    start_port_entry = tk.Entry(input_frame, width=10)
    start_port_entry.grid(row=1, column=1, sticky=tk.W, pady=2)
    start_port_entry.insert(0, "1") # Nilai default

    tk.Label(input_frame, text="Port Akhir:").grid(row=2, column=0, sticky=tk.W, pady=2)
    end_port_entry = tk.Entry(input_frame, width=10)
    end_port_entry.grid(row=2, column=1, sticky=tk.W, pady=2)
    end_port_entry.insert(0, "1024") # Nilai default

    scan_button = tk.Button(input_frame, text="Mulai Pindai", 
                            command=lambda: start_scan(host_entry, start_port_entry, end_port_entry, result_text, scan_button))
    scan_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Frame untuk hasil
    result_frame = tk.Frame(root, padx=10, pady=5)
    result_frame.pack(expand=True, fill=tk.BOTH)

    tk.Label(result_frame, text="Hasil Pemindaian:").pack(anchor=tk.W)
    result_text = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD, width=70, height=15)
    result_text.pack(expand=True, fill=tk.BOTH)

    root.mainloop()

if __name__ == "__main__":
    create_gui()