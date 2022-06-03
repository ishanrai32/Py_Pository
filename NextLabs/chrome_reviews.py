# importing all necessary libraries
import numpy as np
import pandas as pd
import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk.stem import WordNetLemmatizer 
from textblob import TextBlob
lemmatizer = WordNetLemmatizer()

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# remove 'no' and 'not' from the stopwords set as they give significant meaning to the reviews
stop_words = set(stopwords.words('english'))
stop_words.remove('not')
stop_words.remove('no')

# read in the data for running the code on it
data = pd.read_csv("chrome_reviews.csv")
uploaded_file = st.file_uploader("Choose a file in csv format as input")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.write(dataframe)

# clean text by removing stopwords, lemmatizing data, removing leading and trailing whitespaces
clean_text =[]
for review in data['Text']:
    review= re.sub(r'[^\w\s]', '', str(review))
    review = re.sub(r'\d','',review)
    review_token = word_tokenize(review.lower().strip()) #convert reviews into lower case and strip leading and tailing spaces followed by spliting sentnece into words
    review_without_stopwords=[]
    for token in review_token:
        if token not in stop_words:
            token= lemmatizer.lemmatize(token)
            review_without_stopwords.append(token)
    cleaned_review = " ".join(review_without_stopwords)
    clean_text.append(cleaned_review)
    
# assign cleaned reviews and filter out 1 star rated apps
data["cleaned_review"] = clean_text
Single_star_reviews = data[data.Star == 1]

# run sentiment analysis on the reviews and assign one of Positive or Negative/Neutral depending on the positivity score of sentiment
sia = SentimentIntensityAnalyzer()
senti_list = []

for i in Single_star_reviews["cleaned_review"]:
    score = sia.polarity_scores(i)
    blob_score = TextBlob(i).sentiment.polarity
    if (score['pos'] >= 0.7):
        senti_list.append('Positive')
    else:
        senti_list.append('Negative/Neutral')
        
Single_star_reviews["sentiment"]= senti_list

# filtering out data with 1 star rating and positive review
positive_review_with_1_star = Single_star_reviews[Single_star_reviews.sentiment == 'Positive']
positive_review_with_1_star.drop("cleaned_review",axis = 1,inplace=True)

# giving output
positive_review_with_1_star.to_csv('output.csv')
