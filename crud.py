import re


class dataMahasiswa:
    def __init__(self, nama, nim, prodi):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi

    def get_nama(self):
        return self.nama

    def get_nim(self):
        return self.nim

    def get_prodi(self):
        return self.prodi


def display():
    for i in mahasiswa:
        print("-------------------------")
        print("Nama  : ", i.nama)
        print("Nim   : ", i.nim)
        print("Prodi : ", i.prodi, "\n")


def edit(nama):
    for i in mahasiswa:
        if i.nama == nama:
            print("-------------------------")
            print("Ubah data ", i.nama)
            print("1. Nama")
            print("2. Nim")
            print("3. Prodi")
            print("0. Kembali")

            pilihedit = float(input("Pilih Edit : "))
            if pilihedit == 1:
                ubahdata = input("Masukkan Data Baru : ")
                i.nama = ubahdata
            elif pilihedit == 2:
                ubahnim = input("Masukkan Data Baru : ")
                i.nim = int(ubahnim)
            elif pilihedit == 3:
                ubahprodi = input("Masukkan Data Baru : ")
                i.prodi = ubahprodi
            else:
                break


def delete(nama):
    for i in mahasiswa:
        if i.nama == nama:
            mahasiswa.remove(i)


def search(nama):
    for i in mahasiswa:
        if i.nama == nama:
            print("-------------------------")
            print("Nama  : ", i.nama)
            print("Nim   : ", i.nim)
            print("Prodi : ", i.prodi, "\n")


def sortdata(key):
    if key == 1:
        mahasiswa.sort(key=dataMahasiswa.get_nama)
    elif key == 2:
        mahasiswa.sort(key=dataMahasiswa.get_nim)
    elif key == 3:
        mahasiswa.sort(key=dataMahasiswa.get_prodi)
    elif key == 0:
        print("\n")
    else:
        print("Pilihan Tidak Tersedia\n")


mahasiswa = []
mahasiswa.append(dataMahasiswa("Abraham Samuel R",
                 1202200089, "Teknologi Informasi"))
pilih = 1
while pilih != 0:
    print("Menu")
    print("1. Tambah data baru")
    print("2. Hapus data")
    print("3. Ubah data")
    print("4. Tampilkan data")
    print("5. Cari data")
    print("6. Urut berdasarkan")
    pilih = float(input("Pilih Menu "))
    if pilih == 1:
        print("tambah data baru")
        addnama = input("Masukkan Nama : ")
        addnim = int(input("Masukkan Nim : "))
        addprodi = input("Masukkan Prodi : ")
        mahasiswa.append(dataMahasiswa(addnama, addnim, addprodi))
        print("Data Mahasiswa Ditambahkan")
    elif pilih == 2:
        print("Data Mahasiswa")
        hapus = input("Masukkan Nama yang ingin di hapus : ")
        delete(hapus)

    elif pilih == 3:
        print("Ubah Data")
        ubah = input("Masukkan Nama yang ingin di ubah : ")
        edit(ubah)
    elif pilih == 4:
        display()
    elif pilih == 5:
        print("Cari Data")
        ubah = input("Masukkan Nama yang ingin di cari : ")
        search(ubah)
    elif pilih == 6:
        print("Urutkan Data")
        print("1. Nama")
        print("2. Nim")
        print("3. Prodi")
        print("0. Batal")
        urut = int(input("Urutkan berdasatkan : "))
        sortdata(urut)
    else:
        break
