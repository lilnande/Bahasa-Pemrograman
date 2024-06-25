def pencarian_linear(buku, target):
    # Iterasi over daftar buku
    for index, buku_saat_ini in enumerate(buku):
        # Cek jika buku saat ini cocok dengan target
        if buku_saat_ini == target:
            return index  # Return indeks jika ditemukan
    return -1  # Return -1 jika tidak ditemukan

def tambah_buku(buku, judul):
    # Tambahkan judul buku baru ke daftar
    buku.append(judul)
    print(f'Buku "{judul}" berhasil ditambahkan.')

def hapus_buku(buku, judul):
    # Cari indeks buku yang akan dihapus
    indeks = pencarian_linear(buku, judul)
    if indeks!= -1:
        # Hapus buku dari daftar
        buku.pop(indeks)
        print(f'Buku "{judul}" berhasil dihapus.')
    else:
        print(f'Buku "{judul}" tidak ditemukan.')

def main():
    # Daftar judul buku
    buku = [
        "Pemrograman C++",
        "Struktur Data",
        "Algoritma",
        "Sistem Basis Data",
        "Sistem Operasi"
    ]

    while True:
        print("\nMenu:")
        print("1. Cari buku")
        print("2. Tambahkan buku baru")
        print("3. Hapus buku")
        print("4. Lihat semua buku")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == '1':
            target = input("Masukkan judul buku yang ingin Anda cari: ")
            indeks = pencarian_linear(buku, target)
            if indeks!= -1:
                print(f"Buku ditemukan pada indeks {indeks}.")
            else:
                print("Buku tidak ditemukan.")
        
        elif pilihan == '2':
            buku_baru = input("Masukkan judul buku baru: ")
            tambah_buku(buku, buku_baru)
        
        elif pilihan == '3':
            judul_hapus = input("Masukkan judul buku yang ingin dihapus: ")
            hapus_buku(buku, judul_hapus)
        
        elif pilihan == '4':
            print("\nDaftar buku:")
            for i, buku_saat_ini in enumerate(buku):
                print(f"{i}. {buku_saat_ini}")
        
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()