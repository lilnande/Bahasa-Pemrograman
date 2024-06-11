class Mahasiswa:
    def __init__(self, nama, nim, prodi, nilai):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.nilai = nilai

class Barang:
    def __init__(self, nama, kode, jumlah):
        self.nama = nama
        self.kode = kode
        self.jumlah = jumlah

class Transaksi:
    def __init__(self, tipe, jumlah):
        self.tipe = tipe
        self.jumlah = jumlah

def input_data_mahasiswa():
    mahasiswa_list = []
    while True:
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        prodi = input("Masukkan Prodi: ")
        nilai = float(input("Masukkan Nilai: "))
        mahasiswa_list.append(Mahasiswa(nama, nim, prodi, nilai))
        lebih_data = input("Apakah ingin memasukkan data lagi? (y/n): ")
        if lebih_data.lower() != 'y':
            break
    return mahasiswa_list

def tampilkan_data_mahasiswa(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
        return
    for mahasiswa in mahasiswa_list:
        print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Prodi: {mahasiswa.prodi}, Nilai: {mahasiswa.nilai}")

def hitung_rata_rata_mahasiswa(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
        return
    total_nilai = sum(mahasiswa.nilai for mahasiswa in mahasiswa_list)
    rata_rata_nilai = total_nilai / len(mahasiswa_list)
    print(f"Rata-rata Nilai: {rata_rata_nilai}")

def cari_min_maks_mahasiswa(mahasiswa_list):
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
        return
    mahasiswa_max = max(mahasiswa_list, key=lambda mahasiswa: mahasiswa.nilai)
    mahasiswa_min = min(mahasiswa_list, key=lambda mahasiswa: mahasiswa.nilai)
    print(f"Nilai Tertinggi: Nama: {mahasiswa_max.nama}, NIM: {mahasiswa_max.nim}, Prodi: {mahasiswa_max.prodi}, Nilai: {mahasiswa_max.nilai}")
    print(f"Nilai Terendah: Nama: {mahasiswa_min.nama}, NIM: {mahasiswa_min.nim}, Prodi: {mahasiswa_min.prodi}, Nilai: {mahasiswa_min.nilai}")

def input_data_barang():
    barang_list = []
    while True:
        nama = input("Masukkan Nama Barang: ")
        kode = input("Masukkan Kode Barang: ")
        jumlah = int(input("Masukkan Jumlah Barang: "))
        barang_list.append(Barang(nama, kode, jumlah))
        lebih_data = input("Apakah ingin memasukkan data lagi? (y/n): ")
        if lebih_data.lower() != 'y':
            break
    return barang_list

def tampilkan_semua_barang(barang_list):
    if not barang_list:
        print("Tidak ada data barang.")
        return
    for barang in barang_list:
        print(f"Nama Barang: {barang.nama}, Kode Barang: {barang.kode}, Jumlah Barang: {barang.jumlah}")

def cari_barang_berdasarkan_kode(barang_list, kode):
    for barang in barang_list:
        if barang.kode == kode:
            print(f"Nama Barang: {barang.nama}, Kode Barang: {barang.kode}, Jumlah Barang: {barang.jumlah}")
            return
    print("Barang tidak ditemukan.")

def hapus_barang_berdasarkan_kode(barang_list, kode):
    for barang in barang_list:
        if barang.kode == kode:
            barang_list.remove(barang)
            print(f"Barang dengan kode {kode} telah dihapus.")
            return
    print("Barang tidak ditemukan.")

def input_transaksi():
    transaksi_list = []
    while True:
        tipe = input("Masukkan tipe transaksi (pemasukan/pengeluaran): ")
        jumlah = float(input("Masukkan jumlah: "))
        transaksi_list.append(Transaksi(tipe, jumlah))
        lebih_data = input("Apakah ingin memasukkan transaksi lagi? (y/n): ")
        if lebih_data.lower() != 'y':
            break
    return transaksi_list

def tampilkan_semua_transaksi(transaksi_list):
    if not transaksi_list:
        print("Tidak ada transaksi.")
        return
    for transaksi in transaksi_list:
        print(f"Tipe: {transaksi.tipe}, Jumlah: {transaksi.jumlah}")

def hitung_total_pemasukan(transaksi_list):
    total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == "pemasukan")
    print(f"Total Pemasukan: {total_pemasukan}")

def hitung_total_pengeluaran(transaksi_list):
    total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == "pengeluaran")
    print(f"Total Pengeluaran: {total_pengeluaran}")

def hitung_saldo(transaksi_list):
    total_pemasukan = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == "pemasukan")
    total_pengeluaran = sum(transaksi.jumlah for transaksi in transaksi_list if transaksi.tipe == "pengeluaran")
    saldo = total_pemasukan - total_pengeluaran
    print(f"Saldo Akhir: {saldo}")

def main():
    mahasiswa_list = []
    barang_list = []
    transaksi_list = []
    
    while True:
        print("\nMenu Utama:")
        print("1. Tugas Data Mahasiswa")
        print("2. Tugas Data Barang")
        print("3. Tugas Keuangan Pribadi")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")
        
        if pilihan == '1':
            while True:
                print("\nMenu Data Mahasiswa:")
                print("1. Input Data Mahasiswa")
                print("2. Tampilkan Semua Data Mahasiswa")
                print("3. Hitung Rata-rata Nilai Mahasiswa")
                print("4. Cari Mahasiswa dengan Nilai Tertinggi dan Terendah")
                print("5. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu (1/2/3/4/5): ")
                
                if sub_pilihan == '1':
                    mahasiswa_list = input_data_mahasiswa()
                elif sub_pilihan == '2':
                    tampilkan_data_mahasiswa(mahasiswa_list)
                elif sub_pilihan == '3':
                    hitung_rata_rata_mahasiswa(mahasiswa_list)
                elif sub_pilihan == '4':
                    cari_min_maks_mahasiswa(mahasiswa_list)
                elif sub_pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        
        elif pilihan == '2':
            while True:
                print("\nMenu Data Barang:")
                print("1. Input Data Barang")
                print("2. Tampilkan Semua Barang")
                print("3. Cari Barang Berdasarkan Kode")
                print("4. Hapus Barang Berdasarkan Kode")
                print("5. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu (1/2/3/4/5): ")
                
                if sub_pilihan == '1':
                    barang_list = input_data_barang()
                elif sub_pilihan == '2':
                    tampilkan_semua_barang(barang_list)
                elif sub_pilihan == '3':
                    kode = input("Masukkan Kode Barang yang dicari: ")
                    cari_barang_berdasarkan_kode(barang_list, kode)
                elif sub_pilihan == '4':
                    kode = input("Masukkan Kode Barang yang akan dihapus: ")
                    hapus_barang_berdasarkan_kode(barang_list, kode)
                elif sub_pilihan == '5':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        
        elif pilihan == '3':
            while True:
                print("\nMenu Keuangan Pribadi:")
                print("1. Input Transaksi")
                print("2. Tampilkan Semua Transaksi")
                print("3. Hitung dan Tampilkan Total Pemasukan")
                print("4. Hitung dan Tampilkan Total Pengeluaran")
                print("5. Hitung dan Tampilkan Saldo Akhir")
                print("6. Kembali ke Menu Utama")
                sub_pilihan = input("Pilih menu (1/2/3/4/5/6): ")
                
                if sub_pilihan == '1':
                    transaksi_list = input_transaksi()
                elif sub_pilihan == '2':
                    tampilkan_semua_transaksi(transaksi_list)
                elif sub_pilihan == '3':
                    hitung_total_pemasukan(transaksi_list)
                elif sub_pilihan == '4':
                    hitung_total_pengeluaran(transaksi_list)
                elif sub_pilihan == '5':
                    hitung_saldo(transaksi_list)
                elif sub_pilihan == '6':
                    break
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
        
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
