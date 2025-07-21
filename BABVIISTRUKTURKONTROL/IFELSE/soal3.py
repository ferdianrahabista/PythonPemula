usia = int(input("Masukkan usia: "))
pelajar = input("Apakah kamu pelajar? (ya/tidak): ")

if usia < 17 or pelajar.lower() == "ya":
    print("Kamu dapat diskon!")
else:
    print("Maaf, tidak ada diskon")
