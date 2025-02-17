from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

tweet = "@MehhranShakarami today's cold @ home 😔 https://mehranshakarami.com"

#preprocess tweet
tweet_words = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    
    elif word.startswith('http'):
        word = 'http'
    tweet_words.append(word)

tweet_proc = " ".join(tweet_words)
print(tweet_proc)

#load model and tokenizer
roberta = "cardiffnlp/twitter-roberta-base-sentiment-latest"

model = AutoModelForSequenceClassification.from_pretrained(roberta)

tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Positive', 'Neutral']

#sentiment analysis
encoded_tweet = tokenizer(tweet_proc, return_tensors='pt')

output = model(encoded_tweet['input_ids'], encoded_tweet['attention_mask'])

scores = output[0][0].detach().numpy()
scores = softmax(scores)

for i in range(len(scores)):

    l = labels[i]
    s = scores[i]
    print(l,s)
