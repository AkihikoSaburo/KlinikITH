"""
riwayat.py

Berisi route untuk riwayat pasien
Menampilkan keterangan: Tgl, Gejala, Diagnosa, Obat
"""
from flask import Blueprint, render_template

from core import pasien as p
from core import kunjungan

riwayat_bp = Blueprint("riwayat", __name__, url_prefix="/riwayat")

@riwayat_bp.route("/<nim>")
def lihat_riwayat(nim):
    pasien = p.data_pasien.get(nim)
    data = kunjungan.data_kunjungan.get(nim)
    riwayat = sorted(data, key=lambda x: x["tanggal"], reverse=True)

    if pasien is None:
        pasien = {"nama": "Tidak diketahui", "prodi": "Tidak diketahui"}

    return render_template("riwayat.html", nim=nim, pasien=pasien, riwayat=riwayat)
