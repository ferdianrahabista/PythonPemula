umur = int(input("Masukkan Umur :"))
if umur < 12:
    print("Anak-anak")
elif umur < 18:
    print("Remaja")
elif umur < 60:
    print("Dewasa")
else:
    print("Lansia")
    
# Program di atas adalah contoh penggunaan percabangan if-elif-else untuk menentukan kategori umur.
# Program ini meminta pengguna untuk memasukkan umur dan kemudian mencetak kategori umur berdasarkan rentang yang telah ditentukan.
# Program ini menggunakan operator perbandingan (<) untuk membandingkan umur yang dimasukkan dengan batasan kategori umur yang telah ditentukan.
# Jika umur kurang dari 12, maka kategori umur adalah "Anak-anak".
# Jika umur kurang dari 18, maka kategori umur adalah "Remaja".
# Jika umur kurang dari 60, maka kategori umur adalah "Dewasa".
# Jika umur lebih dari atau sama dengan 60, maka kategori umur adalah "Lansia".
# Program ini juga menggunakan fungsi input() untuk meminta pengguna memasukkan umur dan mengonversinya menjadi tipe data integer dengan fungsi int().
# Program ini juga menggunakan fungsi print() untuk mencetak kategori umur yang sesuai dengan umur yang dimasukkan oleh pengguna.
# Program ini adalah contoh sederhana dari penggunaan percabangan dalam pemrograman Python.
# Program ini juga dapat dikembangkan lebih lanjut dengan menambahkan kategori umur lainnya atau dengan menambahkan validasi input untuk memastikan bahwa pengguna memasukkan nilai yang valid.
# Program ini juga dapat digunakan sebagai dasar untuk membuat aplikasi yang lebih kompleks yang melibatkan kategori umur, seperti aplikasi pendaftaran atau aplikasi kesehatan.