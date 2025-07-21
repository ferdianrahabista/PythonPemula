kontak = {}

def simpan_kontak(nama, hp):
    kontak[nama] = hp
    with open("kontak.txt", "a") as file:
        file.write(f"{nama}:{hp}\n")

def tampilkan_kontak():
    for nama, hp in kontak.items():
        print(f"{nama} -> {hp}")

# Contoh pemakaian:
simpan_kontak("Budi", "08123456789")
simpan_kontak("Ani", "08987654321")

print("Kontak yang tersimpan:")
tampilkan_kontak()
