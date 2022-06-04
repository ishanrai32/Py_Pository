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
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')

# remove 'no' and 'not' from the stopwords set as they give significant meaning to the reviews
stop_words = set(stopwords.words('english'))
stop_words.remove('not')
stop_words.remove('no')

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Enter the Password", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Enter the Password", type="password", on_change=password_entered, key="password")
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    # read in the data for running the code on it
    st.title("Chrome reviews")
    st.header("Upload csv file in chrome_reviews format")
    st.markdown('This application takes csv input from the user in chrome_reviews format. It outputs reviews that were positive in sentiment but had 1-star rating.')

    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
      data = pd.read_csv(uploaded_file)
      st.write(data)
      st.subheader('Functioning of the code is as follows:')
      st.markdown('1.   Import libraries. Pick a pre-trained model for sentiment analysis.')
      st.markdown('2.   Remove stopwords. Exclude *no* and *not* as these have meaning in the reviews.')
      st.markdown('3.   Cleaning the text further by lemmatization and keeping a uniform lower case with leading, trailing whitespaces removed.')
      st.markdown('4.   Filter out rows with 1 star rating. Apply the Sentiment Analyzer on the reviews of these rows.')
      st.markdown('5.   If positivity score > 0.7, the review is considered to be positive.')
      st.markdown('6.   Return rows that have 1 star rating and Positive review.')
      # clean text by removing stopwords, lemmatizing data, removing leading and trailing whitespaces
      clean_text =[]
      for review in data['Text']:
          review= re.sub(r'[^\w\s]', '', str(review))
          review = re.sub(r'\d','',review)
          review_token = word_tokenize(review.lower().strip()) #convert reviews into lower case and strip leading and tailing spaces followed by spliting sentence into words
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
      # positive_review_with_1_star.to_csv('output.csv')
      st.header("Reviews with positive text and 1-star ratings")
      st.write(positive_review_with_1_star)
      csv_output = positive_review_with_1_star.to_csv().encode('utf-8')
      st.download_button(label = 'Download the output file', data = csv_output, file_name = 'positive_review_with_1_star.csv', mime = 'text/csv')
