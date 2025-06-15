"""
home.py

Berisi route utama (homepage) untuk KlinikITH.
Menampilkan halaman dashboard awal yang berisi penyakit yang dialami mahasiswa dengan urutan paling banyak.
"""
from flask import Blueprint, render_template

from core import statistik

home_bp = Blueprint("home", __name__)

@home_bp.route("/")
def home():
    # Ambil data statistik penyakit
    data_penyakit = statistik.statistik_penyakit_terbanyak(return_data=True)
    
    data_mahasiswa = statistik.statistik_pasien_tersering(return_data=True)
    
    return render_template("home.html", penyakit=data_penyakit, mahasiswa=data_mahasiswa)