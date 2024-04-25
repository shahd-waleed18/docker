import nltk
from nltk.corpus import stopwords
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

# to define the stop words in the paragraph
stop_words = set(stopwords.words('english'))

# to read the txt file
with open(r"/app/paragraphs.txt") as f:
    text = f.read()

    # (tokenize ) function is to seperate the the text into words
    words = nltk.word_tokenize(text)

    # Remove stop words
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # A Counter for the words frequency after removing the stop words
    word_freq = Counter(filtered_words)

    # Displaying the  word frequency
    for word, freq in word_freq.items():
        print(f'{word}: {freq}')