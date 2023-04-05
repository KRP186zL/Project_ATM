import os
import fungsi
import time
#Runnning
while True:
#Tampilan Awal
    while fungsi.fungsi_fungsi.status_login == False:
        os.system("clear")
        try:
            print(f""" {'='*70}\n| {'|':>70}
|{'Bank Wibu Negara Indonesia':^70}| 
|{'JL.Menuju Isekai No. 27':^70}|
|{'Telp: 0270403':^70}|
|{'Email: Wibu@wibu.co.isk ':^70}|
| {'|':>70}
|{'-'*70}|
| {'|':>70}
|{time.asctime(time.localtime(time.time())):>65} {'|':>5}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
|     {'ingin mengirim uang ke waifu anda yang ada di isekai ?'.upper()} {'|':>11}
|     {'anda datang di bank yang tepat !'.upper()} {'|':>33}
| {'|':>70}
|     {'Login untuk melakuan transaksi'.upper()} {'|':>35}
|     {'Belom memiliki akun?'.upper()} {'|':>45}
| {'|':>70}
| {'|':>70}
|     {'Silahkan daftar terlebih dahulu !'.upper()} {'|':>32}
| {'|':>70}
| {'|':>70}
|     {'Pilih'.upper()} : {'|':>58}
| {'|':>70}
|     {'1. Login'.upper()} {'|':>57}
|     {'2. Daftar'.upper()} {'|':>56}
|     {'3. Lupa/Ganti Pin'.upper()} {'|':>48}
|     {'4. Keluar'.upper()} {'|':>56}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
            menu_awal = int(input("\n Masukkan Pilihan Anda: "))
            if (menu_awal == 1):
                fungsi.fungsi_fungsi.login()
                continue
            elif (menu_awal == 2):
                fungsi.fungsi_fungsi.daftar()
                continue
            elif (menu_awal == 3):
                fungsi.fungsi_fungsi.ganti_pin(input(" Masukkan Nomor ATM yang ingin diganti Pin nya: "))
                time.sleep(1.5)
                continue
            elif (menu_awal == 4):
                print("\n Terimakasih sudah menggunakan layanan kami ! \n\n\n\n\n\n\n\n\n\n\n\n PESAN RAHASIA!\n Saya harap anda sadar, bahwa Waifu anda itu tidaklah nyata...")
                exit()
            else:
                print("\n Pilihan tidak tersedia !")
                time.sleep(1.5)
                continue
        except ValueError:
            print("\n Mohon gunakan angka untuk memilih Menu !")
            time.sleep(1.5)
            continue

#Tampilan Setelah Login
    while fungsi.fungsi_fungsi.status_login == True:
        panjang_username = 67 - 18
        os.system("clear")
        print(f""" {'='*70}\n| {'|':>70}
|{'Bank Wibu Negara Indonesia':^70}| 
|{'JL.Menuju Isekai No. 27':^70}|
|{'Telp: 0270403':^70}|
|{'Email: Wibu@wibu.co.isk ':^70}|
| {'|':>70}
|{'-'*70}|
| {'|':>70}
|{time.asctime(time.localtime(time.time())):>65} {'|':>5}
| {'|':>70}
| {'Selamat datang,':>18} {'|':>51}
| {fungsi.fungsi_fungsi.username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Menu:'.upper()} : {'|':>58}
| {'|':>70}
|     {'1. Transfer'.upper()} {'|':>54}
|     {'2. Cek Saldo'.upper()} {'|':>53}
|     {'3. Setor Tunai'.upper()} {'|':>51}
|     {'4. Tarik Tunai'.upper()} {'|':>51}
|     {'5. Logout'.upper()} {'|':>56}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        while True:
            try:
                menu = int(input(" Silahkan Pilih Menu: "))
                if menu == 1:
                    fungsi.fungsi_fungsi.transfer()
                elif menu == 2:
                    fungsi.fungsi_fungsi.cek_saldo()
                elif menu == 3:
                    fungsi.fungsi_fungsi.setor_tunai()
                elif menu == 4:
                    fungsi.fungsi_fungsi.tarik_tunai()
                elif menu == 5:
                    print("\n\n Berhasil Logout !")
                    print("\n Terimakasih sudah menggunakan layanan kami :)")
                    time.sleep(1.5)
                    fungsi.fungsi_fungsi.status_login = False
                    break
            except ValueError:
                print(" Gunakan angka untuk memilih !")
                time.sleep(1.5)
                break
            break