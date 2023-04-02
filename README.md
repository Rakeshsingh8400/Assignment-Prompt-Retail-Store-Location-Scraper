# Assignment-Prompt-Retail-Store-Location-Scraper
Assignment Prompt: Retail Store Location Scraper

**REPORT**

Approach:

The given code is a Python script that sends a POST request to a web page URL and retrieves JSON data. The JSON data is then parsed, and the required data is extracted and saved to a CSV file.

I used an  application knows as POSTMAN to get the required header and payload information.
Postman,  it is a popular tool used for testing API requests. You can use it to send requests to the same URL with different parameters and see the responses. This can help in debugging and testing the API endpoint before integrating it into your code.

First, we import the necessary modules, including requests for sending HTTP requests, json for handling JSON data, and csv for writing to CSV files. We then define the URL and the request payload, along with the headers required for the request.

We then send the POST request using the requests module and retrieve the JSON data in the response. The JSON data is then parsed using the json module, and the required data is extracted from the JSON data.

Finally, the extracted data is written to a CSV file using the csv module. A CSV file is created and opened in write mode. A writer object is then created to write the data to the CSV file. The writer object writes the header row first, followed by the data row by row.

Challenges:

My primary non technical challenge was to find a website that let's you scrape the data and also has all the required data. I tried on Apple, Domino's Pizza and Taco Bell before using Unicorn Stores. Apart from that Unicorn stores does not have Store timings but since all the stores have the same timings I manually wrote it in the csv using writer.writerow function.

One of the main challenges faced while working with this code was to extract the required data from the JSON response. As the JSON response was a nested structure, it required careful understanding and analysis to extract the relevant data. However, this was overcome by using the built-in Python JSON module and accessing the required data using the appropriate keys.

Another challenge was to write the data to the CSV file in the required format. As the data was in a nested structure, it required careful manipulation and formatting to be written to the CSV file. However, this was overcome by using the csv writer object to write the data row by row, with each row containing the required information in the correct format.

Overall, the approach involved using the appropriate Python modules to handle HTTP requests, JSON data, and CSV files, along with careful understanding and manipulation of the data structures to extract and write the required data in the correct format.




Code of the Assignment:

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

