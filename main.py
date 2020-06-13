import string
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
# Encoding is used to decipher the text from Blog or Posts to normal readable text data.
text = open('read.txt', encoding='utf-8').read()

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
tokenised_words = word_tokenize(cleaned_text, "english")

# Removing the stop words which are redundant in a sentence.


# Creating an empty list for storing the new words acquired after removing the stop words.
new_words = []
# Traversing through the total words achieved after tokenization.
for word in tokenised_words:
    if word not in stopwords('english'):
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