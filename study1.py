from bs4 import BeautifulSoup
from collections import Counter
from urllib.request import urlopen
import nltk
soup = BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/Computer"))
words = nltk.word_tokenize(soup.text)
count = Counter(words)

print("computer : {} Computer : {} hardware : {}".format(count['computer'],count['Computer'],count['hardware']))