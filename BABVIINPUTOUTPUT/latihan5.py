nama = input("Nama karyawan: ")
gaji_pokok = float(input("Gaji pokok: "))
tunjangan = float(input("Tunjangan: "))
potongan = float(input("Potongan: "))

gaji_bersih = gaji_pokok + tunjangan - potongan

print(f"\nGaji bersih {nama} adalah Rp{gaji_bersih:,.2f}")
