# Import necessary libraries
from bs4 import BeautifulSoup  # BeautifulSoup for HTML parsing
import requests  # Requests for making HTTP requests

# Set the user-agent string to mimic a web browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Define a function to get weather information for a given city
def weather(city):
    # Replace spaces in the city name with '+' for constructing a valid URL
    city = city.replace(" ", "+")
    
    # Construct the URL for Google search with the city name
    url = f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'
    
    # Send an HTTP GET request to the constructed URL with headers
    res = requests.get(url, headers=headers)
    
    # Print a message indicating the search is in progress
    print("Searching......\n")
    
    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(res.text, 'html.parser')   
    
    
    # Extract location, time, additional information, and temperature using CSS selectors
    location = soup.select('#wob_loc')[0].getText().strip()  # Location
    time = soup.select('#wob_dts')[0].getText().strip()       # Time
    info = soup.select('#wob_dc')[0].getText().strip()        # Additional information
    weather_temp = soup.select('#wob_tm')[0].getText().strip()  # Temperature
    
    # Print the extracted information
    print(location)
    print(time)
    print(info)
    print(weather_temp + "°C")

# Take user input for the city name
city = input("Enter the Name of Any City >>  ")

# Append "weather" to the city name to improve search accuracy
city = city + " weather"

# Call the weather function with the modified city name
weather(city)
