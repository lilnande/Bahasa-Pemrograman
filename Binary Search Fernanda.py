def pencarian_biner_indeks(buku, target_indeks):
    kiri, kanan = 0, len(buku) - 1
    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        if tengah == target_indeks:
            return tengah
        elif tengah < target_indeks:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    return -1

def tambah_buku(buku, judul):
    buku.append(judul)
    print(f'Buku "{judul}" berhasil ditambahkan.')

def hapus_buku(buku, indeks):
    if 0 <= indeks < len(buku):
        judul = buku.pop(indeks)
        print(f'Buku "{judul}" berhasil dihapus.')
    else:
        print(f'Buku dengan indeks {indeks} tidak ditemukan.')

def main():
    buku = [
        "Algoritma",
        "Pemrograman C++",
        "Sistem Basis Data",
        "Sistem Operasi",
        "Struktur Data"
    ]

    while True:
        print("\nMenu:")
        print("1. Cari buku berdasarkan nomor indeks")
        print("2. Tambah buku baru")
        print("3. Hapus buku berdasarkan nomor indeks")
        print("4. Lihat semua buku")
        print("5. Keluar")
        
        pilihan = input("Masukkan pilihan Anda (1-5): ")

        if pilihan == '1':
            try:
                target_indeks = int(input("Masukkan nomor indeks buku yang ingin Anda cari: "))
                indeks = pencarian_biner_indeks(buku, target_indeks)
                if indeks != -1:
                    print(f"Buku ditemukan: {buku[indeks]} di indeks {indeks}.")
                else:
                    print("Buku tidak ditemukan.")
            except ValueError:
                print("Masukkan nomor indeks yang valid.")
        
        elif pilihan == '2':
            buku_baru = input("Masukkan judul buku baru: ")
            tambah_buku(buku, buku_baru)
        
        elif pilihan == '3':
            try:
                hapus_indeks = int(input("Masukkan nomor indeks buku yang ingin dihapus: "))
                hapus_buku(buku, hapus_indeks)
            except ValueError:
                print("Masukkan nomor indeks yang valid.")
        
        elif pilihan == '4':
            print("\nDaftar buku:")
            for i, judul in enumerate(buku):
                print(f"{i}. {judul}")
        
        elif pilihan == '5':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
