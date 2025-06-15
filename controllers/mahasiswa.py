"""
mahasiswa.py

Menampilkan daftar mahasiswa yang pernah melakukan kunjungan ke klinik, beserta jumlah kunjungannya. Termasuk pencarian dan redirect ke riwayat.
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash

from struktur_data.hash_table import HashTable
from core import kunjungan, statistik

mahasiswa_bp = Blueprint("statistik", __name__)

@mahasiswa_bp.route("/mahasiswa")
def mahasiswa():
    query = request.args.get("q", "").lower()
    data = statistik.semua_statistik_pasien()

    if query:
        if kunjungan.data_kunjungan.exists(query):
            return redirect(url_for("riwayat.lihat_riwayat", nim=query))
        
        flash(f"NIM {query} tidak ditemukan dalam data kunjungan.", "error")
        return redirect(url_for("statistik.mahasiswa"))
    
    return render_template("mahasiswa.html", mahasiswa=data, query=query)
