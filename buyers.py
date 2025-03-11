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
n_buyer = 100

#fungsi untuk menghasilkan nomor telepon dengan format konsisten 
def generate_phone_number():
 return f"+62-{random.randint(100,999)}-{random.randint(1000,9999)}-{random.randint(1000,9999)}"

#fungsi untuk membuat riwayat pembelian acak
def generate_purchase_history():
 num_purchases = random.randint(1,5) #jumlah pembelian acak
 purchases = [f"Purchase {i+1}: {fake.date_time_this_year()}" for i in range(num_purchases)]
 return "; ".join(purchases)

#membuat data dummy sellers
buyers ={
 'buyer_id': [fake.uuid4() for _ in range(n_buyer)],
 'name': [fake.name() for _ in range(n_buyer)],
 'email': [fake.ascii_free_email() for _ in range(n_buyer)],
 'password': [fake.password() for _ in range(n_buyer)],
 'contact_number': [generate_phone_number() for _ in range(n_buyer)],
 'location': [fake.city_name().replace('\n', ', ') for _ in range(n_buyer)],
 'registration_date': [fake.date_time() for _ in range(n_buyer)],
 'status': [random.choice(['Active', 'Inactive']) for _ in range (n_buyer)],
 'purchase_history': [round(random.uniform(1.0, 5.0),2) for _ in range(n_buyer)]
}

#membuat dataframe
df_buyers = pd.DataFrame(buyers)

#membuat file csv
df_buyers.to_csv('buyers.csv', index=False)
print("Data telah diekspor ke buyers.csv")

#membaca file csv
df_buyers = pd.read_csv('buyers.csv')