# 📘 Task 1: Web Scraping – Books to Scrape

In this task, I extracted book information from the website [Books to Scrape](https://books.toscrape.com/) using Python.
The scraped data includes:
- Title
- Price (£)
- Rating
- Availability
- Product Page URL

The data is saved as a CSV file and analyzed briefly for patterns.
## 🔧 Step 1: Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
## 🔍 Step 2: Scrape Book Data

We loop through the first 5 pages of the site to collect book details.
# we put the url of the site
base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []

# looping through the 5 pages
for page in range(1,6):
    print(f"Scraping Page {page}...")
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # find book containers
    articles = soup.find_all("article", class_="product_pod")

    for book in articles:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.replace("£", "")
        availability = book.find("p", class_="instock availability").text.strip()
        rating_class = book.p["class"][1]
        rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating = rating_map.get(rating_class, 0)
        link = "http://books.toscrape.com/catalogue/" + book.h3.a["href"]

        books.append({
            "Title": title,
            "Price (£)": float(price),
            "Availability": availability,
            "Rating": rating,
            "URL": link
        })
        
## 💾 Step 3: Save Data to CSV
df = pd.DataFrame(books)
df.to_csv("books_data.csv", index=False)
print("Scraping complete. Saved to books_data.csv")
df.head()
## 📊 Step 4: Basic Data Analysis
df.info()
df.describe()
df["Rating"].value_counts()
df["Availability"].value_counts()
## 📈 Step 5: Visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Rating distribution
plt.figure(figsize=(6,4))
sns.countplot(x="Rating", data=df)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.show()
In this Task, I:
- Scraped 100 books from 5 pages of `books.toscrape.com`
- Collected key data fields including Title, Price, Rating, and Availability
- Stored the data in CSV format
- Performed basic statistical and visual analysis
