"""
pasien.py
Berisi fungsi fungsi mengatur alur penambahan pasien dan mencari data pasien berdasarkan format NIM
"""
from datetime import datetime

from struktur_data.hash_table import HashTable
from core import kunjungan

# Inisialisasi global (bisa juga di-return ke main.py nanti)
data_pasien = HashTable()

# Validasi input pasien
def valid_nim(nim):
    """
    Mengecek apakah NIM sudah benar atau belum, dengan panjang lebih besar dari 5
    """
    return nim.isdigit() and len(nim) >= 5

# Validasi tanggal
def valid_tanggal(tanggal_str):
    """
    Mengecek apakah tanggal yang dimasukkan sudah benar atau belum
    """
    try:
        datetime.strptime(tanggal_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def tambah_pasien(nim, nama, tgl_lahir, prodi):
    """
    Menambahkan pasien baru ke HashTable jika valid dan belum ada.
    """
    if not valid_nim(nim):
        print("[!] NIM tidak valid. Minimal 5 digit angka.")
        return False
    if not valid_tanggal(tgl_lahir):
        print("[!] Format tanggal salah. Gunakan YYYY-MM-DD.")
        return False
    if data_pasien.exists(nim):
        print("[!] Pasien dengan NIM ini sudah terdaftar.")
        return False

    pasien = {
        "nama": nama,
        "tgl_lahir": tgl_lahir,
        "prodi": prodi
    }
    data_pasien.set(nim, pasien)
    print(f"[✓] Pasien '{nama}' berhasil ditambahkan.")
    return True

def cari_pasien(nim):
    """
    Mencari dan mengembalikan data pasien berdasarkan NIM.
    """
    if not valid_nim(nim):
        print("[!] NIM tidak valid.")
        return None

    pasien = data_pasien.get(nim)
    if pasien:
        return pasien
    else:
        print("[!] Pasien tidak ditemukan.")
        return None