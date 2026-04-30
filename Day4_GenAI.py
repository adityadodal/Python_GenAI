# in this session we will learn about tokenization and how to use it in our projects
# tokenization is the process of breaking down a piece of text into smaller units called tokens. These tokens can be words, subwords, or even characters. Tokenization is an essential step in natural language processing (NLP) tasks, as it allows us to convert raw text into a format that can be easily processed by machine learning models.
# there are different types of tokenization techniques, such as word tokenization, subword tokenization, and character tokenization. Word tokenization breaks down text into individual words, while subword tokenization breaks down words into smaller units, which can be useful for handling out-of-vocabulary words. Character tokenization breaks down text into individual characters, which can be useful for certain NLP tasks.
# in this session we will focus on word tokenization and how to use it in our projects. We will use the NLTK library in Python, which provides a simple and efficient way to perform tokenization. We will also explore how to use tokenization in conjunction with other NLP techniques, such as stemming and lemmatization, to further process our text data. By the end of this session, you will have a solid understanding of tokenization and how to use it in your NLP projects.
# first we need to install the NLTK library if we haven't already. We can do this using pip:
# pip install nltk
# once we have NLTK installed, we can start using it for tokenization. Here's a simple example of how to use NLTK for word tokenization:

from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
import nltk
from nltk.tokenize import word_tokenize
# download the necessary resources for tokenization
nltk.download('punkt')
# example text
text = "Hello, how are you doing today? I hope you're having a great day!"
# tokenize the text
tokens = word_tokenize(text)
print(tokens)
# output: ['Hello', ',', 'how', 'are', 'you', 'doing',
# 'today', '?', 'I', 'hope', "you're", 'having', 'a', 'great', 'day', '!']
# as you can see, the text has been tokenized into individual words and punctuation marks.
# we can also use tokenization in conjunction with other NLP techniques, such as stemming and lemmatization, to further process our text data. Stemming is the process of reducing words to their base or root form, while lemmatization is the process of reducing words to their base or dictionary form. Here's an example of how to use stemming and lemmatization with tokenization:
# download the necessary resources for lemmatization
nltk.download('wordnet')
# initialize the stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
# example text
text = "The cats are running in the garden."
# tokenize the text
tokens = word_tokenize(text)
# stem the tokens
stemmed_tokens = [stemmer.stem(token) for token in tokens]
# lemmatize the tokens
lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
print("Original Tokens:", tokens)
print("Stemmed Tokens:", stemmed_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)
# output:
# Original Tokens: ['The', 'cats', 'are', 'running', 'in', 'the', 'garden', '.']
# Stemmed Tokens: ['the', 'cat', 'are', 'run', 'in', 'the', 'garden', '.']
# Lemmatized Tokens: ['The', 'cat', 'are', 'running', 'in', 'the', 'garden', '.']
# as you can see, the stemmed tokens have been reduced to their base form, while the lemmatized tokens have been reduced to their dictionary form. This can be useful for various NLP tasks, such as text classification, sentiment analysis, and information retrieval.

nltk.download('punkt')
nltk.download('punkt_tab')

nltk.download('punkt', quiet=True)
