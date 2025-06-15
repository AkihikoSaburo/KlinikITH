"""
input_mahasiswa.py

Berisi route untuk input kunjungan mahasiswa.
Jika NIM belum pernah tercatat, pasien baru otomatis ditambahkan.
"""
from flask import Blueprint, render_template, request, redirect, flash

from core import pasien, kunjungan
from struktur_data.storage import save_hashtable_as_json

input_mahasiswa_bp = Blueprint("input", __name__, url_prefix="/input")

@input_mahasiswa_bp.route("/", methods=["GET", "POST"])
def input_mahasiswa():
    if request.method == "POST":
        nim = request.form["nim"]
        nama = request.form["nama"]
        tgl_lahir = request.form["tgl_lahir"]
        prodi = request.form["prodi"]

        tanggal = request.form["tanggal"]
        gejala = request.form["gejala"]
        diagnosa = request.form["diagnosa"]
        obat = request.form["obat"]

        # Cek dan tambahkan pasien jika belum ada
        if not pasien.data_pasien.exists(nim):
            pasien.tambah_pasien(nim, nama, tgl_lahir, prodi)

        # Tambahkan kunjungan
        kunjungan.tambah_kunjungan(nim, tanggal, gejala, diagnosa, obat)
        save_hashtable_as_json("pasien.json", pasien.data_pasien)
        save_hashtable_as_json("kunjungan.json", kunjungan.data_kunjungan)
        flash("Kunjungan berhasil disimpan.", "success")
        return redirect("/input")

    return render_template("input.html")
