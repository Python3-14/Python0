import gensim
from gensim.models import Word2Vec
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def preprocess(text):
    words = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    punc=[".",",","'","(",")"]
    good_words =[]
    for word in words:
        if word.casefold() not in stop_words and word not in punc:
            good_words.append(word)
    reduced =[]
    for word in good_words:
        if word.casefold() not in reduced:
            reduced.append(word)
    return reduced

def train_word2vec(sentence):
    model = Word2Vec(sentence,vector_size=100,window=5,min_count=1,workers=4)
    return model

def calculate_similarity(target,sentence,model):
    targetWords = preprocess(target)
    sentWords = preprocess(sentence)
    sim = model.wv.n_similarity(targetWords,sentWords)
    return sim

def find_similar(target,sentence,model,topN = 5):
    simList =[]
    for sent in sentence:
        sim = calculate_similarity(target,sent,model)
        tup = (sent,sim)
        simList.append(tup)
    simList = sorted(simList,key= lambda x: x[1], reverse = True)
    simStrings = [(sim[0],sim[1])for sim in simList[:topN]]
    return simStrings 
def getRec(word,sentences):
    preprocessSents = [preprocess(sent) for sent in sentences]

    model = train_word2vec(preprocessSents)
    simStrings = find_similar(word,sentences,model)

    print("Target string:", word)
    print("Top most similar strings:")
    for i, (simString, simScore) in enumerate(simStrings,1):
        print(f"{i},'{simString}' -- Similarity Score:{(simScore*100):.1f}%")

sentences = [
    "hello world",
    "how are you",
    "what is your name",
    "python programming language",
    "data science is fun",
    "do you want six or seven gummy bears"
]
target_string = "programming"

getRec(target_string,sentences)