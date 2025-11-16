def tambah_barang():
    print("\n===== TAMBAH BARANG =====")
    nama    = input("Masukkan nama barang              : ")
    kode    = input("Masukkan kode barang              : ")
    jumlah  = int(input("Masukkan jumlah barang            : "))
    expired = input("Masukkan tanggal expired          : ")

    print("\nKondisi barang: rusak/ penyok/ kemasan terbuka/ bau/ berubah warna")
    kondisi = input("Masukkan kondisi barang           : ").lower()

    # Cek kondisi barang
    if kondisi in ["rusak", "penyok", "kemasan terbuka", "bau", "berubah warna"]:
        kategori = "Reject"
        print("Barang Reject")
    else:
        kategori = "Gudang Umum"
        print("Barang masuk ke gudang umum")

    # Tambahkan ke daftar barang
    barang = {
        "nama": nama,
        "kode": kode,
        "jumlah": jumlah,
        "expired": expired,
        "kondisi": kondisi,
        "kategori": kategori
    }
    daftar_barang.append(barang)

    # Tambahkan ke data stok
    data_stok.append(barang.copy())

    print("Barang berhasil ditambahkan!\n")
