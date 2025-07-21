gaji = float(input("Masukkan gaji: "))

while gaji < 0:
    print("Gaji tidak boleh negatif. Coba lagi.")
    gaji = float(input("Masukkan gaji: "))

print(f"Gaji yang dimasukkan: Rp{gaji:,.2f}")
