from bs4 import BeautifulSoup
import requests


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
        break
    elif choice == '2':
        url = global_best_series
        break
    elif choice == '3':
        url = indian_best_movies
        break
    elif choice == '4':
        url = indian_best_series
        break
    else:
        print("Invalid input! Please make sure you type a number corresponding to the option.")
