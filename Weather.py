#!/usr/bin/env python
# coding: utf-8

# # Pull data from meteorlogy

# In[1]:


import requests
import pandas as pd
import os
from datetime import datetime

# Define the URL for the API
url = "https://api.data.gov.my/weather/forecast"

# Make a request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Add a timestamp to the data
    df['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Define the CSV file path
    csv_file = 'weather_data.csv'
    
    # Check if the CSV file already exists
    if os.path.exists(csv_file):
        # Append the data to the existing file
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        # Create a new file with a header
        df.to_csv(csv_file, index=False)
    
    print("Data saved successfully.")
else:
    print("Failed to retrieve data:", response.status_code)

