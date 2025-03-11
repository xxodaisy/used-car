#import library

import duckdb
import os
from dotenv import load_dotenv
#membaca kredensial dari env
load_dotenv()

# Ambil kredensial
host = os.getenv('POSTGRES_HOST')
database = os.getenv('POSTGRES_DB')
username = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
schema = os.getenv('POSTGRES_SCHEMA')
port = os.getenv('POSTGRES_PORT')

# Menyusun string koneksi untuk DuckDB
# DuckDB tidak memerlukan username dan password jika menggunakan database lokal
connection_str = f'postgresql://{username}:{password}@{host}/{database}'
print(connection_str)
arr_buyer_id = []
arr_ad_id = []

# Menghubungkan ke DuckDB
try:
    print("set up postgre")
    conn = duckdb.connect(database=':memory:')  # Untuk DuckDB, bisa menggunakan database di memory atau file lokal
    conn.execute('INSTALL postgres;')
    conn.execute('LOAD postgres;')
    conn.execute(f'ATTACH \'host={host} port={port} dbname={database} user={username} password={password}\' as db (TYPE postgres);')

    print(f"Berhasil terhubung ke PosgreSQL dengan database {connection_str} menggunakan DuckDB!")

    # Contoh query: Tampilkan versi DuckDB
    result = conn.execute('SELECT version();').fetchall() # Jika menggunakan PosgreSQL sebagai database
    # SELECT datname FROM pg_database;
    print(result)

 #ambil buyer_id
    query = f"select buyer_id from db.{schema}.buyers;"

    # Menampilkan hasil
    arr_buyer_id = [row[0] for row in conn.execute(query).fetchall()]  # Mengambil buyer_id
    print(arr_buyer_id)

    #ambil ad_id
    query = f"select ad_id from db.{schema}.ads"

    # Menampilkan hasil
    arr_ad_id = [row[0] for row in conn.execute(query).fetchall()]  # Mengambil add_id
    print(arr_ad_id)


    # Menutup koneksi setelah selesai
    conn.close()

except Exception as e:
    print(f"Gagal terhubung ke database: {e}")
    exit(1)


#import library
import pandas as pd
from faker import Faker
import random

#membuat variable untuk generator-variable sbg fungsi Faker
fake = Faker()
#membuat instance Faker dengan lokal Indonesia
fake = Faker('id_ID')

#jumlah data yg dibutuhkan
n_bids = 300

# Contoh data bids
bids = {
    'bid_id': [fake.uuid4() for _ in range(n_bids)],
    'ad_id': [random.choice(arr_ad_id) for _ in range(n_bids)],
    'buyer_id': [random.choice(arr_buyer_id) for _ in range(n_bids)],#arr_buyer_id
    'bid_amount': [round(random.randint(90_000_000, 450_000_000), 2) for _ in range(n_bids)],
    'bid_date': [fake.date_time_this_year() for _ in range(n_bids)],
    'status_bid': [random.choice(['Pending', 'Accepted', 'Rejected']) for _ in range(n_bids)],
    'interaction_type': [random.choice(['View', 'Bid', 'Contract']) for _ in range(n_bids)],
    'bid_detail': []
}

# Mengisi bid_detail berdasarkan status bid
for i in range(n_bids):
    buyer = fake.name()
    bid_amount = bids['bid_amount'][i]
    status_bid = bids['status_bid'][i]

    if status_bid == 'Pending':
        detail = f"Pembeli {buyer} menawarkan Rp {bid_amount:,.2f}. Penawaran sedang diproses."
    elif status_bid == 'Accepted':
        detail = f"Pembeli {buyer} menawarkan Rp {bid_amount:,.2f}. Penawaran diterima."
    elif status_bid == 'Rejected':
        detail = f"Pembeli {buyer} menawarkan Rp {bid_amount:,.2f}. Penawaran ditolak."

    bids['bid_detail'].append(detail)

# Membuat dataframe
df_bids = pd.DataFrame(bids)

# Menyimpan ke CSV
df_bids.to_csv('bids.csv', index=False)

print("Data telah diekspor ke bids.csv")