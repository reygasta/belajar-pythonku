#kerjaan reygasta
'''perintah = ""
sudah = False
while True:
    perintah = input("> ")
    if perintah == "mulai":
        if sudah:
            print("mobil sudah berjalan")
        else:
            sudah = True
            print("mobil berjalan")
    elif perintah == "berhenti":
        if not sudah:
            print("mobil sudah berhenti")
        else:
            sudah = False
            print("mobil berhenti")
    elif perintah == "help":
        print("""
mulai - untuk menyalakan mobil
berhenti - untuk menonaktifkan mobil
quit - untuk keluar mobil
        """)
    elif perintah == "keluar":
        break
    else:
        print("maap ndak tau maksut anda")'''

### program alternatif chatgpt
'''
def kontrol_mobil():
    perintah = ""
    while perintah != "keluar":
        perintah = input("> ")
        if perintah == "mulai":
            print("Memulai mobil...")
        elif perintah == "berhenti":
            print("Mobil berhenti")
        elif perintah == "help":
            tampilkan_bantuan()
        else:
            print("Maaf, saya tidak mengerti maksud Anda")

def tampilkan_bantuan():
    print("""
          mulai - untuk menyalakan mobil
          berhenti - untuk menonaktifkan mobil
          keluar - untuk keluar dari program
          """)

kontrol_mobil()
'''

#gpt4
# Inisialisasi variabel 'mobil_menjalankan' sebagai False (artinya mobil belum berjalan).
mobil_menjalankan = False

# Memulai perulangan utama dengan menggunakan 'while True:' yang berarti selalu berjalan.
while True:
    # Meminta pengguna untuk memasukkan perintah.
    perintah = input("> ")

    # Memeriksa jika perintah adalah "mulai".
    if perintah == "mulai":
        # Jika mobil sudah berjalan sebelumnya, cetak pesan mobil sudah berjalan.
        # Jika tidak, ubah status mobil menjadi berjalan (True) dan cetak pesan mobil berjalan.
        if mobil_menjalankan:
            print("Mobil sudah berjalan")
        else:
            mobil_menjalankan = True
            print("Mobil sedang berjalan")

    # Memeriksa jika perintah adalah "berhenti".
    elif perintah == "berhenti":
        # Jika mobil belum berjalan sebelumnya, cetak pesan mobil sudah berhenti.
        # Jika tidak, ubah status mobil menjadi berhenti (False) dan cetak pesan mobil berhenti.
        if not mobil_menjalankan:
            print("Mobil sudah berhenti")
        else:
            mobil_menjalankan = False
            print("Mobil telah dihentikan")

    # Memeriksa jika perintah adalah "help".
    elif perintah == "help":
        # Menampilkan pesan bantuan yang menjelaskan perintah yang tersedia.
        print("""
mulai - untuk menyalakan mobil
berhenti - untuk menonaktifkan mobil
keluar - untuk keluar dari program
        """)

    # Memeriksa jika perintah adalah "keluar".
    elif perintah == "keluar":
        # Menghentikan perulangan utama dan keluar dari program.
        break

    # Jika perintah tidak cocok dengan opsi di atas, cetak pesan bahwa perintah tidak dimengerti.
    else:
        print("Maaf, saya tidak mengerti maksud Anda")
