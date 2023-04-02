import csv
import requests
import json

url = "https://shop.unicornstore.in/cart/store_locator"

payload = "data=New+Delhi&data_state=Delhi&ajax=true&param=store"
headers = {
    'authority': 'shop.unicornstore.in',
    'accept': '*/*',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,hi;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'PHPSESSID=q8f8ui9s04rcsg90telhnq2fl5; _ga=GA1.2.2017187880.1680358973; _gid=GA1.2.867518694.1680358973; _gat_UA-133563307-2=1; ln_or=eyIyMjczNDc2IjoiZCJ9; _scid=78c5a4f7-c4d9-48a5-ab88-1d9fee5b6e8f; _gcl_au=1.1.398540766.1680358973; _sctr=1|1680287400000',
    'origin': 'https://shop.unicornstore.in',
    'referer': 'https://shop.unicornstore.in/find_store/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

response = requests.request("POST", url, headers=headers, data=payload)

# Parse the response text as JSON object
data = json.loads(response.text)

with open('store_data.csv', mode='w', newline='') as file:
    # Create a writer object
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Store Name', 'Address', 'Pincode','Timings', 'Phone', 'Latitude', 'Longitude'])
    # Write the data row by row
    for store in data:
         writer.writerow([
             store.get('store_name'),
             store.get('store_address'),
             store.get('pin_code'),
             '10am-6pm IST',
             store.get('store_contacts',),
             store.get('latitude'),
             store.get('longitude')
         ])
        
print("Data written to CSV file.")
