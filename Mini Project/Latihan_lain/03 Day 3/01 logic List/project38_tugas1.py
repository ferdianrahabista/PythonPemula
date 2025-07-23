siswa = [
    { "No": "1","Nama": "Budi", "Nilai": 80, },
    { "No": "2", "Nama": "Siti", "Nilai": 90, },
    { "No": "3", "Nama": "Andi", "Nilai": 70, },
    { "No": "4", "Nama": "Dewi", "Nilai": 95, },
    { "No": "5", "Nama": "Rudi", "Nilai": 50, },
]

# Cek kelulusan
for a in siswa:
    if a["Nilai"] >= 75:
        print("Siswa ke-", a['No'], f"{a['Nama']}", "Nilai :", a['Nilai'], "lulus")
    else:
        print(f"{a['Nama']} tidak lulus")

# Hitung rata-rata
print("=======================================")
total = 0
for a in siswa:
    total += a['Nilai']

rata = total / len(siswa)
print("Rata-rata nilai siswa adalah:", rata)
print("=======================================")
#opsi Rata-rata dengan penulisan singkat
total = sum([a['Nilai'] for a in siswa])
print("Rata-rata nilai siswa adalah:", total / len(siswa))