# from nltk.tokenize import sent_tokenize, word_tokenize

# EXAMPLE_TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# print(sent_tokenize(EXAMPLE_TEXT))

# print(word_tokenize(EXAMPLE_TEXT))
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()
example_words = ["python","pythoner","pythoning","pythoned","pythonly"]
for w in example_words:
    print(ps.stem(w))

new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))