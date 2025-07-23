import math

#Luas Lingkaran
def luas_lingkaran(r):
    return math.pi * r ** 2
print("Luas Lingkaran dengan jari-jari 7 adalah: ", luas_lingkaran(7))

#konversi suhu
def konversi_suhu(c):
    return (c * 9/5) + 32
print("Suhu 25 derajat Celcius dalam Fahrenheit adalah: ", konversi_suhu(25))

# Cek Genap
def cek_genap(n):
    return n % 2 ==0
print("Apakah 10 genap? ", cek_genap(10))
print("Apakah 7 genap? ", cek_genap(7))
