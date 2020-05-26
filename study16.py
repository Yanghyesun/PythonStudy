import pandas as pd
import nltk
df = pd.read_csv('/Users/yanghyesun/bing_news_shuffle.csv', encoding = 'cp949')

text_data = df['description'].str.cat(sep=', ')

tokens = nltk.word_tokenize(text_data) 
tokens = [token.lower() for token in tokens if len(token) > 1]

from nltk.corpus import stopwords
stop_words = stopwords.words('english')
tokens_clean = [token for token in tokens if not token in stop_words]
tokens_tagged = nltk.pos_tag(tokens_clean)
tokens_noun = [word for word, pos in tokens_tagged if pos in ['NN', 'NNP']]

noun_text_data = (" ").join(tokens_noun)

#word cloud
import matplotlib.pyplot as plt
from wordcloud import WordCloud

wc = WordCloud(background_color="white", max_font_size=100, max_words=50)

wordcloud = wc.generate(noun_text_data)

plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')