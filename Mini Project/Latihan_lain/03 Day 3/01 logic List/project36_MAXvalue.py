#Mencari Nilai tertinggi dari List

angka =[65, 70, 85, 88]
maks = angka[0]

for a in angka:
    if a > maks:
        maks = a
        
print("Nilai tertinggi adalah", maks)