# CAPSTONE PROJECT 1 : TOKO IKAN

## 1. Program Toko Ikan

Program ini merupakan aplikasi sederhana yang dibuat menggunakan aplikasi python. Program ini dibuat untuk membantu karyawan toko ikan dalam melihat data ikan, menambah ikan baru, menambah stok ikan, menghapus data ikan serta membantu karyawan untuk melakukan transaksi dengan pelanggan.

## 2. Fitur Utama

- Tampilkan data ikan --> Karyawan toko dapat melihat data seluruh ikan maupun dengan menginput nama ikan tertentu yang ingin di lihat.
- Tambah ikan --> Karyawan toko dapat menambah ikan baru maupun menambah stok ikan. Karyawan toko dapat mengakses menu ini dengan memasukkan password.
- Hapus ikan --> Karyawan toko dapat menghapus ikan maupun mengurangi stok ikan. Karyawan toko dapat mengakses menu ini dengan memasukkan password.
- Pembelian ikan --> Karyawan toko dapat menginput nama ikan beserta jumlah ikan berdasarkan permintaan pelanggan, kemudian dilanjutkan ke proses pembayaran.

## 3. CRUD Function

- Create (menambah data) --> menambah ikan baru dengan mengakses fitur menu tambah ikan. Karyawan menambah ikan dengan memasukkan nama ikan, ukuran ikan, origin ikan, stok ikan dan harga ikan tersebut.
- Read (membaca data) --> membaca data ikan dengan mengakses fitur menu tampilkan data ikan. karyawan dapat membaca data ikan dengan mengakses submenu yang tersedia.
- Update (mengubah data) --> mengubah data akan terjadi jika adanya proses transaksi dengan pelanggan. stok ikan yang ada akan berkurang setelah pelanggan melakukan transaksi.
- Delete (menghapus data) --> menghapus ikan dengan mengakses fitur menu hapus ikan. karyawan dapat menghapus keseluruhan ikan maupun hanya mengurangi stok ikan jika terjadi sesuatu yang menyebabkan ikan tersebut harus di hapus.

## 4. Struktur Data

- `index` --> angka unik untuk mengidentifikasi ikan
- `nama ikan` --> (string) nama ikan
- `ukuran`  --> (integer) ukuran ikan ditulis dengan satuan pengukuran centimeter
- `origin` --> (string) nama daerah habitat asli ikan tersebut
- `stok` --> (integer) jumlah ikan yang tersedia
- `harga` --> (integer) harga per ekor ikan

## 5. Panduan Pengguna

- Gunakan python untuk menjalankan program
- Pilih menu dengan menginput angka sesuai menu yang tersedia
- Masukkan data sesuai petunjuk
- Keluar dari program dengan memilih menu yang tersedia

---

Adrian Irsanda Boestamam

JCDS 2602, Purwadhika Digital Technology School, BSD

2025