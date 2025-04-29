import streamlit as st
import pandas as pd
import os
from datetime import datetime
import cv2
from PIL import Image
import time

# Konfigurasi folder
os.makedirs("photos", exist_ok=True)

# Fungsi format tanggal
def format_tanggal():
    bulan = ["Jan", "Feb", "Mar", "Apr", "Mei", "Jun", 
             "Jul", "Agu", "Sep", "Okt", "Nov", "Des"]
    now = datetime.now()
    return f"{now.day}-{bulan[now.month-1]}-{now.year} {now.strftime('%I:%M %p')}"

# Tampilan UI
st.title("📸 Buku Tamu Digital")
st.subheader("Stasiun Geofisika Nganjuk")

# Form input
with st.form("guest_form"):
    nama = st.text_input("Nama Lengkap*", placeholder="Nama anda")
    instansi = st.text_input("Instansi*", placeholder="Asal instansi/organisasi")
    keperluan = st.text_area("Keperluan*", placeholder="Tujuan kunjungan")
    
    # Widget kamera
    st.write("Ambil Foto*")
    img_file_buffer = st.camera_input("", label_visibility="collapsed")
    
    submitted = st.form_submit_button("Submit Data")
    
    if submitted:
        if not all([nama, instansi, keperluan, img_file_buffer]):
            st.error("Harap isi semua field yang wajib diisi (*)")
        else:
            try:
                # Simpan foto
                timestamp = int(time.time())
                foto_path = f"photos/{timestamp}_{nama.replace(' ', '_')}.jpg"
                
                # Konversi dari buffer ke image
                image = Image.open(img_file_buffer)
                image.save(foto_path)
                
                # Simpan data ke CSV
                data_baru = {
                    "Nama": nama,
                    "Instansi": instansi,
                    "Tanggal": format_tanggal(),
                    "Keperluan": keperluan,
                    "Foto": foto_path
                }
                
                df = pd.DataFrame([data_baru])
                
                if os.path.exists("buku_tamu.csv"):
                    df.to_csv("buku_tamu.csv", mode='a', header=False, index=False)
                else:
                    df.to_csv("buku_tamu.csv", index=False)
                
                st.success("Data berhasil disimpan!")
                st.balloons()
                
            except Exception as e:
                st.error(f"Terjadi error: {str(e)}")

# Tampilkan data yang tersimpan (opsional)
