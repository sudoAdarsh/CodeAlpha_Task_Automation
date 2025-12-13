from bs4 import BeautifulSoup

class ScrapeData():
    def __init__(self, response):
        self.response = response.text
    
    def global_movies(self):
        soup = BeautifulSoup(self.response, "html.parser")
        names = soup.find_all(name="h3", class_="EnhancedListItemContent_heading__ODx0z")
        descriptions = soup.find_all(name="div", class_="ipc-html-content-inner-div")

        all_details = soup.find_all(name="li", class_="ipc-inline-list__item")

        details = []
        start = 0
        end = 4
        for _ in range(10):
            current_details = all_details[start:end]
            start += 4
            end += 4
            detail = [i.text.replace(u'\xa0', u' ') for i in current_details]
            details.append(detail)

        return names, descriptions, details
    
    def indian_movies(self):
        soup = BeautifulSoup(self.response, "html.parser")
        names = soup.find_all(name="h3", class_="ipc-title__text")[0:10]
        ratings = soup.find_all(name="span", class_="ipc-rating-star--rating")
        descriptions = soup.find_all(name="div", class_="ipc-html-content-inner-div")[1:]

        return names, descriptions, ratings
