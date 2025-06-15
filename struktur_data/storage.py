"""
Utilitas untuk memuat data dari json ke dalam hashtable dan menyimpan data dari hashtable ke json dengan format dict
"""
import json
import os

from struktur_data.hash_table import HashTable
from struktur_data.merge_sort import merge_sort_dict_items

def load_json_as_hashtable(filepath):
    """
    Load file JSON dan konversi ke HashTable.
    Kalau file tidak ada, buat file baru dengan dict kosong.
    """
    hashtable = HashTable()

   # Jika filenya ada, maka ambil data dari file json, kemudian masukkan ke HashTable 
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            try:
                raw_data = json.load(file)
                if isinstance(raw_data, dict):
                    for key, value in raw_data.items():
                        hashtable.set(key, value)
                    print(f"[✓] Data dari {filepath} berhasil dimuat ke HashTable.")
                else:
                    print(f"[!] Format JSON tidak sesuai. Menggunakan HashTable kosong.")
            except json.JSONDecodeError:
                print(f"[!] Format JSON rusak. Gunakan HashTable kosong.")
    else:
        print(f"[!] File {filepath} tidak ditemukan. Membuat file baru...")
        save_hashtable_as_json(filepath, hashtable)

    return hashtable

def save_hashtable_as_json(filepath, hashtable_data):
    items = list(hashtable_data.items())
    sorted_items = merge_sort_dict_items(items)
    sorted_dict = dict(sorted_items)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(sorted_dict, f, ensure_ascii=False, indent=4)
