data_pengguna = {
    "panitia": {"password": "panitia123", "role": "panitia"},
    "peserta": {"password": "peserta123", "role": "peserta"}
}

data_peserta_lomba = []

def login():
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in data_pengguna and data_pengguna[username]["password"] == password:
            print("Login berhasil!")
            return data_pengguna[username]["role"]
        else:
            print("Username atau password salah. Coba lagi.")

def tambah_peserta():
    print("--- Tambah Peserta ---")
    nama = input("Nama Peserta: ")
    desa = input("Asal Desa: ")
    lomba = input("Lomba yang diikuti: ")
    
    peserta_baru = {
        "nama": nama,
        "desa": desa,
        "lomba": lomba
    }
    data_peserta_lomba.append(peserta_baru)
    print("Peserta berhasil ditambahkan.")

def lihat_data():
    if not data_peserta_lomba:
        print("Belum ada data peserta.")
        return

    print("--- Daftar Peserta Lomba ---")
    for i, peserta in enumerate(data_peserta_lomba):
        print(f"{i+1}. Nama: {peserta['nama']}, Desa: {peserta['desa']}, Lomba: {peserta['lomba']}")

def update_peserta():
    lihat_data()
    if not data_peserta_lomba:
        return
        
    try:
        indeks = int(input("Masukkan nomor urut peserta yang ingin diubah: ")) - 1
        if 0 <= indeks < len(data_peserta_lomba):
            peserta = data_peserta_lomba[indeks]
            
            print(f"--- Ubah Data Peserta {peserta['nama']} ---")
            nama_baru = input(f"Nama baru (kosongkan jika tidak diubah): ")
            desa_baru = input(f"Desa baru (kosongkan jika tidak diubah): ")
            lomba_baru = input(f"Lomba baru (kosongkan jika tidak diubah): ")
            
            if nama_baru:
                peserta['nama'] = nama_baru
            if desa_baru:
                peserta['desa'] = desa_baru
            if lomba_baru:
                peserta['lomba'] = lomba_baru
            
            print("Data peserta berhasil diperbarui.")
        else:
            print("Nomor urut tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
    except KeyboardInterrupt:
        print("Jangan menekan CTRL + C.")
    except KeyError:
        print("Tidak ada dalam dictionary.")
    except IndexError:
        print("Indeks tidak valid.")
    except TypeError:
        print("Input tidak valid.")

def hapus_peserta():
    lihat_data()
    if not data_peserta_lomba:
        return
        
    try:
        indeks = int(input("Masukkan nomor urut peserta yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(data_peserta_lomba):
            peserta_dihapus = data_peserta_lomba.pop(indeks)
            print(f"Peserta atas nama '{peserta_dihapus['nama']}' berhasil dihapus.")
        else:
            print("Nomor urut tidak valid.")
    except ValueError:
        print("Input tidak valid. Masukkan angka.")
    except KeyboardInterrupt:
        print("Jangan menekan CTRL + C.")
    except KeyError:
        print("Tidak ada dalam dictionary.")
    except IndexError:
        print("Indeks tidak valid.")
    except TypeError:
        print("Input tidak valid.")

print("Sistem Pencatatan Peserta Lomba Antar Desa")

while True:
    role = login()
    
    while True:
        print("="*40)
        print("Menu Utama")
        print("="*40)
        
        if role == "panitia":
            print("1. Tambah Peserta")
            print("2. Lihat Data Peserta")
            print("3. Ubah Data Peserta")
            print("4. Hapus Peserta")
            print("5. Logout")
            print("6. Keluar Program")
            
            try:
                pilihan = int(input("Pilih menu (1-6): "))
                if pilihan == 1:
                    tambah_peserta()
                elif pilihan == 2:
                    lihat_data()
                elif pilihan == 3:
                    update_peserta()
                elif pilihan == 4:
                    hapus_peserta()
                elif pilihan == 5:
                    print("Anda telah logout.")
                    break  
                elif pilihan == 6:
                    print("Terima kasih, sampai jumpa!")
                    exit() 
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
            except KeyboardInterrupt:
                print("Jangan menekan CTRL + C.")
            except KeyError:
                print("Tidak ada dalam dictionary.")
            except IndexError:
                print("Indeks tidak valid.")
            except TypeError:
                print("Input tidak valid.")

        elif role == "peserta":
            print("1. Lihat Data Peserta")
            print("2. Logout")
            print("3. Keluar Program")
            
            try:
                pilihan = int(input("Pilih menu (1-3): "))
                if pilihan == 1:
                    lihat_data()
                elif pilihan == 2:
                    print("Anda telah logout.")
                    break  
                elif pilihan == 3:
                    print("Terima kasih, sampai jumpa!")
                    exit()
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
            except KeyboardInterrupt:
                print("Jangan menekan CTRL + C.")
            except KeyError:
                print("Tidak ada dalam dictionary.")
            except IndexError:
                print("Indeks tidak valid.")
            except TypeError:
                print("Input tidak valid.")