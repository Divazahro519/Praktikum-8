class DaftarNilaiMahasiswa:
    def __init__(self):
        """Constructor untuk menginisialisasi list mahasiswa"""
        self.mahasiswa = []

    def tambah(self, nama, nilai):
        """
        Menambahkan data mahasiswa baru.

        :param nama: Nama mahasiswa
        :param nilai: Nilai mahasiswa
        """
        data_mahasiswa = {'nama': nama, 'nilai': nilai}
        self.mahasiswa.append(data_mahasiswa)
        print(f"Data mahasiswa {nama} berhasil ditambahkan.\n")

    def tampilkan(self):
        """
        Menampilkan daftar semua mahasiswa dan nilainya.
        Jika tidak ada data mahasiswa, menampilkan pesan bahwa data kosong.
        """
        if not self.mahasiswa:
            print("Tidak ada data mahasiswa.\n")
        else:
            print("Daftar Nilai Mahasiswa:")
            for mhs in self.mahasiswa:
                print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
            print()  # Memberikan baris kosong setelah daftar

    def hapus(self, nama):
        """
        Menghapus data mahasiswa berdasarkan nama.

        :param nama: Nama mahasiswa yang ingin dihapus
        """
        for mhs in self.mahasiswa:
            if mhs['nama'] == nama:
                self.mahasiswa.remove(mhs)
                print(f"Data mahasiswa dengan nama {nama} berhasil dihapus.\n")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.\n")

    def ubah(self, nama, nilai_baru):
        """
        Mengubah data nilai mahasiswa berdasarkan nama.

        :param nama: Nama mahasiswa yang nilainya ingin diubah
        :param nilai_baru: Nilai baru yang akan diberikan
        """
        for mhs in self.mahasiswa:
            if mhs['nama'] == nama:
                mhs['nilai'] = nilai_baru
                print(f"Nilai mahasiswa {nama} berhasil diubah menjadi {nilai_baru}.\n")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.\n")


# Contoh penggunaan class DaftarNilaiMahasiswa

# Membuat objek daftar_nilai dari class DaftarNilaiMahasiswa
daftar_nilai = DaftarNilaiMahasiswa()

# Menambahkan data mahasiswa
daftar_nilai.tambah("Diva", 90)
daftar_nilai.tambah("Leni", 85)
daftar_nilai.tambah("Bagus", 88)

# Menampilkan daftar nilai mahasiswa
daftar_nilai.tampilkan()

# Mengubah nilai mahasiswa Budi
daftar_nilai.ubah("Diva", 95)

# Menampilkan daftar nilai mahasiswa setelah diubah
daftar_nilai.tampilkan()

# Menghapus data mahasiswa Leni
daftar_nilai.hapus("Leni")

# Menampilkan daftar nilai mahasiswa setelah dihapus
daftar_nilai.tampilkan()
