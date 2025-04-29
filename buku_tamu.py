import streamlit as st
import pandas as pd
import os
from datetime import datetime
import time

# Konfigurasi
st.set_page_config(page_title="Buku Tamu - Stasiun Geofisika Nganjuk")

# Fungsi format tanggal
def format_tanggal(dt):
    bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", 
             "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
    return f"{dt.day}-{bulan[dt.month-1]}-{dt.year} {dt.strftime('%I:%M %p')}"

# UI
st.title("📝 Buku Tamu")
st.subheader("Stasiun Geofisika Nganjuk")

with st.form("guest_form"):
    nama = st.text_input("Nama*")
    instansi = st.text_input("Instansi*")
    tanggal = st.date_input("Tanggal Kunjungan*")
    waktu = st.time_input("Waktu Kunjungan*")
    keperluan = st.text_area("Keperluan*")
    foto = st.file_uploader("Foto*", type=["jpg", "png", "jpeg"])
    
    if st.form_submit_button("Submit"):
        if not all([nama, instansi, keperluan, foto]):
            st.error("Harap isi semua field wajib (*)")
        else:
            # Gabung tanggal dan waktu
            dt = datetime.combine(tanggal, waktu)
            
            # Simpan data ke dictionary
            data = {
                "Nama": nama,
                "Instansi": instansi,
                "Tanggal": format_tanggal(dt),
                "Keperluan": keperluan,
                "Foto": foto.name if foto else ""
            }
            
            # Simpan ke CSV (simulasi)
            st.success(f"Data {nama} berhasil disimpan! (Simulasi)")
            st.json(data)  # Hanya untuk demo di GitHub
