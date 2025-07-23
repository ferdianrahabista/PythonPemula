def luas_lingkaran(r):
    pi = 3.14159
    return pi * r ** 2

def konversi_suhu(c):
    return (c * 9/5) + 32

def cek_genap(n):
    return n % 2 == 0

print("Luas Lingkaran dengan jari-jari 10:", luas_lingkaran(10))
print("Konversi suhu 25 derajat Celcius ke Fahrenheit:", konversi_suhu(25), "Fahrenheit")
print("Apakah 8 genap?", cek_genap(8))
print("Apakah 9 genap?", cek_genap(9))