###Extract

import pandas as pd

# File paths for the uploaded CSV files

files = [
    '/mnt/data/tmp738_purk.csv',
    '/mnt/data/tmpdfeo3qy2.csv',
    '/mnt/data/tmpfap3hfze.csv',
    '/mnt/data/tmpkd_w64k_.csv',
    '/mnt/data/tmp6w6ts2d7.csv',
    '/mnt/data/tmpf_uzkqpk.csv',
    '/mnt/data/tmp3apxsafn.csv',
    '/mnt/data/tmp3ochjtdc.csv',
    '/mnt/data/tmpzr3l5bxw.csv'
]

# Load each CSV file into a DataFrame and store them in a list
dataframes = [pd.read_csv(file) for file in files]

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Display basic information about the combined DataFrame
print(combined_df.info())

# Optionally, display the first few rows of the combined DataFrame
print(combined_df.head())


###Transform
import requests

api_key = 'your_api_key_here'

def forward_geocode(address, api_key):
    url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {'q': address, 'key': api_key}
    response = requests.get(url, params=params)
    if response.ok:
        data = response.json()
        if data['results']:
            return data['results'][0]['geometry']['lat'], data['results'][0]['geometry']['lng']
    return None, None

def reverse_geocode(lat, lon, api_key):
    url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {'lat': lat, 'lng': lon, 'key': api_key}
    response = requests.get(url, params=params)
    if response.ok:
        data = response.json()
        if data['results']:
            return data['results'][0]['formatted']  # This returns the full formatted address
    return None

# Example usage:
# Forward geocoding
lat, lon = forward_geocode('1600 Pennsylvania Ave NW, Washington, DC 20500', api_key)
print(lat, lon)

# Reverse geocoding
street = reverse_geocode(lat, lon, api_key)
print(street)

###Load

from sqlalchemy import create_engine
import pandas as pd

# Your transformed DataFrame
# combined_df = ...

# Database connection information
database_username = 'your_username'
database_password = 'your_password'
database_ip       = 'localhost'
database_name     = 'your_database_name'
database_connection = 'sqlite:///C:/Users/hanus/OneDrive/Desktop/Projects/Boston_Crime_Data/test_database.db'

#use below command if sql database details are available
#database_connection = f'mysql+pymysql://{database_username}:{database_password}@{database_ip}/{database_name}'


# Create database engine
engine = create_engine(database_connection)

# Load the DataFrame into SQL
combined_df.to_sql('crime_data', con=engine, if_exists='replace', index=False)

print("Data loaded successfully")
