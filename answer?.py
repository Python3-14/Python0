def get_sen(text):
    blob = Textblob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        sentiment = "Positive"
    elif polarity < -0.1:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment, polarity #polarity is reused to determine rating

for i in range(len(reviews)):
    sentiment,polarity = get_sen(reviews[1])
    rat = rating(polarity)

    topic_scores = lda_model[corpus[i]]
    main_topic = max(topic_scores, key=lambda item: item[1])

    topic_nnumber = main_topic[0]
    topic_score  = main_topic[main_topic

    topic_words = lda_model.show_topic(topic_number, topn =5) 
    keywords = []
    for word, score in topic_words:
        keywords.append(word)
    rating_counts[rating] += 1
    total

