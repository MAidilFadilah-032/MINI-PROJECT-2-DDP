data_pengguna = { ... } = Mendefinisikan sebuah kamus (dictionary) global. Kamus ini menyimpan data otentikasi (username, password, dan role) yang telah ditetapkan untuk pengguna "panitia" dan "peserta".

data_peserta_lomba = [] = Mendefinisikan sebuah daftar (list) kosong global. List ini adalah tempat semua data peserta lomba akan disimpan dan diolah selama program berjalan.

def login(): = Mendeklarasikan fungsi yang bertugas untuk menangani proses login pengguna.

while True: = Memulai perulangan tak terbatas. Perulangan ini memastikan pengguna harus memasukkan username dan password hingga berhasil.

username = input("Masukkan username: ") = Menerima input username dari pengguna.

password = input("Masukkan password: ") = Menerima input password dari pengguna.

if username in data_pengguna and data_pengguna[username]["password"] == password:= Melakukan pengecekan kondisi: apakah username ada dalam kamus data_pengguna DAN apakah password yang dimasukkan sesuai dengan password yang tersimpan.

print("Login berhasil!") = Mencetak pesan keberhasilan login.

return data_pengguna[username]["role"] = Mengembalikan peran (role) pengguna (panitia atau peserta) yang berhasil login, lalu mengakhiri fungsi.

else:= Blok kode yang dijalankan jika kondisi pengecekan login gagal.

print("Username atau password salah. Coba lagi.") = Mencetak pesan kegagalan, dan perulangan akan kembali ke awal.

Mendeklarasikan fungsi untuk menambahkan entri peserta baru.

print("--- Tambah Peserta ---") = Mencetak judul sub-menu.

nama = input("Nama Peserta: ") = Menerima input data Nama Peserta.

desa = input("Asal Desa: ") = Menerima input data Asal Desa.

lomba = input("Lomba yang diikuti: ") = Menerima input data Lomba yang diikuti.

peserta_baru = { ... } = Membuat kamus baru (peserta_baru) dengan tiga kunci-nilai dari data yang baru diinput.

data_peserta_lomba.append(peserta_baru) = Menambahkan kamus peserta_baru ke dalam list global data_peserta_lomba.

print("Peserta berhasil ditambahkan.") = Mencetak pesan konfirmasi penambahan data.

def lihat_data(): = Mendeklarasikan fungsi untuk menampilkan semua data peserta.

if not data_peserta_lomba: return = Memeriksa apakah list data_peserta_lomba kosong. Jika ya, mencetak pesan "Belum ada data peserta." dan mengakhiri fungsi (return).

print("--- Daftar Peserta Lomba ---") = Mencetak judul daftar.

for i, peserta in enumerate(data_peserta_lomba): = Memulai perulangan melalui list. Fungsi enumerate memberikan indeks (i) dan item data peserta (peserta) pada setiap iterasi.

print(f"{i+1}. Nama: {peserta['nama']}, ...") = Mencetak detail peserta, menggunakan i+1 untuk memastikan nomor urut dimulai dari 1.

def update_peserta(): = Mendeklarasikan fungsi untuk mengubah data peserta yang sudah ada.

lihat_data() = Memanggil fungsi tampil data sebagai referensi agar pengguna tahu nomor urut yang akan diubah.

if not data_peserta_lomba: return = Menghentikan fungsi jika list kosong (sudah diperiksa di lihat_data(), tapi ini adalah pengamanan tambahan).

try: = Memulai blok penanganan kesalahan (Exception Handling) untuk mengantisipasi input yang tidak valid.

indeks = int(input(...)) - 1 = Menerima nomor urut dari pengguna, mengonversinya ke integer, dan mengurangi 1 untuk mendapatkan indeks list yang benar.

if 0 <= indeks < len(data_peserta_lomba): = Memeriksa apakah indeks yang dihasilkan valid (berada dalam jangkauan list).

peserta = data_peserta_lomba[indeks] = Mengambil kamus data peserta yang akan diubah berdasarkan indeks yang valid.

print(f"--- Ubah Data Peserta {peserta['nama']} ---") = Mencetak judul perubahan dengan nama peserta saat ini.

nama_baru = input(...) dst. = Menerima input data baru untuk Nama, Desa, dan Lomba.

if nama_baru: peserta['nama'] = nama_baru dst. = Memperbarui nilai dalam kamus peserta hanya jika input data baru tidak kosong (kosong berarti data lama dipertahankan).

print("Data peserta berhasil diperbarui.") = Mencetak konfirmasi.

else: print("Nomor urut tidak valid.") = Menampilkan pesan jika indeks di luar batas valid.

except ValueError: = Menangani kesalahan jika input nomor urut bukan angka.

except KeyboardInterrupt: = Menangani kesalahan jika pengguna menekan CTRL + C saat input.

except KeyError: = Menangani kesalahan jika mencoba mengakses kunci kamus yang tidak ada.

except IndexError: = Menangani kesalahan jika indeks yang dimasukkan di luar jangkauan list.

except TypeError: = Menangani kesalahan jika ada operasi yang dilakukan pada tipe data yang salah.

def hapus_peserta(): = Mendeklarasikan fungsi untuk menghapus data peserta.

lihat_data() = Memanggil fungsi tampil data sebagai referensi.

if not data_peserta_lomba: return = Menghentikan fungsi jika list kosong.

try: = Memulai blok penanganan kesalahan.

indeks = int(input(...)) - 1 = Menerima nomor urut dan mengonversinya menjadi indeks list.

if 0 <= indeks < len(data_peserta_lomba): = Memastikan indeks valid.

peserta_dihapus = data_peserta_lomba.pop(indeks) = Menghapus item pada indeks dari list dan menyimpan item yang dihapus.

print(f"Peserta atas nama '{peserta_dihapus['nama']}' berhasil dihapus.") = Mencetak konfirmasi penghapusan.

else: print("Nomor urut tidak valid.") = Menampilkan pesan jika indeks di luar batas.

except ValueError: = Menangani kesalahan jika input nomor urut bukan angka.

except KeyboardInterrupt: = Menangani kesalahan jika pengguna menekan CTRL + C saat input.

except KeyError: = Menangani kesalahan jika mencoba mengakses kunci kamus yang tidak ada.

except IndexError: = Menangani kesalahan jika indeks yang dimasukkan di luar jangkauan list.

except TypeError: = Menangani kesalahan jika ada operasi yang dilakukan pada tipe data yang salah.

print("Sistem Pencatatan Peserta Lomba Antar Desa") = Mencetak judul program.

while True: = Memulai perulangan utama yang akan terus berjalan hingga pengguna memilih keluar.

role = login() = Memanggil fungsi login() dan menyimpan peran pengguna yang berhasil login.

while True: = Memulai perulangan Menu Utama; akan terus berjalan sampai logout atau exit.

print("="*40) / print("Menu Utama") = Mencetak dekorasi dan judul menu.

if role == "panitia": = Memeriksa peran. Jika panitia, program akan:

Mencetak opsi menu lengkap (1-6).

try: pilihan = int(input(...)) = Menerima input menu panitia.

if pilihan == 1: tambah_peserta() dst. = Menjalankan fungsi terkait pilihan (Tambah, Lihat, Ubah, Hapus).

elif pilihan == 5: break = Pilihan Logout, keluar dari perulangan menu internal dan kembali ke login().

elif pilihan == 6: exit() = Pilihan Keluar Program, menghentikan eksekusi.

else: print("Pilihan tidak valid...") = Menangani pilihan angka di luar 1-6.

except ValueError: = Menangani kesalahan jika input nomor urut bukan angka.

except KeyboardInterrupt: = Menangani kesalahan jika pengguna menekan CTRL + C saat input.

except KeyError: = Menangani kesalahan jika mencoba mengakses kunci kamus yang tidak ada.

except IndexError: = Menangani kesalahan jika indeks yang dimasukkan di luar jangkauan list.

except TypeError: = Menangani kesalahan jika ada operasi yang dilakukan pada tipe data yang salah.

elif role == "peserta":: Memeriksa peran. Jika peserta, program akan:

Mencetak opsi menu terbatas (1-3).

try: pilihan = int(input(...)): Menerima input menu peserta.

if pilihan == 1: lihat_data(): Menjalankan fungsi Lihat Data.

elif pilihan == 2: break: Pilihan Logout.

elif pilihan == 3: exit(): Pilihan Keluar Program.

else: print("Pilihan tidak valid..."): Menangani pilihan angka di luar 1-3.

except ValueError: = Menangani kesalahan jika input nomor urut bukan angka.

except KeyboardInterrupt: = Menangani kesalahan jika pengguna menekan CTRL + C saat input.

except KeyError: = Menangani kesalahan jika mencoba mengakses kunci kamus yang tidak ada.

except IndexError: = Menangani kesalahan jika indeks yang dimasukkan di luar jangkauan list.

except TypeError: = Menangani kesalahan jika ada operasi yang dilakukan pada tipe data yang salah.

==================================================================================================================================================================================================================

