!pip install flair
!pip install sentence-transformers

# importing all necessary libraries
import numpy as np
import pandas as pd
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()

from flair.models import TextClassifier
from flair.data import Sentence
from flair.embeddings import SentenceTransformerDocumentEmbeddings
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# remove 'no' and 'not' from the stopwords set as they give significant meaning to the reviews
stop_words = set(stopwords.words('english'))
stop_words.remove('not')
stop_words.remove('no')

data = pd.read_csv('browser_rankings_data.csv', skiprows = 1)

stop_words = set(stopwords.words('english'))

clean_text =[]
for review in data['Short Description']:
    review= re.sub(r'[^\w\s]', '', str(review))
    review = re.sub(r'\d','',review)
    # review_token = word_tokenize(review.lower().strip()) #convert reviews into lower case and strip leading and tailing spaces followed by spliting sentence into words
    review_without_stopwords=[]
    for token in review:
        if token not in stop_words:
            token= lemmatizer.lemmatize(token)
            review_without_stopwords.append(token)
    cleaned_review = " ".join(review_without_stopwords)
    clean_text.append(cleaned_review)

# assign cleaned reviews 
data["cleaned_review"] = clean_text

# run sentiment analysis on the reviews and assign one of Positive or Negative/Neutral depending on the positivity score of sentiment
embedding = SentenceTransformerDocumentEmbeddings('bert-base-nli-mean-tokens')
sia = TextClassifier.load('en-sentiment')
senti_list = []

for i in data["cleaned_review"]:
    sentence = Sentence(i)
    embedding.embed(sentence)
    sia.predict(sentence)
    senti_list.append(sentence.labels[0].score)

data["short_sentiment"] = senti_list

clean_text =[]
for review in data['Long Description']:
    review= re.sub(r'[^\w\s]', '', str(review))
    review = re.sub(r'\d','',review)
    review_without_stopwords=[]
    for token in review:
        if token not in stop_words:
            token= lemmatizer.lemmatize(token)
            review_without_stopwords.append(token)
    cleaned_review = " ".join(review_without_stopwords)
    clean_text.append(cleaned_review)

# assign cleaned reviews and filter out 1 star rated apps
data["cleaned_review"] = clean_text

# run sentiment analysis on the reviews and obtain the positivity score of sentiment
embedding = SentenceTransformerDocumentEmbeddings('bert-base-nli-mean-tokens')
sia = TextClassifier.load('en-sentiment')
senti_list = []

for i in data["cleaned_review"]:
    sentence = Sentence(i)
    embedding.embed(sentence)
    sia.predict(sentence)
    senti_list.append(sentence.labels[0].score)

data["long_sentiment"] = senti_list

import seaborn as sns
sns.set(rc = {'figure.figsize':(40,8)})
sns.regplot(x = data["Rank"], y = data["short_sentiment"])

import seaborn as sns
sns.regplot(x = data["Rank"], y = data["long_sentiment"])