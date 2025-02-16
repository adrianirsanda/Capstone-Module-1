# Capstone Project
# PredaTank Fish Store

import os
import platform

def clear_terminal():

    system = platform.system().lower()

    if system == 'windows':
        os.system('cls')

    else:
        os.system('clear')

clear_terminal() # untuk windows

from tabulate import tabulate

# password admin : PDT0101

ikan = {
    'Nama' : ['Oscar', 'Peacock Bass', 'Arwana Jardini', 'Payara', 'Vittatus', 'Goliath', 'Golden Dorado'], 
    'Ukuran' : [10, 15, 20, 10, 20, 7, 15], 
    'Origin' : ['Amerika Selatan', 'Amerika Selatan', 'Papua', 'Amerika Selatan', 'Afrika', 'Afrika', 'Amerika Selatan'], 
    'Stok' : [15, 6, 1, 2, 3, 10, 5], 
    'Harga' : [30000, 80000, 250000, 200000, 200000, 185000, 300000]
    }

def readIkan ():
    while True:
        print('=== Menu Tampilkan Data Ikan ===') # tampilan menu 1
        print()
        print('1. Tampilkan Semua Ikan')
        print('2. Tampilkan Ikan Berdasarkan Nama')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi1 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan (1-3): ')) # memilih submenu pada menu 1
        except ValueError:
            print()
            print('Pilihan Menu Tidak valid!\nMasukkan Angka Sesuai Menu!') # pilihan tidak sesuai
            print()
            continue
        print()
        
        if opsi1 == 1:
            clear_terminal()
            print('=== Daftar Ikan ===')
            print()
            print(tabulate(ikan, headers='keys',tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center'))) # list seluruh ikan
            print()
            
        elif opsi1 == 2:
            clear_terminal()
            print('=== Daftar Ikan ===')
            print(tabulate(ikan, headers='keys', tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center'))) # list seluruh ikan
            print()
            nyariIkan = input('Masukkan Nama Ikan yang Ingin Dicari: ').title() # memasukkan nama ikan
            
            if nyariIkan in ikan['Nama']: # user input sesuai dengan nama ikan di list utama
                indexReadIkan = ikan['Nama'].index(nyariIkan)
                clear_terminal()
                print(f'Data Ikan {nyariIkan}:')
                print()
                print(f"Nama: {ikan['Nama'][indexReadIkan]}") # tampilan nama ikan
                print(f"Ukuran: {ikan['Ukuran'][indexReadIkan]}") # tampilan ukuran ikan
                print(f"Origin: {ikan['Origin'][indexReadIkan]}") # tampilan origin ikan
                print(f"Stok: {ikan['Stok'][indexReadIkan]}") #  tampilan stok ikan
                print(f"Harga: {ikan['Harga'][indexReadIkan]}") # tampilan harga ikan
                print()
                continue
            else:
                clear_terminal()
                print(f'Ikan Dengan Nama {nyariIkan} Tidak Ditemukan!.') # user input tidak sesuai dengan nama ikan di list utama
                print()
                continue
        elif opsi1 == 3:
            break # kembali ke menu utama
        
        else:
            print('Pilihan Menu Tidak valid!\nMasukkan Angka Sesuai Menu!') # user input tidak sesuai
            print()
            
def pw():
    print('Hanya Karyawan Yang Dapat Mengakses Menu Ini\nSilahkan Masukkan Password!') # berlaku pada menu 2 dan menu 3
    print()
    password = 'PDT0101' # password admin
    
    while True:
        pasword = input('Masukkan Password: ')
        
        if pasword == password: # password admin sesuai dengan yang diinput
            print()
            clear_terminal()
            print('Password Benar!')
            print()
            return True
        else:
            clear_terminal()
            print('Password Salah, Silahkan Masukkan Password ulang: ') # password admin tidak sesuai dengan yang diinput
            print()
    
def nambahIkan():
    while True:
        print('=== Menu Tambah Ikan ===')
        print()
        print('1. Tambah Ikan Baru')
        print('2. Tambah Stok Ikan')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi2 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan (1-3): ')) # memilih submenu pada menu 2
        except ValueError:
            print()
            print('Pilihan Menu Tidak Valid!\nMasukkan Angka Sesuai Menu!') # pilihan tidak sesuai
            continue

        if opsi2 == 1:
            while True:
                print()
                tambahIkan = input('Masukan Nama Ikan Yang Ingin Ditambah: ').title() # user input nama ikan baru
                while True:
                    try:
                        ukuranIkanBaru = int(input('Masukkan Ukuran Ikan (Angka (cm)): ')) # user input ukuran ikan baru
                    except ValueError:
                        print()
                        print('Input Tidak Valid, Harap Masukkan Angka!')
                        print()
                        continue
                    originIkanBaru = input('Masukkan Origin Ikan: ').title() # user input origin ikan baru
                    while True:
                        try:
                            stokIkanBaru = int(input('Masukkan Jumlah Stok Ikan (Angka): ')) # user input stok ikan baru
                        except ValueError:
                            print()
                            print('Input Tidak Valid, Harap Masukkan Angka!')
                            print()
                            continue
                        while True:
                            try:
                                HargaIkanBaru = int(input('Masukkan Harga Ikan (Angka): ')) # user input harga ikan baru
                            except ValueError:
                                print()
                                print('Input Tidak Valid, Harap Masukkan Angka!')
                                print()
                                continue
                            ikan['Nama'].append(tambahIkan) # memasukkan nama ikan baru ke dalam list utama
                            ikan['Ukuran'].append(ukuranIkanBaru) # memasukkan ukuran ikan baru ke dalam list utama
                            ikan['Origin'].append(originIkanBaru) # memasukkan origin ikan baru ke dalam list utama
                            ikan['Stok'].append(stokIkanBaru) # memasukkan stok ikan baru ke dalam list utama
                            ikan['Harga'].append(HargaIkanBaru) # memasukkan harga ikan baru ke dalam list utama
                            print()
                            print(f'Ikan {tambahIkan} Berhasil Ditambahkan!')
                            print()
                            print(tabulate(ikan, headers = 'keys', tablefmt='psql', showindex = 'always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
                            break
                        break
                    break
                break
        elif opsi2 == 2:
            while True:
                print(tabulate(ikan, headers = 'keys', tablefmt='psql', showindex = 'always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
                print()
                tambahStokIkan = input('Masukkan Nama Ikan yang Sudah Ada: ').title() # user input nama ikan yang sudah ada
                if tambahStokIkan in ikan['Nama']:
                    while True:
                        try:
                            jumlahBaru = int(input('Masukkan Jumlah Stok Ikan Tambahan (Angka): ')) # user input jumlah ikan untuk nama ikan yang sudah ada
                        except ValueError:
                            print()
                            print('Input Tidak Valid, Harap Masukkan Angka!')
                            continue
                        indexTambahIkan = ikan['Nama'].index(tambahStokIkan)
                        ikan['Stok'][indexTambahIkan] += jumlahBaru # menambah stok ikan baru dengan stok ikan lama
                        print()
                        print(f'Stok Ikan {tambahStokIkan} Berhasil Ditambahkan!')
                        print()
                        print(tabulate(ikan, headers = 'keys', tablefmt='psql', showindex = 'always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
                        break
                    break
                else:
                    print(f'Ikan {tambahStokIkan} Tidak Ditemukan') # nama ikan tidak ada didalam list utama

        elif opsi2 == 3:
            break # kembali ke menu utama

        else:
            print('Pilihan Menu Tidak valid!\nMasukkan Angka Sesuai Menu!')
            
def deleteIkan ():
    while True:
        print('=== Menu Hapus Ikan ===')
        print()
        print('1. Hapus Ikan')
        print('2. Hapus Sebagian Stok Ikan')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi3 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan (1-3): ')) # user input memilih submenu pada menu 3
        except ValueError:
            print()
            print('Input Tidak Valid, Harap Masukkan Angka.') # user input salah
            print()
            continue
        print()
        
        if opsi3 == 1:
            clear_terminal()
            print(tabulate(ikan, headers='keys', tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
            print()
            hapusIkan = input('Masukkan Nama Ikan yang Ingin Dihapus: ').title() # masukkan nama ikan yang ingin di hapus
            if hapusIkan in ikan['Nama']:
                indexHapusIkan = ikan['Nama'].index(hapusIkan)
                del ikan['Nama'][indexHapusIkan] # menghapus nama ikan
                del ikan['Ukuran'][indexHapusIkan] # menghapus ukuran ikan
                del ikan['Origin'][indexHapusIkan] # menghapus origin ikan
                del ikan['Stok'][indexHapusIkan] # menghapus stok ikan
                del ikan['Harga'][indexHapusIkan] # menghapus harga ikan
                print()
                print(f'Ikan {hapusIkan} Berhasil Dihapus!')
                print()
                print(tabulate(ikan, headers='keys', tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
            else:
                print()
                print(f'Ikan {hapusIkan} Tidak Ditemukan!') # nama ikan tidak ada di list utama
                print()
                
        elif opsi3 == 2:
            clear_terminal()
            print(tabulate(ikan, headers='keys', tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
            print()
            hapusStokIkan = input('Masukkan Nama Ikan yang Ingin Dikurangi Stoknya: ').title() # user input untuk menghapus stok ikan dari ikan yang ada di list utama
    
            if hapusStokIkan in ikan['Nama']: # validasi nama ikan di list utama dengan nama ikan di user input
                indexHapusStokIkan = ikan['Nama'].index(hapusStokIkan)
                print(f'Stok {hapusStokIkan} Yang Tersedia: {ikan["Stok"][indexHapusStokIkan]}')
                while True:
                    try:
                        hapusJumlahStok = int(input('Masukkan Jumlah Stok Yang Ingin Dikurangi (Angka): ')) # user input jumlah stok yang ingin dihapus
                    except ValueError:
                        print('Input Tidak Valid, Harap Masukkan Angka.')
                        continue
                    if hapusJumlahStok > ikan['Stok'][indexHapusStokIkan]: # user input melebihi stok
                        print()
                        print(f'Tidak Bisa Mengurangi Stok Lebih Dari Jumlah Yang Tersedia {ikan["Stok"][indexHapusStokIkan]}.')
                        print()
                    elif hapusJumlahStok < 0:
                        print()
                        print('Jumlah Stok Yang Akan Dikurangi Tidak Boleh Negatif!') # user input negatif
                        print()
                    else:
                        ikan['Stok'][indexHapusStokIkan] -= hapusJumlahStok # mengurangi stok ikan berdasarkan user input
                        print()
                        print(f'Stok Ikan {hapusStokIkan} Berhasil Dikurangi Sebanyak {hapusJumlahStok}!')
                        print()
                        print(tabulate(ikan, headers='keys', tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
                        print()
                        break
            else:
                print()
                print(f'Ikan {hapusStokIkan} Tidak Ditemukan!')
                print()

        elif opsi3 == 3:
            break # kembali ke menu utama
        
        else:
            print('Pilihan Tidak Valid.')
            break

keranjang = [] # list kosong untuk submenu pembayaran pada menu 4
            
def updateIkan():
    while True:
        print()
        print('=== Menu Pembelian Ikan ===')
        print()
        print('1. Pesan Ikan')
        print('2. Pembayaran')
        print('3. Kembali ke Menu Utama')
        print()
        try:
            opsi4 = int(input(f'Masukkan Pilihan Menu Yang Ingin Dijalankan (1-3): ')) # memilih submenu pada menu 4
        except ValueError:
            print()
            print('Input Tidak Valid, Harap Masukkan Angka.')
            continue
        print()
        
        if opsi4 == 1:
            clear_terminal()
            print(tabulate(ikan, headers='keys',tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center', 'center')))
            print()
            beliIkan = input('Masukkan Nama Ikan yang Ingin Dibeli: ').title() # user input nama ikan yang ingin dibeli
            print()
            
            if beliIkan in ikan['Nama']: # validasi nama ikan di list utama dengan user input
                indexBeliIkan = ikan['Nama'].index(beliIkan)
                
                print(f"Stok Tersedia Untuk {beliIkan}: {ikan['Stok'][indexBeliIkan]} Ikan.")
                print()
                while True:
                    try:
                        jumlahBeli = int(input('Masukkan Jumlah Ikan Yang Ingin Dibeli (Angka): ')) # user input jumlah yang ingin dibeli
                    except ValueError:
                        print()
                        print('Harap Masukkan Angka!')
                        print()
                        continue
                    print()
                    totalHarga = jumlahBeli * ikan['Harga'][indexBeliIkan] # total harga
                    
                    while True:
                        if jumlahBeli <= ikan['Stok'][indexBeliIkan]: # pemesanan stok ikan
                            ikan['Stok'][indexBeliIkan] -= jumlahBeli # mengurangi stok ikan di list utama dengan jumlah yang ingin dibeli
                            hargaSatuanIkan = ikan['Harga'][indexBeliIkan]
                            keranjang.append({'Nama': beliIkan, 'Jumlah': jumlahBeli, 'Harga Satuan': hargaSatuanIkan, 'Total Harga': totalHarga}) # memasukkan nama ikan, jumlah, harga satuan, total harga ke dalam keranjang kosong
                            print()
                            print(tabulate(keranjang, headers='keys',tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center')))
                            print()
                            print(f'{jumlahBeli} Ikan {beliIkan} Ditambahkan Ke Keranjang.') # pemberitahuan bahwa ikan sudah ditambah ke keranjang
                            print(f'Total Harga ikan {beliIkan} Sebesar Rp. {totalHarga}') # total harga ikan yang dibeli
                            print()
                            break
                        else:
                            print(f'Stok Ikan {beliIkan} Tidak Cukup!')
                            print()
                            break
                    break
            else:
                print(f'Ikan {beliIkan} Tidak Ditemukan!')
                print()
        elif opsi4 == 2:
            clear_terminal()
            if keranjang:
                    print(tabulate(keranjang, headers='keys',tablefmt='psql', showindex='always', colalign=('center', 'center', 'center', 'center', 'center')))
                    totalPembayaran = sum(item['Total Harga'] for item in keranjang) # menambahkan seluruh total belanja ikan menjadi total pembayaran
                    print()
                    print(f'Total Harga: {totalPembayaran}')
                    while True:
                        print()
                        try:
                            uangBayar = int(input('Masukkan Jumlah Uang: ')) # user input jumlah uang yang ingin dibayar
                        except ValueError:
                            clear_terminal()
                            print('Input tidak valid. Masukkan jumlah uang tanpa separator digit!')
                            print(f'Total Harga: {totalPembayaran}')
                            continue
                        if uangBayar < totalPembayaran: # uang kurang
                            print(f'Transaksi Gagal, Uang Kurang {totalPembayaran - uangBayar}')
                        elif uangBayar == totalPembayaran: # uang pas
                            print('Transaksi Berhasil!')
                            print('Terima Kasih')
                            keranjang.clear()
                            break
                        else:
                            print(f'Transaksi Berhasil!, Uang Kembalian Anda Sebesar Rp.{uangBayar - totalPembayaran}') # uang lebih
                            print('Terima Kasih')
                            keranjang.clear()
                            break
            else:
                print('Tidak ada ikan yang dipesan. Pilih menu 1 untuk memilih ikan.') # keranjang kosong tidak dapat memproses pembayaran
                
        elif opsi4 == 3:
            break # kembali ke menu utama
        
        else:
            print()
            print('Pilihan Menu Tidak Valid!\nMasukkan Angka Sesuai Menu!')
       
def menuUtama():
    while True:
        print()
        print('===== welcome to PredaTank fish store =====')
        print()
        print('List Menu:')
        print()
        print('1. Menampilkan Data ikan')
        print('2. Menambah Ikan')
        print('3. Menghapus Ikan')
        print('4. Membeli Ikan')
        print('5. Exit Program')
        print()

        try:
            menu = int(input('Masukkan Pilihan Menu Ingin Dijalankan (1-5): ')) # memilih menu 1-5
        except ValueError:
            clear_terminal()
            print('Pilihan Menu Tidak valid!\nMasukkan Angka Sesuai Menu!')
            continue
        print()
    
        if menu == 1:
            clear_terminal()
            readIkan ()

        elif menu == 2:
            clear_terminal()
            pw ()
            nambahIkan ()

        elif menu == 3:
            clear_terminal()
            pw ()
            deleteIkan ()

        elif menu == 4:
            clear_terminal()
            updateIkan ()
        
        elif menu == 5:
            clear_terminal()
            print('Terima Kasih!')
            print('Exit Program')
            print()
            break

        else:
            clear_terminal()
            print('Pilihan Menu Tidak valid!\nMasukkan Angka Sesuai Menu!')
        
menuUtama()