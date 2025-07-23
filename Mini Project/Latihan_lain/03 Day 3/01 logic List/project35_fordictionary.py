siswa = {
    "nama": "Ferdian",
    "nilai": 90,
    "status": "lulus",
}

for key in siswa :
    print(key, ":", siswa[key])

print("==========")
#Bija juga pakai opsi ke 2
for key, value in siswa.items():
    print(f"{key}: {value}")