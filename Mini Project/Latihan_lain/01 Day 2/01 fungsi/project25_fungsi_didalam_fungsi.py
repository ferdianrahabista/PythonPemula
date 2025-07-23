# Fungsi didalam Fungsi

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    return luas, keliling

l, k = persegi_panjang(10, 3)
print("Luas Persegi Panjang: ", l)
print("Keliling Persegi Panjang: ", k)

