# Daftar buku (data buku)
buku_list = []

def add_buku():
    # Fungsi untuk menambahkan buku ke dalam daftar
    title = input("Masukkan judul buku: ")
    year = input("Masukkan tahun pembuatan: ")
    publisher = input("Masukkan nama penerbit: ")

    buku = {"title": title, "year": year, "publisher": publisher}
    buku_list.append(buku)
    print(f"{title} berhasil ditambahkan ke daftar!")

def search_buku_by_title(keyword):
    # Fungsi untuk mencari buku berdasarkan judul
    results = []
    for buku in buku_list:
        if keyword.lower() in buku['title'].lower():
            results.append(buku)
    return results

def search_buku_by_year(year):
    # Fungsi untuk mencari buku berdasarkan tahun pembuatan
    results = []
    for buku in buku_list:
        if buku['year'] == year:
            results.append(buku)
    return results

def search_buku_by_publisher(publisher):
    # Fungsi untuk mencari buku berdasarkan nama penerbit
    results = []
    for buku in buku_list:
        if publisher.lower() in buku['publisher'].lower():
            results.append(buku)
    return results

def display_buku(buku_list):
    # Fungsi untuk menampilkan daftar buku
    if not buku_list:
        print("Tidak ada buku yang ditemukan.")
    else:
        print("Buku yang ditemukan:")
        for buku in buku_list:
            print(f"Judul: {buku['title']}, Tahun: {buku['year']}, Penerbit: {buku['publisher']}")

def delete_all_buku():
    # Fungsi untuk menghapus semua data buku
    global buku_list
    confirmation = input("Ketik 'KONFIRMASI' untuk menghapus semua data buku: ")
    if confirmation == "KONFIRMASI":
        buku_list = []
        print("Semua data buku telah dihapus.")
    else:
        print("Penghapusan semua data buku dibatalkan.")

def main():
    while True:
        print("\nMenu Daftar Buku:")
        print("1. Tambah Buku")
        print("2. Cari Buku Berdasarkan Judul")
        print("3. Cari Buku Berdasarkan Tahun")
        print("4. Cari Buku Berdasarkan Penerbit")
        print("5. Hapus Semua Data Buku")
        print("6. Keluar")
        choice = input("Pilih menu (1/2/3/4/5/6): ")

        if choice == '1':
            add_buku()
        elif choice == '2':
            keyword = input("Masukkan kata kunci judul buku yang ingin dicari: ")
            results = search_buku_by_title(keyword)
            display_buku(results)
        elif choice == '3':
            year = input("Masukkan tahun pembuatan buku yang ingin dicari: ")
            results = search_buku_by_year(year)
            display_buku(results)
        elif choice == '4':
            publisher = input("Masukkan nama penerbit yang ingin dicari: ")
            results = search_buku_by_publisher(publisher)
            display_buku(results)
        elif choice == '5':
            delete_all_buku()
        elif choice == '6':
            print("Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
