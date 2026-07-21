import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from textblob import TextBlob

def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative" 
    else:
        return "neutral"
def sentiment_analysis(text):
    print("Target String:",text)
    print("Sentiment:",get_sentiment(text))
example_string = "The chef made a great dinner. The chef made a disgusting dinner. The chef made a simple dinner."
# for i in sent_tokenize(example_string):
#     print(i)
# print(word_tokenize(example_string))
words = word_tokenize(example_string)

stop_words = set(stopwords.words("english"))
punc = [".",",","'"]
good_words = []

for word in words:
    if word not in stop_words and word not in punc:
        good_words.append(words)
        sentiment_analysis(word)
