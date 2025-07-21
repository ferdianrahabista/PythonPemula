total = 0
while True:
    data = input("Masukkan harga barang (atau ketik 'selesai' untuk berhenti): ")
    if data.lower() == "selesai":
        break
    try:
        harga = int(data)
        if harga < 0:
            print("Harga tidak boleh negatif.")
        else:
            total += harga
    except ValueError:
        print("Masukkan angka yang valid.")

print(f"Total belanja: Rp{total:,}")
