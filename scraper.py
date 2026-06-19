import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

for page in range(1, 51):

    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:

        title = book.h3.a["title"]

        price = book.find("p", class_="price_color").text

        rating = book.find("p")["class"][1]

        data.append([title, price, rating])

df = pd.DataFrame(
    data,
    columns=["Title", "Price", "Rating"]
)

df.to_csv("all_books.csv", index=False)

print("Total Books:", len(df))
print("Data Saved Successfully")