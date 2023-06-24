import requests
import csv
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find the table that holds the list of countries
table = soup.find("table", class_="wikitable")

# Find all the rows in the table (excluding the header row)
rows = table.find_all("tr")[1:]

# Create a CSV file to save the data
csv_file = open("top_countries.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Rank", "Country"])

# Iterate over the rows and extract the rank and country
for row in rows:
    cells = row.find_all("td")
    
    # Ensure the row has the expected number of cells
    if len(cells) >= 2:
        rank = cells[0].text.strip()
        country = cells[1].text.strip()
        
        # Write the rank and country to the CSV file
        csv_writer.writerow([rank, country])

csv_file.close()

print("Data has been successfully scraped and saved to 'top_countries.csv'.")
