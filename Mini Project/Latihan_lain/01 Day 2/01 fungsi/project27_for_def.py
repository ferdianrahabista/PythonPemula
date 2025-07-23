#gabungan antara Loop for dan fungsi

def cek_genap(n):
    return n % 2 ==0

for i in range(10):
    print("Halo ke-", i)
    print("Cek apakah ",i ," Adalah Ganjil/Genap? ", cek_genap(i))
print("Selesai")