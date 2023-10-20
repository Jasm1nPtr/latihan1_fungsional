#KEGIATAN 3

def hitung_nilai_akhir(uts,uas):
  return (uts + uas)/2

def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

def tampilkan_nilai_akhir(data_nilai_akhir):
  print ("hasil Nilai Akhir Mahasiwa")
  for nama, nilai_akhir in data_nilai_akhir.items():
    print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

if __name__ == "__main__":
    data_mahasiswa = {
        'Mahasiswa1': {'uts': 82, 'uas': 85},
        'Mahasiswa2': {'uts': 87, 'uas': 90},
        'Mahasiswa3': {'uts': 90, 'uas': 85},
    }
    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)
    tampilkan_nilai_akhir(data_nilai_akhir)