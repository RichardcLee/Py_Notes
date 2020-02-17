from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path
# print(STOPWORDS)

# 该文件包含一些词汇
with open('words_clean.txt') as f:
	text = f.read()
# print(text)

wordcloud = WordCloud(stopwords=STOPWORDS, background_color='#222222', width=1000, height=800).generate(text)

plt.figure(figsize=(13, 12))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()