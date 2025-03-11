import duckdb
import json

# Fungsi untuk membaca kredensial dari file JSON
def read_config(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config

# Membaca kredensial dari file config.json
config = read_config('config.json')

# Ambil kredensial
host = config.get('host')
database = config.get('database')
username = config.get('username')
password = config.get('password')

# Menyusun string koneksi untuk DuckDB
# DuckDB tidak memerlukan username dan password jika menggunakan database lokal
connection_str = f'postgresql://{username}:{password}@{host}/{database}'

# Menghubungkan ke DuckDB
try:
    conn = duckdb.connect(database=':memory:')  # Untuk DuckDB, bisa menggunakan database di memory atau file lokal
    print(f"Berhasil terhubung ke PosgreSQL dengan database {connection_str} menggunakan DuckDB!")

    # Contoh query: Tampilkan versi DuckDB
    result = conn.execute('SELECT version();').fetchall() # Jika menggunakan PosgreSQL sebagai database
    print(result)

    # Menutup koneksi setelah selesai
    conn.close()

except Exception as e:
    print(f"Gagal terhubung ke database: {e}")
