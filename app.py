"""
app.py

Berfungsi sebagai main program, menjalankan flask(web framework).
Serta meload data dari json, dengan menggunakan fungsi dari storage.
"""
from flask import Flask

from struktur_data.storage import load_json_as_hashtable
from controllers.riwayat import riwayat_bp
from controllers.home import home_bp
from controllers.mahasiswa import mahasiswa_bp
from controllers.input_mahasiswa import input_mahasiswa_bp
from controllers.penyakit import penyakit_bp

from core import pasien, kunjungan

app = Flask(__name__)
app.secret_key = "klinikith2025"

# Mendaftarkan blueprint dari controllers yang telah dibuat
app.register_blueprint(home_bp)
app.register_blueprint(mahasiswa_bp)
app.register_blueprint(input_mahasiswa_bp)
app.register_blueprint(riwayat_bp)
app.register_blueprint(penyakit_bp)

# Load data dari json ke dalam hashtable
pasien.data_pasien = load_json_as_hashtable("pasien.json")
kunjungan.data_kunjungan = load_json_as_hashtable("kunjungan.json")

if __name__ == "__main__":
    app.run(debug=True)
