# in this session we will learn about tokenization and how to use it in our projects
# tokenization is the process of breaking down a piece of text into smaller units called tokens. These tokens can be words, subwords, or even characters. Tokenization is an essential step in natural language processing (NLP) tasks, as it allows us to convert raw text into a format that can be easily processed by machine learning models.
# there are different types of tokenization techniques, such as word tokenization, subword tokenization, and character tokenization. Word tokenization breaks down text into individual words, while subword tokenization breaks down words into smaller units, which can be useful for handling out-of-vocabulary words. Character tokenization breaks down text into individual characters, which can be useful for certain NLP tasks.
# in this session we will focus on word tokenization and how to use it in our projects. We will use the NLTK library in Python, which provides a simple and efficient way to perform tokenization. We will also explore how to use tokenization in conjunction with other NLP techniques, such as stemming and lemmatization, to further process our text data. By the end of this session, you will have a solid understanding of tokenization and how to use it in your NLP projects.
# first we need to install the NLTK library if we haven't already. We can do this using pip:
# pip install nltk
# once we have NLTK installed, we can start using it for tokenization. Here's a simple example of how to use NLTK for word tokenization:

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
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

# we can also use the `punkt` tokenizer to tokenize text into sentences instead of words. Here's an example of how to use the `punkt` tokenizer for sentence tokenization:
# example text
text = "Hello, how are you doing today? I hope you're having a great day!"
# tokenize the text into sentences
sentences = sent_tokenize(text)
print(sentences)
# output: ['Hello, how are you doing today?', "I hope you're having a great day!"]
# as you can see, the text has been tokenized into individual sentences. This can be useful for various NLP tasks, such as text summarization, question answering, and dialogue systems.
# in summary, tokenization is a crucial step in natural language processing that allows us to break down text into smaller units called tokens. We can use the NLTK library in Python to perform tokenization, and we can also combine it with other NLP techniques like stemming and lemmatization to further process our text data. Additionally, we can use the `punkt` tokenizer to tokenize text into sentences, which can be useful for various NLP tasks.
# in the next session, we will learn about stop words and how to remove them from our text data. Stop words are common words that do not carry much meaning and can be removed from text to improve the performance of NLP models. We will explore how to use NLTK to remove stop words from our text data and how it can benefit our NLP tasks.
# in the meantime, you can practice tokenization by using the NLTK library to tokenize different pieces of text and experimenting with stemming and lemmatization. You can also try tokenizing text into sentences using the `punkt` tokenizer. This will help you get a better understanding of how tokenization works and how it can be applied in various NLP tasks.

# that's all for this session. In the next session, we will dive deeper into stop words and how to remove them from our text data using NLTK. Stay tuned!
# in the meantime, you can practice tokenization by using the NLTK library to tokenize different pieces of text and experimenting with stemming and lemmatization. You can also try tokenizing text into sentences using the `punkt` tokenizer. This will help you get a better understanding of how tokenization works and how it can be applied in various NLP tasks.
# that's all for this session. In the next session, we will dive deeper into stop words and how to remove them from our text data using NLTK. Stay tuned!

# solve the below practice problems to test your understanding of tokenization and its applications:
# 1. Write a Python function that takes a piece of text as input and returns a list of tokens using NLTK's word_tokenize function.
# 2. Write a Python function that takes a list of tokens as input and returns a list of stemmed tokens using NLTK's PorterStemmer.
# 3. Write a Python function that takes a list of tokens as input and returns a list of lemmatized tokens using NLTK's WordNetLemmatizer.
# 4. Write a Python function that takes a piece of text as input and returns a list of sentences using NLTK's sent_tokenize function.
# 5. Write a Python function that takes a piece of text as input and returns a list of tokens with stop words removed using NLTK's stopwords list.

# here are the solutions to the practice problems:
# 1. Function to tokenize text


def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens
# 2. Function to stem tokens


def stem_tokens(tokens):
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return stemmed_tokens
# 3. Function to lemmatize tokens


def lemmatize_tokens(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens
# 4. Function to tokenize text into sentences


def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences
# 5. Function to remove stop words from tokens


def remove_stop_words(tokens):
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [
        token for token in tokens if token.lower() not in stop_words]
    return filtered_tokens


# you can test these functions with different pieces of text to see how they work. For example:
text = "Hello, how are you doing today? I hope you're having a great day!"
tokens = tokenize_text(text)
stemmed_tokens = stem_tokens(tokens)
lemmatized_tokens = lemmatize_tokens(tokens)
sentences = tokenize_sentences(text)
filtered_tokens = remove_stop_words(tokens)
print("Tokens:", tokens)
print("Stemmed Tokens:", stemmed_tokens)
print("Lemmatized Tokens:", lemmatized_tokens)
print("Sentences:", sentences)
print("Filtered Tokens:", filtered_tokens)
# output:
# Tokens: ['Hello', ',', 'how', 'are', 'you', 'doing', 'today', '?', 'I', 'hope', "you're", 'having', 'a', 'great', 'day', '!']
# Stemmed Tokens: ['hello', ',', 'how', 'are', 'you', 'do', 'today', '?', 'I', 'hope', "you'RE", 'have', 'a', 'great', 'day', '!']
# Lemmatized Tokens: ['Hello', ',', 'how', 'are', 'you', 'doing', 'today', '?', 'I', 'hope', "you're", 'having', 'a', 'great', 'day', '!']
# Sentences: ['Hello, how are you doing today?', "I hope you're having a great day!"]
# Filtered Tokens: ['Hello', ',', 'doing', 'today', '?', 'I', 'hope', "you're", 'having', 'great', 'day', '!']

# as you can see, the functions work as expected, and you can use them to process different pieces of text for various NLP tasks.
# that's all for this session. In the next session, we will learn about stop words and how to remove them from our text data using NLTK. Stay tuned!
# goodbye!
# PRACTICE THE ABOVE CODE AND TRY TO UNDERSTAND IT. IF YOU HAVE ANY QUESTIONS, FEEL FREE TO ASK. SEE YOU IN THE NEXT SESSION!
