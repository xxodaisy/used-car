#import library
from faker import Faker 
import pandas as pd
import random
import re 

#membuat variable untuk generator-variable sbg fungsi Faker
fake = Faker()
#membuat instance Faker dengan lokal Indonesia
fake = Faker('id_ID')

#jumlah data yg ingin dibuat
n_seller = 100

#fungsi untuk menghasilkan nomor telepon dengan format konsisten 
def generate_phone_number():
 return f"+62-{random.randint(100,999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"

#membuat data dummy sellers
sellers ={
 'seller_id': [fake.uuid4() for _ in range(n_seller)],
 'name': [fake.name() for _ in range(n_seller)],
 'email': [fake.ascii_free_email() for _ in range(n_seller)],
 'password': [fake.password() for _ in range(n_seller)],
 'contact_number': [generate_phone_number() for _ in range(n_seller)],
 'location': [fake.city_name().replace('\n', ', ') for _ in range(n_seller)],
 'registration_date': [fake.date_time() for _ in range(n_seller)],
 'status': [random.choice(['Active', 'Inactive']) for _ in range (n_seller)],
 'rating': [round(random.uniform(1.0, 5.0),2) for _ in range(n_seller)],
 'number_of_sales': [random.randint(0, 100) for _ in range(n_seller)]
}

#membuat dataframe
df_sellers = pd.DataFrame(sellers)

#membuat file csv
df_sellers.to_csv('sellers.csv', index=False)
print("Data telah diekspor ke sellers.csv")

#membaca file csv
df_sellers = pd.read_csv('sellers.csv')


