import requests
from scrape import ScrapeData
from format_data import Format

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:145.0) Gecko/20100101 Firefox/145.0",
    "Accept-Language": "en-US,en;q=0.5"
}

global_best_movies = "https://www.imdb.com/best-of/most-popular-movies-2025/"

global_best_series = "https://www.imdb.com/best-of/most-popular-series-2025/"

indian_best_movies = "https://www.imdb.com/list/ls4156041707/"

indian_best_series = "https://www.imdb.com/list/ls4156506611/"

print("Please choose an option:")
print("1. Global Best Movies")
print("2. Global Best Series")
print("3. Indian Best Movies")
print("4. Indian Best Series")

while True:
    choice = input("Enter the number corresponding to your choice: ").strip()

    if choice == '1':
        url = global_best_movies
        print("Fetching url...")
        response = requests.get(url, headers=headers)
        print("Scraping data...")
        sc = ScrapeData(response)
        names, descriptions, details = sc.global_movies()
        print("Formatting data...")
        f = Format(names, descriptions, details)
        f.format_movies()
        print("Done!")
        break
    elif choice == '2':
        url = global_best_series
        print("Fetching url...")
        response = requests.get(url, headers=headers)
        print("Scraping data...")
        sc = ScrapeData(response)
        break
    elif choice == '3':
        url = indian_best_movies
        break
    elif choice == '4':
        url = indian_best_series
        break
    else:
        print("Invalid input! Please make sure you type a number corresponding to the option.")

response = requests.get(url)

data = response.text

soup = (data, "html.parser")
