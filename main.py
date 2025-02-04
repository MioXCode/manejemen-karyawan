import csv
import os

csvFile = r"/home/tomio/Documents/Project/manejemen-karyawan/csv/data_karyawan.csv"


def init_csv():
    if not os.path.exists(csvFile):
        with open(csvFile, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nama", "Jabatan", "Gaji"])


def add_karyawan(id, nama, jabatan, gaji):
    with open(csvFile, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, nama, jabatan, gaji])
    print("Berhasil Add Data Karyawan Baru :)")


def del_karyawan(id):
    rows = []

    with open(csvFile, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(csvFile, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])

        found = False
        for row in rows[1:]:
            if row[0] != id:
                writer.writerow(row)
            else:
                found = True

        if found:
            print(f"Data karyawan dengan ID: {id} berhasil dihapus :)")
        else:
            print(f"Data karyawan dengan ID: {id} tidak ditemukan :(")


def upd_karyawan(id, nama=None, jabatan=None, gaji=None):
    rows = []
    updated = False

    with open(csvFile, mode="r", newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(csvFile, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])

        for row in rows[1:]:
            if row[0] == id:
                if nama:
                    row[1] = nama
                if jabatan:
                    row[2] = jabatan
                if gaji:
                    row[3] = gaji

                updated = True
            writer.writerow(row)

    if updated:
        print(f"Data karyawan dengan ID: {id} berhasil diperbarui :)")
    else:
        print(f"Data karyawan dengan ID: {id} tidak ditemukan :(")


def read_karyawan():
    with open(csvFile, mode="r", newline="") as file:
        reader = csv.reader(file)

        for row in reader:
            print(f"ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}")


def read_karyawan_by_id(id):
    show_id = False

    with open(csvFile, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            if row[0] == id:
                show_id = True
                print(
                    f"ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}"
                )
                break

        if not show_id:
            print(f"Tidak dapat menemukan karyawan dengan ID: {id}")


def menu():
    while True:
        print("=" * 50)
        print("1. Add Karyawan")
        print("2. Del Karyawan")
        print("3. Upd Karyawan")
        print("4. Read Karyawan")
        print("5. Read Karyawan By ID")
        print("6. Exit")
        print("=" * 50)

        try:
            inputUser = int(input("Masukan Angka Di Menu [1 - 6]: "))
        except ValueError:
            print("Masukan angka yang valid!")
            continue

        if inputUser == 1:
            id = input("ID: ")
            nama = input("Nama: ")
            jabatan = input("Jabatan: ")
            gaji = input("Gaji: ")
            add_karyawan(id, nama, jabatan, gaji)
        elif inputUser == 2:
            id = input("Masukan ID karyawan yg mau dihapus: ")
            del_karyawan(id)
        elif inputUser == 3:
            id = input("Masukan ID karyawan yg akan di perbarui: ")
            nama = input("Masukan Nama baru ( Kosongkan Jika Tidak Perlu! ): ")
            jabatan = input("Masukan Jabatan baru ( Kosongkan Jika Tidak Perlu! ): ")
            gaji = input("Masukan Gaji baru ( Kosongkan Jika Tidak Perlu! ): ")
            upd_karyawan(
                id,
                nama if nama else None,
                jabatan if jabatan else None,
                gaji if gaji else None,
            )
        elif inputUser == 4:
            read_karyawan()
        elif inputUser == 5:
            id = input("Masukan data karyawana yg ingin dicari: ")
            read_karyawan_by_id(id)
        elif inputUser == 6:
            print("Keluar dari program.")
            break


if __name__ == "__main__":
    init_csv()
    menu()
