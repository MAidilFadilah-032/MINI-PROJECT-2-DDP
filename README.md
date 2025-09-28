Nama: Muhammad Aidil Fadilah\
Nim: 2509116032\
Kelas: Sistem Informasi (A) 2025

============================================================================================

data_pengguna = { ... } = Mendefinisikan sebuah kamus (dictionary) global. Kamus ini menyimpan data otentikasi (username, password, dan role) yang telah ditetapkan untuk pengguna "panitia" dan "peserta".

data_peserta_lomba = [] = Mendefinisikan sebuah daftar (list) kosong global. List ini adalah tempat semua data peserta lomba akan disimpan dan diolah selama program berjalan.

def login(): = Mendeklarasikan fungsi yang bertugas untuk menangani proses login pengguna.

while True: = Memulai perulangan tak terbatas. Perulangan ini memastikan pengguna harus memasukkan username dan password hingga berhasil.

username = input("Masukkan username: ") = Menerima input username dari pengguna.

password = input("Masukkan password: ") = Menerima input password dari pengguna.

if username in data_pengguna and data_pengguna[username]["password"] == password: = Melakukan pengecekan kondisi, apakah username ada dalam kamus data_pengguna DAN apakah password yang dimasukkan sesuai dengan password yang tersimpan.

print("Login berhasil!") = Mencetak pesan keberhasilan login.

return data_pengguna[username]["role"] = Mengembalikan peran (role) pengguna (panitia atau peserta) yang berhasil login, lalu mengakhiri fungsi.

else:= Blok kode yang dijalankan jika kondisi pengecekan login gagal.

print("Username atau password salah. Coba lagi.") = Mencetak pesan kegagalan, dan perulangan akan kembali ke awal.

def tambah_peserta(): = Mendeklarasikan fungsi untuk menambahkan entri peserta baru.

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

nama_baru = input(...) dan seterusnya. = Menerima input data baru untuk Nama, Desa, dan Lomba.

if nama_baru: peserta['nama'] = nama_baru dan seterusnya. = Memperbarui nilai dalam kamus peserta hanya jika input data baru tidak kosong (kosong berarti data lama dipertahankan).

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

if role == "panitia": = Memeriksa peran. Jika panitia, program akan Mencetak opsi menu lengkap (1-6).

try: pilihan = int(input(...)) = Menerima input menu panitia.

if pilihan == 1: tambah_peserta() dan seterusnya. = Menjalankan fungsi terkait pilihan (Tambah, Lihat, Ubah, Hapus).

elif pilihan == 5: break = Pilihan Logout, keluar dari perulangan menu internal dan kembali ke login().

elif pilihan == 6: exit() = Pilihan Keluar Program, menghentikan eksekusi.

else: print("Pilihan tidak valid...") = Menangani pilihan angka di luar 1-6.

except ValueError: = Menangani kesalahan jika input nomor urut bukan angka.

except KeyboardInterrupt: = Menangani kesalahan jika pengguna menekan CTRL + C saat input.

except KeyError: = Menangani kesalahan jika mencoba mengakses kunci kamus yang tidak ada.

except IndexError: = Menangani kesalahan jika indeks yang dimasukkan di luar jangkauan list.

except TypeError: = Menangani kesalahan jika ada operasi yang dilakukan pada tipe data yang salah.

elif role == "peserta": = Memeriksa peran. Jika peserta, program akan Mencetak opsi menu terbatas (1-3).

try: pilihan = int(input(...)) = Menerima input menu peserta.

if pilihan == 1: lihat_data() = Menjalankan fungsi Lihat Data.

elif pilihan == 2: break = Pilihan Logout.

elif pilihan == 3: exit(): = Pilihan Keluar Program.

else: print("Pilihan tidak valid..."): = Menangani pilihan angka di luar 1-3.

except ValueError: = Menangani kesalahan jika input nomor urut bukan angka.

except KeyboardInterrupt: = Menangani kesalahan jika pengguna menekan CTRL + C saat input.

except KeyError: = Menangani kesalahan jika mencoba mengakses kunci kamus yang tidak ada.

except IndexError: = Menangani kesalahan jika indeks yang dimasukkan di luar jangkauan list.

except TypeError: = Menangani kesalahan jika ada operasi yang dilakukan pada tipe data yang salah.

============================================================================================
<img width="1640" height="357" alt="Screenshot 2025-09-28 192927" src="https://github.com/user-attachments/assets/3d7ff1e5-c74a-4235-ad5a-3d1f304d307f" />
Pertama kita akan mulai dengan memasukan username dan password, setelahnya kita akan ditampilkan beberapa menu pilihan.

<img width="1618" height="908" alt="Screenshot 2025-09-28 193021" src="https://github.com/user-attachments/assets/8cfab7ab-80f5-49f8-ba4f-e5bf4ed11245" />
Selanjutnya kita bisa menambahkan peserta lomba dengan mengisi nama, desa, dan juga lomba yang mereka ikutkan, lalu setelah itu kita bisa melihat data peserta.

<img width="1637" height="299" alt="Screenshot 2025-09-28 193114" src="https://github.com/user-attachments/assets/4b8ef171-411a-4627-adfe-303744f9b268" />
Panitia juga dapat menghapus peserta yang ingin di hilangkan, disini kita akan menghapus peserta Aidil.

<img width="1630" height="260" alt="Screenshot 2025-09-28 193135" src="https://github.com/user-attachments/assets/14a14f10-a08a-42cd-b7ee-a28942e2be44" />
setelah menghapus aidil kita dapat melakukan pengecekan ulang dengan opsi melihat data peserta.

<img width="1632" height="263" alt="Screenshot 2025-09-28 193200" src="https://github.com/user-attachments/assets/f5f78d3f-6178-45c3-8e7d-e8a75574516d" />
Opsi selanjutnya adalah Log out kita akan berganti ke pengguna lain.

<img width="1642" height="221" alt="Screenshot 2025-09-28 193231" src="https://github.com/user-attachments/assets/e9069380-7652-46ea-9b89-35c796f65bd1" />
Disini kita masuk kembali sebagai peserta dan sudah ada tampilan menu seperti, melihat data peserta, log out, dan juga keluar program.

<img width="1640" height="200" alt="Screenshot 2025-09-28 193245" src="https://github.com/user-attachments/assets/a03518e5-dc78-4c0d-8c3d-6bda1a2ba4dc" />
Jika user memilih opsi untuk melihat daftar peserta makan user akan melihat data yang telah diupdate oleh panitia.

<img width="1631" height="198" alt="Screenshot 2025-09-28 193332" src="https://github.com/user-attachments/assets/bdde953d-29a5-4568-ae70-45dbcc29310c" />
Dan opsi terakhir adalah keluar, jika user menekan keluar maka program akan langsung berhenti.

============================================================================================

<img width="1155" height="712" alt="Screenshot 2025-09-28 203230" src="https://github.com/user-attachments/assets/46df8f4c-b8e5-49d3-9442-57644acc3839" />


Pada bagian pertama flowchart kita mulai memasukan username dan password.

setelah itu program akan mengecek ulang, jika salah akan disuruh untuk mengisi ulang kembali, namun jika benar akan lanjut ke program berikutnya.

**Apakah role yang kita ambil adalah panitia, jika iya maka kita punya kendali lebih terhadap praogram, lalu kita akan di bawa ke bagian menu panitia dan terdapat 6 pilihan seperti TAMBAH PESERTA, LIHAT DATA PESERTA, UBAH DATA PESERTA, HAPUS PESERTA, LOG OUT, DAN KELUAR.**

Pertama kita akan ke TAMBAH PESERTA terlebih dahulu di dalam program ini kita bisa mengisi nama, desa, dan lomba yang akan di ikutkan.

Kedua adalah LIHAT DATA PESERTA kita dapat melihat peserta yang sudah kita tambahkan sebelumnya.

Ketiga UBAH DATA PESERTA Panitia dapat mengubah informasi peserta, dimulai dari memilih peserta dengan indeks yang kita pilih, lalu kita akan disuruh untuk mengisi ulang nama, desa, dan lomba yang akan diikutkan.

Keempat HAPUS DATA PESERTA, ini berfungsi untuk menghapus informasi peserta, kita dapat memilih peserta dengan nomor indeks mereka dan akan langsung dihapus.

Kelima LOG OUT, Kita dapat log out untuk mengganti role yang kita inginkan, seperti dari panitia menjadi peserta.

Keenam dan yang terakhir adalah Keluar, jika kita ingin menutup program kita bisa memilih opsi ini.

**Jika kita memilih role peserta maka kita akan mendapatkan beberapa pilihan menu seperti LIHAT DATA PESERTA, LOG OUT, DAN KELUAR**

Pertama LIHAT DATA PESERTA kita sebagai peserta hanya bisa melihat data yang sudah di tambahkan oleh panitia dengan opsi ini.

Kedua LOG OUT kita dapat berganti ke peserta lain atau role lain dengan pilihan ini.

Ketiga KELUAR jika peserta ingin keluar dari program ia bisa memilih opsi ini.













