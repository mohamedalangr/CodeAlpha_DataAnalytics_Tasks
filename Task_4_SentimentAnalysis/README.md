# 💬 Task 4: Sentiment Analysis – IMDB Movie Reviews

## 🎯 Objective

The objective of this task is to analyze the sentiment of movie reviews using Natural Language Processing (NLP) techniques.  
The reviews are classified into three categories:
- **Positive**
- **Negative**
- **Neutral**

---

## 🧰 Tools & Libraries Used

- Python
- Jupyter Notebook
- pandas
- seaborn
- matplotlib
- TextBlob
- re (Regular Expressions)
- nltk
- WordCloud (optional)

---

## 📑 Dataset Description

- Name: **IMDB Dataset of 50K Movie Reviews**
- Size: 50,000 labeled reviews
- Format: CSV
- Columns:
  - `review` — text of the movie review
  - `sentiment` — original binary label (`positive`/`negative`) – not used for our TextBlob-based classification

---

## 🔎 NLP Steps Performed

1. **Text Cleaning**: Removed HTML tags, non-alphabetic characters, and converted to lowercase.
2. **Sentiment Scoring**: Used TextBlob’s polarity score to classify each review as:
   - Positive (polarity > 0)
   - Negative (polarity < 0)
   - Neutral (polarity = 0)
3. **Data Labeling**: Added a new `Sentiment` column to the dataset.
4. **Visualization**: Plotted sentiment distribution and generated word clouds.

---

## 📊 Visual Outputs

- Bar chart showing the distribution of sentiment categories
- Word cloud of most frequent words in **positive** reviews
- Sample random reviews by sentiment

---

## ✅ Key Findings

- Most reviews are classified as **Positive**, which aligns with the natural bias in public review datasets.
- Word clouds highlight frequent adjectives like *"great"*, *"amazing"*, and *"love"* in positive reviews.
- TextBlob offers a simple but powerful baseline method for quick sentiment classification.

---

## 📁 Files Included

- `sentiment_analysis.ipynb` – Main notebook with all steps
- `IMDB Dataset.csv` – Dataset used
- `README.md` – This documentation file

---

## 🔚 Conclusion

This project demonstrates the basics of sentiment analysis using Python and TextBlob.  
It shows how to preprocess text, apply sentiment scoring, and visualize the emotional content of text data.  
The results can be extended to product reviews, tweets, or customer feedback analysis.

✔️ Task 4 Completed.
