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
