import streamlit as st
import os
import toml

# Fungsi untuk membaca konfigurasi
def read_config():
    config = {}
    
    # Coba membaca dari file config.toml jika ada
    if os.path.exists('config.toml'):
        config = toml.load('config.toml')['database']
    elif st.secrets:
        # Jika tidak ada file config.toml, gunakan secrets Streamlit jika tersedia
        config = {
            'host': st.secrets["host"],
            'port': st.secrets["port"],
            'user': st.secrets["user"],
            'password': st.secrets["password"],
            'database': st.secrets["database"]
        }
    
    return config
