from bs4 import BeautifulSoup
import requests
import re

date = input("Enter the date like this MM/DD/YY: ")

# Get the URL from the requests module
page = requests.get(f"https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa?date={date}#matchesclipNext")

def main(page):
    # Get the content of the page as a byte
    src = page.content

    # Convert from a byte code to HTML code
    soup = BeautifulSoup(src, "lxml")

    # Find all div elements with class containing "matchcard"
    championships = soup.find_all("div", class_=re.compile(".*matchcard.*"))

    # Extract and print the text content of each element
    for championship in championships:
        print(championship)

main(page)
