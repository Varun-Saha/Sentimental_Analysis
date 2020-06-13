import GetOldTweets3 as got

import string
from collections import Counter
import matplotlib.pyplot as plt


def get_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona virus') \
     .setSince("") \
     .setUntil("") \
     .setMaxTweets(10)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    '''
    In the tweets acquired from Twitter we choose the ones which we require and 
    pass the rest to tweet from tweet we segregate the text and store them inside
    text_tweets
    '''
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets




# text received is a list we will need to convert it into a string.
text = ""
text_tweets = get_tweets()
length = len(text_tweets)

for i in range(0, length):
    text = text_tweets[i][0] + "" + text




# Encoding is used to decipher the text from Blog or Posts to normal readable text data.
# = open('read.txt', encoding='utf-8').read()

# Convert all the letters into lowercase text.
lower_case = text.lower()

'''
1) Remove all the punctuation marks.
2) The translate function is usaed tp convert the existing variable to a desired variables.
3) 'maketrans' is used to translate the variable to a predefined mapped values.
4) string.punctuation means that we are targeting the punctuation marks present inside the sentence.
5) ('a', 'b', c) maps as ('variables that need to be repalaced', 'new variables which will be put instead of the new variables', 'values to be removed')
'''
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenisation: Splitting the words in a sentence and storing these words in a list.
tokenised_words = cleaned_text.split()


# Stop Words: These are words which do not add any meaning to the sentence and can be discarded.
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Creating an empty list for storing the new words acquired after removing the stop words.
new_words = []
# Traversing through the total words achieved after tokenization.
for word in tokenised_words:
    if word not in stop_words:
# Appending the word to the empty list.
      new_words.append(word)

# The list which will contain all the emotion attributes from the read.txt file and emotions file
emotion_list = []
# Opening new file
with open('emotions.txt', 'r') as file:
    for line in file:

# Removing spaces, commas etc from the emotions file.
        clean_line = line.replace('\n', '').replace(',', '').replace("'",'').strip()
# Assigning the word before colon to word and after colon to emotion.
        word, emotion = clean_line.split(':')

        if word in new_words:
            emotion_list.append(emotion)

# This will help us in counting the word and the emotion attribute associated with the word.
word_count = Counter(emotion_list)
print (word_count)

# Using the 'matplotlib' we can now develop a new graph.
fig, axi = plt.subplots()
axi.bar(word_count.keys(), word_count.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()