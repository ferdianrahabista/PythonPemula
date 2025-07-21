nama = input("Nama siswa: ")
nilai1 = float(input("Masukkan nilai Matematika: "))
nilai2 = float(input("Masukkan nilai IPA: "))
nilai3 = float(input("Masukkan nilai Bahasa Inggris: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

print(f"\n{nama} memiliki rata-rata nilai: {rata_rata:.2f}")
