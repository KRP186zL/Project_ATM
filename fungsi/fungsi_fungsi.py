import os
import time
import random
import string
from getpass import getpass
status_login = False
user = {
    "1":{
    "no_atm": "1",
    "pin": "1",
    "nama": "Krisna Rizki Pratama",
    "alamat": "Sukajadi",
    "no_telp": "082281258929",
    "email": "shylpie27@gmail.com",
    "saldo": 99999999999,
    "pin_salah": 0,
    "akun":"aktif",
    "transaksi":[]
    },
    "2":{
    "no_atm": "2",
    "pin": "1",
    "nama": "Shylpie",
    "alamat": "Sukajadi",
    "no_telp": "082281258929",
    "email": "shylpie27@gmail.com",
    "saldo": 0,
    "pin_salah": 0,
    "akun":"aktif",
    "transaksi":[]
    }
}


#Function
def login():
    global login_no_atm
    while True:
        os.system("clear")
        print(f"{'SELAMAT DATANG DI BANK WIBU INDONESIA':^70}\n{'SILAHKAN LOGIN TERLEBIH DAHULU!':^70}\n\n")
        try:
            login_no_atm = int(input((" Masukkan Nomor ATM anda: ")))
            break
        except ValueError:
            print("\n Nomor ATM harus menggunakan angka !")
            time.sleep(1.5)
            continue
            
    while True:
        try:
            login_password = int(getpass("\n Masukkan Pin\t\t: "))
            break
        except ValueError:
            print(" Pin harus menggunakan angka ! !")
            time.sleep(1.5)
            clear_pin_status_login()

    cek_status_login(str(login_no_atm),str(login_password))



# buat clear biodata
def clear_biodata():
    os.system("clear")
    print(f'\n{"PROSES PENDAFTARAN BANK WIBU INDONESIA":^70}\n{"SILAHKAN ISI DATA DIRI ANDA!":^70}\n\n')
    daftar_nama = []
    daftar_alamat= []
    daftar_no_telp = []
    daftar_email = []
    if len(nama) > 0 :
        daftar_nama.append(nama)
        for i in daftar_nama:
            print(f" Masukkan Nama anda\t\t\t: {i}")
        if len(alamat) > 0:
            daftar_alamat.append(alamat)
            for j in daftar_alamat:
                print(f" Masukkan Alamat\t\t\t: {j}") 
                if "@gmail" in email:
                    daftar_email.append(email)
                    for l in daftar_email:
                        print(f" Masukkan Email anda\t\t\t: {l}")
                    if no_telp.startswith("628") or no_telp.startswith("+628"):
                        if validasi_no_hp(no_telp):
                            daftar_no_telp.append(no_telp)
                            for k in daftar_no_telp:
                                print(f" Masukkan No HP anda(+628 Indonesia)\t: {k}")
                    else:
                        pass
                else:
                    pass
        else:
            pass
    else:
        pass



def clear_biodata_ganti_pin():
    os.system("clear")
    print(f"{'SELAMAT DATANG DI BANK WIBU INDONESIA':^70}")
    print(f'{" Silahkan isi data dibawah untuk mengganti Pin".upper():^70}\n\n')
    daftar_nama = []
    daftar_alamat= []
    daftar_no_telp = []
    daftar_email = []
    if len(ganti_pin_nama) > 0 :
        daftar_nama.append(ganti_pin_nama)
        for i in daftar_nama:
            print(f" Masukkan Nama anda\t\t\t: {i}")
        if len(ganti_pin_alamat) > 0:
            daftar_alamat.append(ganti_pin_alamat)
            for j in daftar_alamat:
                print(f" Masukkan Alamat\t\t\t: {j}") 
                if "@gmail" in ganti_pin_email:
                    daftar_email.append(ganti_pin_email)
                    for l in daftar_email:
                        print(f" Masukkan Email anda\t\t\t: {l}")
                    if ganti_pin_no_telp.startswith("628") or ganti_pin_no_telp.startswith("+628"):
                        if validasi_no_hp(ganti_pin_no_telp):
                            daftar_no_telp.append(ganti_pin_no_telp)
                            for k in daftar_no_telp:
                                print(f" Masukkan No HP anda(+628 Indonesia)\t: {k}")
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass



def clear_biodata_buka_blokir():
    os.system("clear")
    print(f"{'SELAMAT DATANG DI BANK WIBU INDONESIA':^70}")
    print(f'{"Silahkan isi data dibawah untuk membuka blokir".upper():^70}\n\n')
    daftar_nama = []
    daftar_alamat= []
    daftar_no_telp = []
    daftar_email = []
    if len(ganti_pin_nama) > 0 :
        daftar_nama.append(ganti_pin_nama)
        for i in daftar_nama:
            print(f" Masukkan Nama anda\t\t\t: {i}")
        if len(ganti_pin_alamat) > 0:
            daftar_alamat.append(ganti_pin_alamat)
            for j in daftar_alamat:
                print(f" Masukkan Alamat\t\t\t: {j}") 
                if "@gmail" in ganti_pin_email:
                    daftar_email.append(ganti_pin_email)
                    for l in daftar_email:
                        print(f" Masukkan Email anda\t\t\t: {l}")
                    if ganti_pin_no_telp.startswith("628") or ganti_pin_no_telp.startswith("+628"):
                        if validasi_no_hp(ganti_pin_no_telp):
                            daftar_no_telp.append(ganti_pin_no_telp)
                            for k in daftar_no_telp:
                                print(f" Masukkan No HP anda(+628 Indonesia)\t: {k}")
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass



def clear_pin_status_login():
    os.system("clear")
    print(f"{'SELAMAT DATANG DI BANK WIBU INDONESIA':^70}\n{'SILAHKAN LOGIN TERLEBIH DAHULU!':^70}\n\n")
    nomor_kartu = []
    nomor_kartu.append(login_no_atm)
    for nom_kartu in nomor_kartu:
        print(f" Masukkan Nomor ATM anda: {nom_kartu}")



def ulangi_pin_salah(ulang_login_no_atm:int)->int:
    user[str(login_no_atm)]["pin_salah"]+=1
    print(" Pin yang anda masukkan salah !")
    print("\n 3x salah Pin akun anda akan terblokir !".upper())
    print(f" Jumlah salah: ",user[str(login_no_atm)]["pin_salah"])
    if user[str(login_no_atm)]["pin_salah"] == 3:
        #Bug buka blokir
        blokir(ulang_login_no_atm)
    else:
        while True:
            lanjut_salah = input ('\n Tekan enter untuk lanjut/ketik "keluar" untuk keluar: ').lower()
            if lanjut_salah == "keluar":
                break
            else:
                while True:
                    clear_pin_status_login()
                    login_password_ulang = getpass("\n Masukkan Pin\t\t: ")
                    if validasi_pin(login_password_ulang) == False:
                        time.sleep(1.5)
                        continue
                    else:
                        break
            if login_password_ulang == user[ulang_login_no_atm]["pin"]:
                cek_status_login(ulang_login_no_atm,login_password_ulang)

            else:
                user[str(login_no_atm)]["pin_salah"]+=1
                if user[str(login_no_atm)]["pin_salah"] == 3:
                    #Bug buka blokir
                    blokir(ulang_login_no_atm)
                    break
                else:
                    print(" Pin yang anda masukkan salah !")
                    print("\n 3x salah Pin akun anda akan terblokir !".upper())
                    print(f" Jumlah salah: ",user[str(login_no_atm)]["pin_salah"])
                    continue
            break

                
            
def cek_status_login(login_no_atm:int,login_password:int)->int:
    if login_no_atm in user:
        global status_login
        if user[login_no_atm]["akun"] == "aktif":
                if login_password == user[login_no_atm]["pin"]:
                    print(" Login berhasil")
                    status_login = True
                    time.sleep(1.5)
                else:
                    ulangi_pin_salah(login_no_atm)
        else:
            print(" Akun anda telah terblokir !")
            apakah_buka_blokir = input(" Buka blokir akun ? [y/n]: ").lower()
            if apakah_buka_blokir == "y":
                buka_blokir(login_no_atm)
            else:
                pass
    else:
        print("\n Nomor ATM yang anda masukkan salah !")
        time.sleep(1.5)
        login()


    
def ganti_pin(ubah_pin:int)->int:
    global ganti_pin_nama,ganti_pin_alamat,ganti_pin_email,ganti_pin_no_telp
    os.system("clear")
    if ubah_pin in user:
        if user[ubah_pin]["akun"]=="aktif":
        # print(" Selamat datang,\n",user[ubah_pin]["nama"]+"\n")
            print(f"{'SELAMAT DATANG DI BANK WIBU INDONESIA':^70}")
            print(f'{" Silahkan isi data dibawah untuk mengganti Pin".upper():^70}\n\n')
            while True:
                ganti_pin_nama = input(" Masukkan Nama anda\t\t\t: ").replace("   "," ").replace("  "," ").lstrip().rstrip()
                if ganti_pin_nama == "":
                    print("\n Nama tidak boleh kosong !\n")
                    time.sleep(1.5)
                    clear_biodata_ganti_pin()
                    continue
                else:
                    pass
                break
            while True:
                ganti_pin_alamat = input(" Masukkan Alamat\t\t\t: ")
                if ganti_pin_alamat == "":
                    print("\n Alamat tidak boleh kosong !\n")
                    time.sleep(1.5)
                    clear_biodata_ganti_pin()
                    continue
                else:
                    pass
                break

            while True:
                ganti_pin_email = input(" Masukkan Email anda\t\t\t: ")
                if ganti_pin_email == "":
                    print("\n Email tidak boleh kosong !\n")
                    time.sleep(1.5)
                    clear_biodata_ganti_pin()
                    continue
                elif "@gmail" not in ganti_pin_email :
                    print("\n Format Email yang anda masukkan salah !\n")
                    time.sleep(1.5)
                    clear_biodata_ganti_pin()
                    continue
                else:
                    pass
                break

            while True:
                ganti_pin_no_telp = input(" Masukkan No HP anda(+628 Indonesia)\t: ")
                if validasi_no_hp(ganti_pin_no_telp) == False:
                    print(" Format no HP yang anda masukkan tidak valid !")
                    time.sleep(1.5)
                    clear_biodata_ganti_pin()
                    continue
                
                else: 
                    break

            if ganti_pin_nama.title() == user[ubah_pin]["nama"]:
                if ganti_pin_alamat.title() == user[ubah_pin]["alamat"]:
                    if replace_no_telp == user[ubah_pin]["no_telp"]:
                        if ganti_pin_email == user[ubah_pin]["email"]:
                            print("\n DATA LENGKAP !")
                            time.sleep(1.5)
                            pin_baru(ubah_pin)
                        else:
                            print("\n Data ada yang salah, Mohon di isi dengan benar !")
                    else:
                        print("\n Data ada yang salah, Mohon di isi dengan benar !")
                else:
                    print("\n Data ada yang salah, Mohon di isi dengan benar !")
            else:
                print("\n Data ada yang salah, Mohon di isi dengan benar !")
            input("\n Tekan enter untuk keluar..")
        else:
            lupa_buka_blokir = input("Akun sedang di blokir ! ingin buka blokir ? [y/n]: ")
            if lupa_buka_blokir == "y" :
                buka_blokir(ubah_pin)
                pin_baru(ubah_pin)

            else:
                pass
    else:
        print("\n Nomor ATM tidak ditemukan !")

def pin_baru (ubah_pin:int)->int:
    while True:
        os.system("clear")
        print(f"{'SELAMAT DATANG DI BANK WIBU INDONESIA':^70}")
        print(f'{"MASUKKAN PIN BARU, MOHON PIN UNTUK SELALU DI INGAT ! ".upper():^70}\n\n')
        pin_baru = getpass(" Buat pin(pin harus di ingat)\t\t: ")
        if validasi_pin(pin_baru) == False:
            time.sleep(1.5)
            continue
        else:
            pass
        cek_password = getpass(" Silahkan masukkan ulang pin\t\t: ")
        if cek_password != pin_baru:
            print("\n Pin yang anda masukkan tidak sama !\n Demi keamanan, silahkan buat pin baru !\n")
            time.sleep(1.5)
            continue
        else:
            pass
        break
    user[ubah_pin].update({"pin":str(pin_baru)})
    print(" Pin berhasil di ganti !")
    time.sleep(1.5)

def blokir(blokir_no_atm:int)->int:
    if blokir_no_atm in user:
        user[str(login_no_atm)].update({"akun":"terblokir"})
        print(" Akun anda telah terblokir !")
        apakah_buka_blokir = input("\n Buka blokir ? [y/n]: ").lower()
        if apakah_buka_blokir == "y":
            buka_blokir(blokir_no_atm)
        else:
            pass



def buka_blokir(buka_blokir_no_atm:int)->int:
    global ganti_pin_nama,ganti_pin_alamat,ganti_pin_email,ganti_pin_no_telp,status_login,gagal_login
    while True:
        os.system("clear")
        print(f"{'selamat datang di bank wibu indonesia'.upper():^70}")
        print(f"{'Silahkan isi data dibawah untuk membuka blokir'.upper():^70}\n\n")
        while True:
            ganti_pin_nama = input(" Masukkan Nama anda\t\t\t: ").replace("   "," ").replace("  "," ").lstrip().rstrip()
            if ganti_pin_nama == "":
                print("\n Nama tidak boleh kosong !\n")
                time.sleep(1.5)
                clear_biodata_buka_blokir()
                continue
            else:
                pass
            break
        while True:
            ganti_pin_alamat = input(" Masukkan Alamat\t\t\t: ").lstrip().rstrip()
            if ganti_pin_alamat == "":
                print("\n Alamat tidak boleh kosong !\n")
                time.sleep(1.5)
                clear_biodata_buka_blokir()
                continue
            else:
                pass
            break

        while True:
            ganti_pin_email = input(" Masukkan Email anda\t\t\t: ").strip().rstrip()
            if ganti_pin_email == "":
                print("\n Email tidak boleh kosong !\n")
                time.sleep(1.5)
                clear_biodata_buka_blokir()
                continue
            elif "@gmail" not in ganti_pin_email :
                print("\n Format Email yang anda masukkan salah !\n")
                time.sleep(1.5)
                clear_biodata_buka_blokir()
                continue
            else:
                pass
            break

        while True:
            ganti_pin_no_telp = input(" Masukkan No HP anda(+628 Indonesia)\t: ")
            if validasi_no_hp(ganti_pin_no_telp) == False:
                print(" Format no HP yang anda masukkan tidak valid !")
                time.sleep(1.5)
                clear_biodata_buka_blokir()
                continue
            
            else: 
                break
        if ganti_pin_nama.title() == user[buka_blokir_no_atm]["nama"]:
            if ganti_pin_alamat.title() == user[buka_blokir_no_atm]["alamat"]:
                if replace_no_telp == user[buka_blokir_no_atm]["no_telp"]:
                    if ganti_pin_email == user[buka_blokir_no_atm]["email"]:
                        user[buka_blokir_no_atm].update({"akun":"aktif"})
                        user[str(login_no_atm)]["pin_salah"]=0
                        print("\n Akun anda berhasil dipulihkan !")
                        time.sleep(1.5)
                        break
                    else:
                        print(" Data ada yang salah, Mohon di isi dengan benar !")
                else:
                    print(" Data ada yang salah, Mohon di isi dengan benar !")
            else:
                print(" Data ada yang salah, Mohon di isi dengan benar !")
        else:
            print("\n Data ada yang salah, Mohon di isi dengan benar !")
            time.sleep(1.5)
            apakah_lanjut_buka_blokir = input(" Lanjut proses ? [y/keluar]: ").lower()
            if apakah_lanjut_buka_blokir == "y":
                continue
            else:
                pass
            break
        break



def username():
    global login_no_atm
    temukan = user[str(login_no_atm)]["nama"].find(" ")
    if " " in user[str(login_no_atm)]["nama"]  :
        return f'{user[str(login_no_atm)]["nama"][:temukan]:>{len({user[str(login_no_atm)]["nama"]})}}'.upper()
    else:
        return f'{user[str(login_no_atm)]["nama"]:>{len({user[str(login_no_atm)]["nama"]})}}'.upper()



def daftar():
    global nama,alamat,no_telp,email,angka_pin
    os.system("clear")
    random_angka = [str(x) for x in range(1,11)]
    no_atm = "".join((random.choice(random_angka) for i in range(10)))
    print(f'\n{"PROSES PENDAFTARAN BANK WIBU INDONESIA":^70}\n{"SILAHKAN ISI DATA DIRI ANDA!":^70}\n\n')
    while True:
        nama = input(" Masukkan Nama anda\t\t\t: ").replace("   "," ").replace("  "," ").lstrip().rstrip()
        if nama == "":
            print("\n Nama tidak boleh kosong !\n")
            time.sleep(1.5)
            clear_biodata()
            continue
        else:
            pass
        break

    while True:
        alamat = input(" Masukkan Alamat\t\t\t: ").lstrip().rstrip()
        if alamat == "":
            print("\n Alamat tidak boleh kosong !\n")
            time.sleep(1.5)
            clear_biodata()
            continue
        else:
            pass
        break

    while True:
        email = input(" Masukkan Email anda\t\t\t: ").lstrip().rstrip()
        if email == "":
            print("\n Email tidak boleh kosong !\n")
            time.sleep(1.5)
            clear_biodata()
            continue
        elif "@gmail" not in email :
            print("\n Formatgit remote add origin https://github.com/KRP186zL/Project_ATM.git Email yang anda masukkan salah !\n")
            time.sleep(1.5)
            clear_biodata()
            continue
        else:
            pass
        break

    while True:
        no_telp = input(" Masukkan No HP anda(+628 Indonesia)\t: ")
        if validasi_no_hp(no_telp) == False:
            print(" Format no HP yang anda masukkan tidak valid !")
            time.sleep(1.5)
            clear_biodata()
            continue
        else: 
            break

    while True:
        pin = getpass(" Buat pin(pin harus di ingat)\t\t: ")
        if validasi_pin(pin) == False:
            time.sleep(1.5)
            clear_biodata()
            continue
        else:
            pass
        cek_password = getpass(" Silahkan masukkan ulang pin\t\t: ")
        if cek_password != pin:
            print("\n Pin yang anda masukkan tidak sama !\n Demi keamanan, silahkan buat pin baru !\n")
            time.sleep(1.5)
            clear_biodata()
            continue
        else:
            pass
        break
    tambah_user(no_atm,pin,nama.title(),alamat.title(),replace_no_telp,email,saldo=0,pin_salah=0,akun="aktif",transaksi=[])

    

def validasi_pin(val_pin:int)->int:
    angka_pin = list(string.ascii_letters)
    for i in angka_pin:
        if i in val_pin :
            print("\n Pin harus menggunakan angka !")
            return False
        
        if val_pin == "":
            print("\n Pin tidak boleh kosong !\n")
            return False
        
    return val_pin



def validasi_no_hp(val_no_telp:int)->int:
    global replace_no_telp
    angka_no_hp = list(string.ascii_letters)
    if val_no_telp.startswith("628") or val_no_telp.startswith("+628"):
        for i in angka_no_hp:
            if i in val_no_telp:
                return False
            else:
                replace_no_telp = str(val_no_telp).replace("628","08").replace("+628","08")
                return True
    if val_no_telp == "":
        return False
    
    for j in angka_no_hp:
        if j in angka_no_hp:
            return False



def tambah_user(no_atm:int,pin:int,nama:str,alamat:str,no_telp:int,email:str,saldo:int,pin_salah:int,akun:str,transaksi:list)->any:
    global user
    user.update({
        no_atm:{
        "no_atm":no_atm,
        "pin":pin,
        "nama":nama,
        "alamat":alamat,
        "no_telp":no_telp,
        "email":email,
        "saldo":saldo,
        "pin_salah":pin_salah,
        "akun":akun,
        "transaksi":transaksi
        }
    })
    print("\n\n Registrasi berhasil !")
    print(" Nomor ATM anda adalah:",user[no_atm]["no_atm"])
    print("\n Mohon untuk di ingat karena nomor ATM hanya muncul sekali !".upper())
    input("\n\n Tekan enter..")

def saldo ():
    saldo = user[str(login_no_atm)]["saldo"]
    return f"{saldo:,}"

def cek_saldo():
    panjang_username = 67 - 18
    riwayat_transaksi = [x for x in user[str(login_no_atm)]["transaksi"]]
    if len(riwayat_transaksi) ==0:
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
| {username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Jumlah saldo anda adalah: Rp.'}{saldo()}{'|':>{37-len(saldo())}}
| {'|':>70}
| {'|':>70}
|     {'Transaksi terakhir anda :'}{'|':>41}
| {'|':>70}
|     {"Belum ada riwayat transaksi"}{'|':>39}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input ("\n Tekan enter untuk kembali...")

    if len(riwayat_transaksi) ==1:
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
| {username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Jumlah saldo anda adalah: Rp.'}{saldo()}{'|':>{37-len(saldo())}}
| {'|':>70}
| {'|':>70}
|     {'Transaksi terakhir anda :'}{'|':>41}
| {'|':>70}
|     {riwayat_transaksi[-1]:<65}{'|':>1}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input ("\n Tekan enter untuk kembali...")

    if len(riwayat_transaksi) ==2:
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
| {username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Jumlah saldo anda adalah: Rp.'}{saldo()}{'|':>{37-len(saldo())}}
| {'|':>70}
| {'|':>70}
|     {'Transaksi terakhir anda :'}{'|':>41}
| {'|':>70}
|     {riwayat_transaksi[-1]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-2]:<65}{'|':>1}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input ("\n Tekan enter untuk kembali...")

    if len(riwayat_transaksi) ==3:
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
| {username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Jumlah saldo anda adalah: Rp.'}{saldo()}{'|':>{37-len(saldo())}}
| {'|':>70}
| {'|':>70}
|     {'Transaksi terakhir anda :'}{'|':>41}
| {'|':>70}
|     {riwayat_transaksi[-1]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-2]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-3]:<65}{'|':>1}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input ("\n Tekan enter untuk kembali...")

    if len(riwayat_transaksi) ==4:
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
| {username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Jumlah saldo anda adalah: Rp.'}{saldo()}{'|':>{37-len(saldo())}}
| {'|':>70}
| {'|':>70}
|     {'Transaksi terakhir anda :'}{'|':>41}
| {'|':>70}
|     {riwayat_transaksi[-1]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-2]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-3]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-4]:<65}{'|':>1}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input ("\n Tekan enter untuk kembali...")

    if len(riwayat_transaksi) >=5:
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
| {username():^20} {'|':>{panjang_username}}
| {'|':>70}
| {'|':>70}
|{'selamat datang di bank wibu indonesia'.upper():^70}|
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Jumlah saldo anda adalah: Rp.'}{saldo()}{'|':>{37-len(saldo())}}
| {'|':>70}
| {'|':>70}
|     {'Transaksi terakhir anda :'}{'|':>41}
| {'|':>70}
|     {riwayat_transaksi[-1]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-2]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-3]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-4]:<65}{'|':>1}
| {'|':>70}
|     {riwayat_transaksi[-5]:<65}{'|':>1}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input ("\n Tekan enter untuk kembali...")



def clear_nominal_tf(no_rek_transfer:int)->int:
    os.system("clear")
    print(f"{'selamat datang di bank wibu indonesia'.upper():^70}")
    print(f"{'mohon di cek kembali no atm yang akan di transfer'.upper():^70}\n\n")
    nominal_transfer= []
    if len(str(no_rek_transfer)) >=1:
        nominal_transfer.append(no_rek_transfer)
        print(f" Masukkan nomor ATM yang ingin anda transfer\t\t: {no_rek_transfer}")



def struk_transfer(nominal_tf:int,no_rek_tf:int)->int:
    if len(str(nominal_tf))>=7:
        spasi_nom_tf = 37 - len(str(nominal_tf))
    else:
        spasi_nom_tf = 38 - len(str(nominal_tf))
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
| {'|':>70}
| {'BUKTI TRANSFER BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Pengirim: '.upper()}{user[str(login_no_atm)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Penerima: '.upper()}{user[str(no_rek_tf)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Transfer uang sebesar: '.upper():<23}Rp.{nominal_tf:,} {'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status Transaksi: PROSES':<36}{'|':>30}
| {'|':>70}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
    
    time.sleep(1.5)
    nama_pengirim = user[str(login_no_atm)]["nama"]
    nama_penerima = user[str(no_rek_tf)]["nama"]
    cek_apakah_transfer = input(f"\n Transfer dana sebesar Rp{nominal_tf:,} ke No ATM {no_rek_tf} AN {nama_penerima} ?[y/n]: ")
    if cek_apakah_transfer == "y":
        if user[str(login_no_atm)]["saldo"] >= nominal_tf:
            user[str(login_no_atm)]["saldo"]-=nominal_tf
            user[str(login_no_atm)]["transaksi"].append(f"Mengirim uang Rp.{nominal_tf:,} kepada {nama_penerima}")
            user[str(no_rek_tf)]["saldo"]+= nominal_tf
            user[str(no_rek_tf)]["transaksi"].append(f"Menerima uang Rp.{nominal_tf:,} dari {nama_pengirim} ")
            time.sleep(2.5)
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
| {'|':>70}
| {'BUKTI TRANSFER BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Pengirim: '.upper()}{user[str(login_no_atm)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Penerima: '.upper()}{user[str(no_rek_tf)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Transfer uang sebesar: '.upper():<23}Rp.{nominal_tf:,} {'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status Transaksi: SUKSES':<36}{'|':>30}
| {'|':>70}
|     {'Sisa saldo anda :'.upper()}Rp.{saldo()}{'|':>{46-len(saldo())}}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
            input(" Tekan enter untuk lanjut...")
        else:
            time.sleep(2.5)
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
| {'|':>70}
| {'BUKTI TRANSFER BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Pengirim: '.upper()}{user[str(login_no_atm)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Penerima: '.upper()}{user[str(no_rek_tf)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Transfer uang sebesar: '.upper():<23}Rp.{nominal_tf:,} {'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status Transaksi: GAGAL, Saldo tidak mencukupi'.upper():<65}{'|':>1}
| {'|':>70}
|     {'Sisa saldo anda :'.upper()}Rp.{saldo()}{'|':>{46-len(saldo())}}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
            input(" Tekan enter untuk lanjut...")
    else:
        time.sleep(2.5)
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
| {'|':>70}
| {'BUKTI TRANSFER BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {'Pengirim: '.upper()}{user[str(login_no_atm)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Penerima: '.upper()}{user[str(no_rek_tf)]["nama"].upper():<26}{'|':>30}
| {'|':>70}
|     {'Transfer uang sebesar: '.upper():<23}Rp.{nominal_tf:,} {'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status Transaksi: DIBATALKAN'.upper():<36}{'|':>30}
| {'|':>70}
| {'|':>70}
| {'|':>70}
 {'='*70}""")
        input(" Tekan enter untuk lanjut...")



def transfer():
    while True:
        os.system("clear")
        print(f"{'selamat datang di bank wibu indonesia'.upper():^70}")
        print(f"{'mohon di cek kembali no atm yang akan di transfer'.upper():^70}\n\n")
        try:
            no_rek_transfer = int(input(" Masukkan nomor ATM yang ingin anda transfer\t\t: "))
            break
        except ValueError:
            print("\n Nomor ATM harus menggunakan angka !")
            time.sleep(1.5)
            continue
            
    while True:
        while True:
            try:
                nominal = int(input(" Masukkan Jumlah transfer Rp.50,000 - Rp.100,000,000\t: "))
                break
            except ValueError:
                print("\n Mohon gunakan angka !")
                time.sleep(1.5)
                clear_nominal_tf(no_rek_transfer)
        if str(no_rek_transfer) in user:
            if nominal >= 50000 and nominal <= 100000000 :
                if nominal % 50000 == 0:
                    if str(no_rek_transfer) != str(login_no_atm):
                        struk_transfer(nominal,no_rek_transfer)
                    else:
                        print(" Anda tidak bisa transfer ke no ATM sendiri !")
                        time.sleep(1.5)
                        transfer()
                else:
                    print("\n Hanya berlaku kelipatan Rp.50.000, Rp,100.000, Rp,150.000...")
                    input(" Tekan enter...")
                    clear_nominal_tf(no_rek_transfer)
                    continue
            else:
                print("\n Nominal transfer yang anda masukkan tidak valid,\n Min Rp.50,000 Max Rp.100,000,000")    
                input(" Tekan enter...")
                clear_nominal_tf(no_rek_transfer)
                continue
        else: 
            print("\n No ATM tidak ditemukan !")
            time.sleep(1.5)
            transfer()
        break



def struk_setor_tunai(nominal_setor_tunai:int)->int:
    if len(str(nominal_setor_tunai))>=7:
        spasi_nom_tf = 52 - len(str(nominal_setor_tunai))
    else:
        spasi_nom_tf = 53 - len(str(nominal_setor_tunai))
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
| {'|':>70}
| {'BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {"Deposit ke tabungan".upper():<26}{"|":>40}
|     {"Sebesar:".upper():<8} Rp.{nominal_setor_tunai:,}{'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status : SUKSES'.upper():<26}{'|':>40}
| {'|':>70}
| {'|':>70}
|     {'Saldo anda :'.upper()}Rp.{saldo()}{'|':>{51-len(saldo())}}
| {'|':>70}
| {'|':>70}
| {'|':>70}
| {'BWI ':^69}{'|'}
| {'MELAYANI WIBU, ':^69}{'|'}
| {'KAPAN SAJA ':^69}{'|'}
| {'|':>70}
| {'KUNJUNGI WWW.BWI.CO.ISK ':^69}{'|'}
| {'UNTUK INFORMASI PROMO-PROMO MENARIK ':^69}{'|'}
 {'='*70}""")
    input(" Tekan enter untuk lanjut...")



def setor_tunai():
    while True:
        while True:
            os.system("clear")
            print(f"{'selamat datang di bank wibu indonesia'.upper():^70}")
            print(f"{'Pastikan uang yang anda masukkan tidak terlipat !'.upper():^70}\n\n")
            try:
                nominal_setor = int(input(" Masukkan nominal uang yang ingin di setor: "))
                break
            except ValueError:
                print("\n Mohon gunakan angka !")
                time.sleep(1.5)
                continue
        if nominal_setor >=50000 and nominal_setor <=10000000:
            if nominal_setor % 50000 == 0:
                user[str(login_no_atm)]["saldo"]+=nominal_setor
                user[str(login_no_atm)]["transaksi"].append(f"Deposit ke tabungan sebesar Rp.{nominal_setor:,}")
                struk_setor_tunai(nominal_setor)
            else:
                print("\n Hanya berlaku kelipatan Rp.50.000, Rp,100.000, Rp,150.000...")
                input(" Tekan enter...")
                continue
        else:
            print(" Setor tunai Min Rp.50,000 Max Rp.10,000,000 !")
            input(" Tekan enter...")
            continue
        break



def tarik_tunai():
    #PROSES DILAKUKAN DI BAGIAN STRUCK TARIK TUNAI
    while True:
        while True:
            os.system("clear")
            print(f"{'selamat datang di bank wibu indonesia'.upper():^70}")
            print(f"{'cukup uang saja yang virtual, hubungan jangan !'.upper():^70}\n\n")
            try:
                nominal_tarik = int(input(" Masukkan nominal uang yang ingin di Tarik: "))
                break
            except ValueError:
                print("\n Mohon gunakan angka !")
                time.sleep(1.5)
                continue
        if nominal_tarik >=50000 and nominal_tarik <=10000000:
            if nominal_tarik % 50000 == 0:
                struk_tarik_tunai(nominal_tarik)
            else:
                print("\n Hanya berlaku kelipatan Rp.50.000, Rp,100.000, Rp,150.000...")
                input(" Tekan enter...")
                continue
        else:
            print(" Tarik tunai Min Rp.50,000 Max Rp.10,000,000 !")
            input(" Tekan enter...")
            continue
        break



def struk_tarik_tunai(nom_tarik:int)->int:
    if len(str(nom_tarik))>=7:
        spasi_nom_tf = 52 - len(str(nom_tarik))
    else:
        spasi_nom_tf = 53 - len(str(nom_tarik))
    if user[str(login_no_atm)]["saldo"] >= nom_tarik:
        user[str(login_no_atm)]["saldo"]-=nom_tarik
        user[str(login_no_atm)]["transaksi"].append(f"Penarikan tabungan sebesar Rp.{nom_tarik:,}")
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
| {'|':>70}
| {'BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {"Penarikan tabungan".upper():<26}{"|":>40}
|     {"Sebesar:".upper():<8} Rp.{nom_tarik:,}{'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status : SUKSES'.upper():<26}{'|':>40}
| {'|':>70}
| {'|':>70}
|     {'Saldo anda :'.upper()}Rp.{saldo()}{'|':>{51-len(saldo())}}
| {'|':>70}
| {'|':>70}
| {'|':>70}
| {'BWI ':^69}{'|'}
| {'MELAYANI WIBU, ':^69}{'|'}
| {'KAPAN SAJA ':^69}{'|'}
| {'|':>70}
| {'KUNJUNGI WWW.BWI.CO.ISK ':^69}{'|'}
| {'UNTUK INFORMASI PROMO-PROMO MENARIK ':^69}{'|'}
 {'='*70}""")
        input(" Tekan enter untuk lanjut...")
    else:
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
| {'|':>70}
| {'BANK WIBU INDONESIA ':^69}{'|'}
| {'|':>70}
| {'|':>70}
| {'|':>70}
|     {"Penarikan tabungan".upper():<26}{"|":>40}
|     {"Sebesar:".upper():<8} Rp.{nom_tarik:,}{'|':>{spasi_nom_tf}}
| {'|':>70}
|     {'Status : GAGAL, saldo anda tidak mencukupi'.upper():<50}{'|':>16}
| {'|':>70}
| {'|':>70}
|     {'Saldo :'.upper()}Rp.{saldo()}{'|':>{56-len(saldo())}}
| {'|':>70}
| {'|':>70}
| {'|':>70}
| {'BWI ':^69}{'|'}
| {'MELAYANI WIBU, ':^69}{'|'}
| {'KAPAN SAJA ':^69}{'|'}
| {'|':>70}
| {'KUNJUNGI WWW.BWI.CO.ISK ':^69}{'|'}
| {'UNTUK INFORMASI PROMO-PROMO MENARIK ':^69}{'|'}
 {'='*70}""")
        input(" Tekan enter untuk lanjut...")

