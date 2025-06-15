"""
penyakit.py

Berisi route utama (penyakitpage) untuk KlinikITH.
Menampilkan halaman dashboard awal yang berisi penyakit yang dialami mahasiswa dengan urutan paling banyak.
"""
from flask import Blueprint, render_template

from core import statistik

penyakit_bp = Blueprint("penyakit", __name__)

@penyakit_bp.route("/penyakit")
def penyakit():
    # Ambil data statistik penyakit
    data_penyakit = statistik.semua_statistik_penyakit_terbanyak(return_data=True)
    
    return render_template("penyakit.html", penyakit=data_penyakit)