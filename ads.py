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
arr_seller_id = []

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

    #ambil seller_id
    query = f"select seller_id from db.{schema}.sellers;"

    # Menampilkan hasil
    arr_seller_id = [row[0] for row in conn.execute(query).fetchall()]  # Mengambil seller_id
    print(arr_seller_id)

    # Menutup koneksi setelah selesai
    conn.close()

except Exception as e:
    print(f"Gagal terhubung ke database: {e}")
    exit(1)

from faker import Faker
import random
import pandas as pd

#membuat variable untuk generator-variable sbg fungsi Faker
fake = Faker()
#membuat instance Faker dengan lokal Indonesia
fake = Faker('id_ID')

#membuat data dummy untuk tabel ads
#jumlah data yang ingin dibuat
n_ads = 200

#referensi data mobil
car_brands = [
    {
        'brand': 'Toyota',
        'models': [
            {'model': 'Avanza', 'engine': ['1.3L 4-Cyl', '1.5L 4-Cyl']},
            {'model': 'Innova', 'engine': ['2.0L 4-Cyl', '2.4L Diesel']},
            {'model': 'Rush', 'engine': ['1.5L 4-Cyl']},
            {'model': 'Yaris', 'engine': ['1.5L 4-Cyl']},
            {'model': 'Fortuner', 'engine': ['2.4L Diesel', '2.7L 4-Cyl']},
        ],
        'body_types': ['MPV', 'SUV', 'Hatchback']
    },
    {
        'brand': 'Honda',
        'models': [
            {'model': 'Jazz', 'engine': ['1.5L 4-Cyl']},
            {'model': 'Brio', 'engine': ['1.2L 4-Cyl']},
            {'model': 'Mobilio', 'engine': ['1.5L 4-Cyl']},
            {'model': 'CR-V', 'engine': ['1.5L Turbo', '2.0L 4-Cyl']},
            {'model': 'HR-V', 'engine': ['1.5L 4-Cyl', '1.8L 4-Cyl']}
        ],
        'body_types': ['Hatchback', 'SUV', 'MPV']
    },
    {
        'brand': 'Suzuki',
        'models': [
            {'model': 'Ertiga', 'engine': ['1.5L 4-Cyl']},
            {'model': 'Swift', 'engine': ['1.2L 4-Cyl', '1.4L 4-Cyl']},
            {'model': 'Jimny', 'engine': ['1.5L 4-Cyl']},
            {'model': 'Karimun Wagon R', 'engine': ['1.0L 3-Cyl']}
        ],
        'body_types': ['MPV', 'SUV', 'Hatchback']
    },
    {
        'brand': 'Daihatsu',
        'models': [
            {'model': 'Xenia', 'engine': ['1.3L 4-Cyl', '1.5L 4-Cyl']},
            {'model': 'Ayla', 'engine': ['1.0L 3-Cyl', '1.2L 4-Cyl']},
            {'model': 'Terios', 'engine': ['1.5L 4-Cyl']},
            {'model': 'Sigra', 'engine': ['1.0L 3-Cyl', '1.2L 4-Cyl']}
        ],
        'body_types': ['MPV', 'SUV', 'Hatchback']
    },
    {
        'brand': 'Nissan',
        'models': [
            {'model': 'Grand Livina', 'engine': ['1.5L 4-Cyl']},
            {'model': 'March', 'engine': ['1.2L 4-Cyl']},
            {'model': 'X-Trail', 'engine': ['2.0L 4-Cyl', '2.5L 4-Cyl']}
        ],
        'body_types': ['MPV', 'Hatchback', 'SUV']
    },
    {
        'brand': 'BMW',
        'models': [
            {'model': '3 Series', 'engine': ['2.0L 4-Cyl Turbo', '3.0L 6-Cyl Turbo']},
            {'model': 'X1', 'engine': ['2.0L 4-Cyl Turbo']}
        ],
        'body_types': ['Sedan', 'SUV']
    },
    {
        'brand': 'Mercedes-Benz',
        'models': [
            {'model': 'C-Class', 'engine': ['1.5L Turbo', '2.0L Turbo']},
            {'model': 'E-Class', 'engine': ['2.0L Turbo', '3.0L 6-Cyl Turbo']}
        ],
        'body_types': ['Sedan', 'Sedan']
    }
]

car_images = {
    'Toyota': {
        'Avanza': 'https://www.toyota.co.id/sites/default/files/styles/large/public/2023-07/Toyota%20Avanza.jpg',
        'Innova': 'https://www.toyota.co.id/sites/default/files/styles/large/public/2023-07/Toyota%20Innova.jpg',
        'Rush': 'https://www.toyota.co.id/sites/default/files/styles/large/public/2023-07/Toyota%20Rush.jpg',
        'Yaris': 'https://www.toyota.co.id/sites/default/files/styles/large/public/2023-07/Toyota%20Yaris.jpg',
        'Fortuner': 'https://www.toyota.co.id/sites/default/files/styles/large/public/2023-07/Toyota%20Fortuner.jpg',
    },
    'Honda': {
        'Jazz': 'https://www.honda-indonesia.com/assets/img/cars/jazz/main/overview-main.jpg',
        'Brio': 'https://www.honda-indonesia.com/assets/img/cars/brio/main/overview-main.jpg',
        'Mobilio': 'https://www.honda-indonesia.com/assets/img/cars/mobilio/main/overview-main.jpg',
        'CR-V': 'https://www.honda-indonesia.com/assets/img/cars/cr-v/main/overview-main.jpg',
        'HR-V': 'https://www.honda-indonesia.com/assets/img/cars/hr-v/main/overview-main.jpg',
    },
    'Suzuki': {
        'Ertiga': 'https://www.suzuki.co.id/media/cars/ertiga/ertiga-exterior.jpg',
        'Swift': 'https://www.suzuki.co.id/media/cars/swift/swift-exterior.jpg',
        'Jimny': 'https://www.suzuki.co.id/media/cars/jimny/jimny-exterior.jpg',
        'Karimun Wagon R': 'https://www.suzuki.co.id/media/cars/karimun-wagon-r/karimun-wagon-r-exterior.jpg',
    },
    'Daihatsu': {
        'Xenia': 'https://www.daihatsu.co.id/uploads/images/model-xenia.jpg',
        'Ayla': 'https://www.daihatsu.co.id/uploads/images/model-ayla.jpg',
        'Terios': 'https://www.daihatsu.co.id/uploads/images/model-terios.jpg',
        'Sigra': 'https://www.daihatsu.co.id/uploads/images/model-sigra.jpg',
    },
    'BMW': {
        '3 Series': 'https://www.bmw.co.id/content/dam/bmw/common/all-models/3-series/sedan/2020/BMW-3-series-sedan-2020.png',
        'X1': 'https://www.bmw.co.id/content/dam/bmw/common/all-models/x-series/x1/2020/BMW-X1-2020.png',
    },
    'Mercedes-Benz': {
        'C-Class': 'https://www.mercedes-benz.co.id/content/dam/mb-nafta/us/my2020/c-class/c-class-sedan-hero.png',
        'E-Class': 'https://www.mercedes-benz.co.id/content/dam/mb-nafta/us/my2020/e-class/e-class-sedan-hero.png',
    },
}

# Fungsi untuk mendapatkan URL gambar berdasarkan brand dan model
def generate_car_image(brand, model):
    return car_images.get(brand, {}).get(model, 'https://example.com/placeholder.jpg')

def generate_engine(brand, model):
    for car in car_brands:
        if car['brand'] == brand:
            for car_model in car['models']:
                if car_model['model'] == model:
                    return random.choice(car_model['engine'])
    return None  # Jika tidak ada, kembalikan None

# Menentukan mileage berdasarkan usia mobil
def generate_mileage(year_of_manufacture):
    current_year = 2024  # Ganti dengan tahun saat ini
    age_of_car = current_year - year_of_manufacture

    if age_of_car <= 2:
        return random.randint(1000, 50000)  # Mobil baru dengan mileage rendah
    elif 3 <= age_of_car <= 5:
        return random.randint(50000, 100000)  # Mobil bekas 3-5 tahun
    elif 6 <= age_of_car <= 10:
        return random.randint(100000, 150000)  # Mobil bekas 6-10 tahun
    else:
        return random.randint(150000, 250000)  # Mobil bekas lebih dari 10 tahun

#fungsi untuk menghasilkan data location, latitude, longitude secara acak
# def generate_location_data():
#     location= fake.city()
#     latitude = fake.latitude()
#     longitude = fake.longitude()
#     return location, latitude, longitude

#menghasilkan data lokasi dengan list comprehension
# location, latitude, longitude = zip(*[generate_location_data() for _ in range(n_ads)])

# Definisikan sellers sebelum digunakan
# Sudah tidak perlu menggunakan dummy seller lagi
# sellers = {
#     'seller_id': [fake.uuid4() for _ in range(100)]  # membuat 100 sellers
# }
sellers = {
    'seller_id': arr_seller_id  # membuat 100 sellers
}

# Generate data dummy ads
ads = {
    'ad_id': [fake.uuid4() for _ in range(n_ads)],
    'seller_id': [random.choice(sellers['seller_id']) for _ in range(n_ads)],
    'title': [],
    'description': [],
    'car_brand': [],
    'models': [],
    'body_car_type': [],
    'transmission': [random.choice(['Manual', 'Automatic']) for _ in range(n_ads)],
    'year_of_manufacture': [random.randint(2010, 2023) for _ in range(n_ads)],
    'color': [fake.color_name() for _ in range(n_ads)],
    'mileage': [],
    'engine': [],
    'price': [round(random.randint(95_000_000, 500_000_000), 2) for _ in range(n_ads)],
    'is_negotiable': [random.choice(['True', 'False']) for _ in range(n_ads)],
    'created_at': [fake.date_time_this_year() for _ in range(n_ads)],
    'updated_at': [fake.date_time_this_year() for _ in range(n_ads)],
    'status': [random.choice(['Active', 'Sold', 'Expired']) for _ in range(n_ads)],
    'image': []
}

#generate data location, latitude, longitude
# for i in range(n_ads):
#     location, latitude, longitude = generate_location_data() #menghasilkan data location, latitude, longitude
#     ads['location'].append(location) #menambahkan data location
#     ads['latitude'].append(latitude) #menambahkan data latitude
#     ads['longitude'].append(longitude) #menambahkan data longitude

# Generate car details
for i in range(n_ads):
    # Choose a random car brand and model
    brand_data = random.choice(car_brands)
    brand = brand_data['brand']
    model_data = random.choice(brand_data['models'])
    model = model_data['model']
    body_types = random.choice(brand_data['body_types'])

    # Append brand, model, and body type
    ads['car_brand'].append(brand)
    ads['models'].append(model)
    ads['body_car_type'].append(body_types)

    # Generate engine
    engine = random.choice(model_data['engine'])
    ads['engine'].append(engine)

    # Generate mileage
    year_of_manufacture = ads['year_of_manufacture'][i]
    mileage = generate_mileage(year_of_manufacture)
    ads['mileage'].append(mileage)

    # Generate image
    image = generate_car_image(brand, model)
    ads['image'].append(image)

    # Create title
    color = ads['color'][i]
    transmission = ads['transmission'][i]
    title = f"Dijual {brand} {model} {year_of_manufacture} {transmission} ({color}) - {body_types}"
    ads['title'].append(title)

    # Create description
    price = ads['price'][i]
    description = (
        f"Mobil bekas {brand}, {model} keluaran tahun {year_of_manufacture}, warna {color}, "
        f"tipe bodi {body_types}, dengan jarak tempuh {mileage} km, transmisi {transmission}, mesin {engine}. "
        f"Harga Rp {price:.2f}."
        f"{' Harga masih bisa nego.' if ads['is_negotiable'][i] == 'True' else ' Harga Pas.'} "
        f"Hubungi penjual segera untuk informasi lebih lanjut!"
    )
    ads['description'].append(description)

# Create dataframe
df_ads = pd.DataFrame(ads)

# Save to CSV
df_ads.to_csv('ads.csv', index=False)
print("Data telah diekspor ke ads.csv")

# Read CSV
df_ads = pd.read_csv('ads.csv')
print(df_ads.head())