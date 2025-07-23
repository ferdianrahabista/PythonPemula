#gabungan antara Loop While dan fungsi

def cek_genap(n):
    return n % 2 ==0

x = 1
while x <= 10:
    print("Cek apakah",x,"Adalah Ganjil/Genap?", cek_genap(x))
    x += 1

print("Selesai")