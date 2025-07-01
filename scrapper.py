import requests
import json
import csv
from bs4 import BeautifulSoup

url="http://books.toscrape.com"

def scrape_book(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to load page.")
        return []
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all("article", class_="product_pod")

    book_list = []
    for book in books:
        title = book.h3.a['title']
        price_text = book.find('p', class_= 'price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        book_list.append(
            {
                "title": title,
                "currency": currency,
                "price": price
            }
        )
    return(book_list)

all_books = scrape_book(url)

with open('books.json', 'w',encoding = "utf-8") as f:
    json.dump(all_books, f,indent=4,ensure_ascii=False)


with open('books.csv', 'w', newline = "", encoding = "utf-8") as f:
    writer = csv.DictWriter(f,fieldnames = ["title","currency","price"])
    writer.writeheader()
    writer.writerows(all_books)

#go to git bash
#git config --global user.name "Riya Bhattarai"
#git config --global user.email "kan078bct065@kec.edu.np"
#git ko through bata jati jana kam gardai xan tni haru sita le gareko kam combine garna milxa collaborate garna bela chai git use garxam.
#git use garnu  ko main karan hamro file ma k vairaxa sabai track garna parxa.kasle k code lekhyo kati jati code lekhyo sab thah huna parxa
#git ko kam vaneko file ra tesko content track garne ho.