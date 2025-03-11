import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Create sellers table
sellers = {
    'seller_id': [fake.uuid4() for _ in range(100)]  # Generate 100 unique seller IDs
}

# Create ads table
n_ads = 200
ads = {
    'ad_id': [fake.uuid4() for _ in range(n_ads)],
    'seller_id': [random.choice(sellers['seller_id']) for _ in range(n_ads)],
    # Other fields...
}

# Convert to DataFrames
df_sellers = pd.DataFrame(sellers)
df_ads = pd.DataFrame(ads)

# Validate connections
# Check if all seller_ids in ads exist in sellers
missing_sellers = set(df_ads['seller_id']) - set(df_sellers['seller_id'])
if not missing_sellers:
    print("All seller IDs in ads are valid and exist in the sellers table.")
else:
    print(f"Missing seller IDs in sellers table: {missing_sellers}")


#import libraries
import pandas as pd
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Create sample tables
n_sellers = 100
n_buyers = 100
n_ads = 200
n_bids = 300

# Generate unique IDs
sellers = {'seller_id': [fake.uuid4() for _ in range(n_sellers)]}
buyers = {'buyer_id': [fake.uuid4() for _ in range(n_buyers)]}
ads = {
    'ad_id': [fake.uuid4() for _ in range(n_ads)],
    'seller_id': [random.choice(sellers['seller_id']) for _ in range(n_ads)]
}
bids = {
    'bid_id': [fake.uuid4() for _ in range(n_bids)],
    'buyer_id': [random.choice(buyers['buyer_id']) for _ in range(n_bids)],
    'ad_id': [random.choice(ads['ad_id']) for _ in range(n_bids)]
}

# Convert to DataFrames
df_sellers = pd.DataFrame(sellers)
df_buyers = pd.DataFrame(buyers)
df_ads = pd.DataFrame(ads)
df_bids = pd.DataFrame(bids)

# Validate connections
# Check if all buyer_ids in bids exist in buyers
missing_buyers = set(df_bids['buyer_id']) - set(df_buyers['buyer_id'])
if not missing_buyers:
    print("All buyer IDs in bids are valid and exist in the buyers table.")
else:
    print(f"Missing buyer IDs in buyers table: {missing_buyers}")

# Check if all ad_ids in bids exist in ads
missing_ads = set(df_bids['ad_id']) - set(df_ads['ad_id'])
if not missing_ads:
    print("All ad IDs in bids are valid and exist in the ads table.")
else:
    print(f"Missing ad IDs in ads table: {missing_ads}")

# Check if all seller_ids in ads exist in sellers
missing_sellers = set(df_ads['seller_id']) - set(df_sellers['seller_id'])
if not missing_sellers:
    print("All seller IDs in ads are valid and exist in the sellers table.")
else:
    print(f"Missing seller IDs in sellers table: {missing_sellers}")
