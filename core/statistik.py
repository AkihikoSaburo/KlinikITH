"""
statistik.py
Berisi fungsi dalam hal statistika, maupun menampilkan data.
"""
from collections import Counter

from core import pasien as p
from core import kunjungan

def semua_statistik_pasien():
    """
    Menampilkan semua statistik: NIM, Nama, Prodi, Jumlah Berkunjung, Terakhir Kali Berkunjung
    """
    # Load data dari hashtable kunjungan dan pasien
    data_kunjungan = kunjungan.data_kunjungan
    data_pasien = p.data_pasien
    
    hasil = []
    for nim, kunjungans in data_kunjungan.items():
        jumlah = len(kunjungans)
        tanggal_terakhir = max(k["tanggal"] for k in kunjungans)

        pasien = data_pasien.get(nim) or {}
        nama = pasien.get('nama')
        prodi = pasien.get('prodi')

        hasil.append({
            "nim": nim,
            "nama": nama,
            "prodi": prodi,
            "jumlah": jumlah,
            "terakhir": tanggal_terakhir
        })

    # Mengembalikan dengan nilai yang telah di sortir
    return sorted(hasil, key=lambda x: x["jumlah"], reverse=True)

def statistik_penyakit_terbanyak(top_n=3, return_data=False):
    """
    Menampilkan diagnosa (penyakit) paling sering.
    """
    # Load data dari hashtable kunjungan dan pasien
    data_kunjungan = kunjungan.data_kunjungan
    data_pasien = p.data_pasien
    
    semua_kunjungan = []
    for _, kunjungans in data_kunjungan.items():
        semua_kunjungan.extend(kunjungans)

    diagnosa_list = [k['diagnosa'] for k in semua_kunjungan]
    counter = Counter(diagnosa_list)
    
    if return_data:
        total = sum(counter.values()) or 1  # biar gak error jika kosong
        result = [
            {"nama": penyakit, "jumlah": jumlah, "persen": int((jumlah / total) * 100)}
            for penyakit, jumlah in counter.most_common(top_n)
        ]
        return result
    
    print("=== 3 Penyakit Terbanyak ===")
    for penyakit, jumlah in counter.most_common():
        print(f"{penyakit}: {jumlah} kasus")
        
def semua_statistik_penyakit_terbanyak(return_data=False):
    """
    Menampilkan diagnosa (penyakit) paling sering.
    """
    # Load data dari hashtable kunjungan dan pasien
    data_kunjungan = kunjungan.data_kunjungan
    data_pasien = p.data_pasien
    
    semua_kunjungan = []
    for _, kunjungans in data_kunjungan.items():
        semua_kunjungan.extend(kunjungans)

    diagnosa_list = [k['diagnosa'] for k in semua_kunjungan]
    counter = Counter(diagnosa_list)
    
    if return_data:
        total = sum(counter.values()) or 1  # biar gak error jika kosong
        result = [
            {"nama": penyakit, "jumlah": jumlah, "persen": int((jumlah / total) * 100)}
            for penyakit, jumlah in counter.most_common()
        ]
        return result
    
    print("=== 3 Penyakit Terbanyak ===")
    for penyakit, jumlah in counter.most_common():
        print(f"{penyakit}: {jumlah} kasus")
        

def statistik_pasien_tersering(top_n=3, return_data=False):
    """
    Menampilkan Top 3 pasien yang paling sering ke klinik.
    """
    data_kunjungan = kunjungan.data_kunjungan
    data_pasien = p.data_pasien

    counter = Counter()
    for nim, kunjungans in data_kunjungan.items():
        counter[nim] += len(kunjungans)

    if return_data:
        result = []
        for nim, jumlah in counter.most_common(top_n):
            kunjungans = data_kunjungan.get(nim) or {}
            tanggal_terakhir = max(k["tanggal"] for k in kunjungans) if kunjungans else "-"
            pasien = data_pasien.get(nim) or {}
            nama = pasien.get('nama', 'Tidak diketahui')
            prodi = pasien.get('prodi', 'Tidak diketahui')

            result.append({
                "nim": nim,
                "nama": nama,
                "prodi": prodi,
                "jumlah": jumlah,
                "terakhir": tanggal_terakhir
            })
        return result

