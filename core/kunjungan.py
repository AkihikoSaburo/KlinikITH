"""
kunjungan.py
Berisi fungsi fungsi logic untuk penambahan pasien ke dalam hashtable
"""
from collections import Counter
from datetime import datetime

from struktur_data.hash_table import HashTable

# Hash table untuk menyimpan daftar kunjungan per NIM
data_kunjungan = HashTable()

def valid_tanggal(tanggal_str):
    """
    Memastikan data tanggal yang dimasukkan valid sesuai dengan format Tahun-Bulan-Hari or Years-Month-Day
    
    :param tanggal_str: Tanggal Dalam Bentuk String Contoh: 2025-05-15
    """
    try:
        datetime.strptime(tanggal_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def tambah_kunjungan(nim, tanggal, gejala, diagnosa, obat):
    """
    Menambahkan kunjungan ke daftar berdasarkan NIM.
    """
    if not valid_tanggal(tanggal):
        print("[!] Format tanggal salah. Gunakan YYYY-MM-DD.")
        return False

    kunjungan = {
        "tanggal": tanggal,
        "gejala": gejala,
        "diagnosa": diagnosa,
        "obat": obat
    }

    if data_kunjungan.exists(nim):
        data_kunjungan.get(nim).append(kunjungan)
    else:
        data_kunjungan.set(nim, [kunjungan])

    print(f"[✓] Kunjungan untuk NIM {nim} berhasil ditambahkan.")
    return True

def cari_kunjungan(nim):
    """
    Menampilkan semua kunjungan milik NIM tertentu.
    """
    if not data_kunjungan.exists(nim):
        print("[!] Belum ada kunjungan untuk NIM ini.")
        return []

    kunjungan_list = data_kunjungan.get(nim)
    print(f"=== Riwayat Kunjungan NIM {nim} ===")
    for k in kunjungan_list:
        print(f"Tanggal : {k['tanggal']}")
        print(f"Gejala  : {k['gejala']}")
        print(f"Diagnosa: {k['diagnosa']}")
        print(f"Obat    : {k['obat']}")
        print("-" * 30)
    return kunjungan_list