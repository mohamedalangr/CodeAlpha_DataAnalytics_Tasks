# 📘 Task 1: Web Scraping – Books to Scrape

## 🔍 Objective

The goal of this task is to extract product (book) data from the website [Books to Scrape](https://books.toscrape.com/), a sandbox site for practicing web scraping. We use Python tools to collect data, store it in a structured format, and perform basic analysis and visualizations.

---

## 🧰 Tools & Technologies Used

- Python
- Jupyter Notebook
- BeautifulSoup
- Requests
- Pandas
- Matplotlib & Seaborn

---

## 📂 Extracted Data Fields

From the first 5 pages of the website, we collected the following information for each book:

- 📖 **Title**
- 💷 **Price (£)**
- ⭐ **Rating** (converted from text to numeric)
- 📦 **Availability**
- 🔗 **Product URL**

---

## 📑 Dataset

The extracted data was stored in a CSV file named:  
📄 `books_data.csv`

A preview of the dataset:

| Title                          | Price (£) | Rating | Availability     |
|--------------------------------|-----------|--------|------------------|
| A Light in the ...             | 51.77     | 3      | In stock         |
| Tipping the Velvet             | 53.74     | 1      | In stock         |
| Soumission                     | 50.10     | 1      | In stock         |

---

## 📈 Visualizations

We created the following visual insights using Seaborn and Matplotlib:

- 📊 **Book Ratings Distribution**

  ![Ratings Plot](#) <!-- replace with actual image link if needed -->

- 💰 **Price Distribution**

  ![Price Plot](#)

---

## 🧪 Sample Code Snippet

```python
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
rating = rating_map.get(rating_class, 0)
