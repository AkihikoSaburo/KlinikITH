"""
hash_table.py
Berisi fungsi menajemen struktur data hashtable
"""
class HashTable:
    def __init__(self, size=8):
        # Ukuran awal tabel hash
        self.size = size
        # Jumlah elemen yang saat ini disimpan dalam tabel
        self.count = 0
        # Inisialisasi tabel hash sebagai list of lists (bucket)
        self.table = [[] for _ in range(size)]
        # Load factor threshold, variabel untuk memicu rehash (resize tabel)
        self.load_factor_threshold = 0.75
    
    def _hash(self, key):
        # Fungsi hash sederhana: menggunakan built-in hash dan modulo dengan ukuran tabel
        return hash(key) % self.size

    def _rehash(self):
        # Menyimpan semua item lama sebelum resize
        old_items = self.items()
        # Menggandakan ukuran tabel
        self.size *= 2
        # Membuat tabel baru dengan ukuran baru
        self.table = [[] for _ in range(self.size)]
        # Mereset jumlah elemen
        self.count = 0

        # Menambahkan ulang semua item ke tabel baru
        for key, value in old_items:
            self.set(key, value)

    def set(self, key, value):
        # Cek apakah perlu melakukan rehash berdasarkan load factor
        if self.count / self.size > self.load_factor_threshold:
            self._rehash()

        # Hitung index untuk kunci menggunakan fungsi hash
        index = self._hash(key)
        bucket = self.table[index]

        # Periksa apakah key sudah ada di bucket; jika ya, update nilainya
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # Jika key belum ada, tambahkan pasangan key-value baru ke bucket
        bucket.append((key, value))
        self.count += 1

    def get(self, key):
        # Mengambil index bucket berdasarkan key
        index = self._hash(key)
        # Iterasi untuk mencari key pada bucket
        for k, v in self.table[index]:
            if k == key:
                return v
        # Kembalikan None jika key tidak ditemukan
        return None

    def exists(self, key):
        # Mengembalikan True jika key ada, False jika tidak
        return self.get(key) is not None

    def delete(self, key):
        # Menghapus item berdasarkan key
        index = self._hash(key)
        bucket = self.table[index]

        # Iterasi untuk mencari dan menghapus pasangan key-value
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        # Kembalikan False jika key tidak ditemukan
        return False

    def keys(self):
        # Mengembalikan daftar semua key dalam tabel
        return [k for bucket in self.table for k, _ in bucket]

    def items(self):
        # Mengembalikan daftar semua pasangan key-value dalam tabel
        return [(k, v) for bucket in self.table for k, v in bucket]

    def __len__(self):
        # Mengembalikan jumlah elemen dalam tabel
        return self.count
