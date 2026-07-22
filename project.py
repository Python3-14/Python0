import gensim
from gensim.models import Word2Vec
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from textblob import TextBlob
from gensim import corpora
from gensim import models
from collections import defaultdict

reviews = [
    "This movie was horrible",
    "Huh"
]
def preprocess(text):
    Word=[]
    for t in text:
        words = word_tokenize(t)
        stop_words = set(stopwords.words("english"))
        punc = [",","'",'"',"(",")","-","/"]
        for word in words:
            if word.casefold() not in stop_words and word.casefold() not in punc:
                Word.append(word)
    return Word

def sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.05:
        print(text,"positive")
    elif polarity < -0.05:
        print(text,"negative")
    else:
        print(text,"neutral")
    print("Polarity Score:",polarity)
    return polarity

def rating(p):
    if p <= -0.8:
        return 1
    if p <= -0.3:
        return 2
    if p < 0:
        return 3
    if p < 0.5:
        return 4
    else:
        return 5
def stars(r):
    print("★"*r + "☆" * (5-r))

texts = preprocess(reviews)
for t in texts:
    a = sentiment(t)
    b = rating(a)
    stars(b)

def create_lda(reviews):
    cleaned_reviews =[]
    for review in reviews:
        cleaned_reviews.append(preprocess(review))
    dictionary = corpora.Dictionary(cleaned_reviews)
    corpus = []
    for review in cleaned_reviews:
        corpus.append(dictionary.doc2bow(review))
    lda_model = models.LdaModel(
        corpus, id2word = dictionary,
        num_topics = 3, passes =20, random_state=42,minimum_probability=0
    )
    

# corpus = [dictionary.doc2bow(text) for text in texts]

# def LDA(corpus,dictionary):
#     lda_model = models.LdaModel(corpus,id2word=dictionary,num_topics=3)
#     corpus_lda = lda_model[corpus]
#     print(corpus_lda)

# LDA(corpus,dictionary)