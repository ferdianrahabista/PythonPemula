username = input("Masukkan username: ")

if username == "admin":
    password = input("Masukkan password: ")
    if password == "1234":
        print("Login sukses")
    else:
        print("Password salah")
else:
    print("Akses ditolak")
