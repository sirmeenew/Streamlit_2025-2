import streamlit as st

st.set_page_config(
  page_title="B935275_유민서",
  layout="wide",
  initial_sidebar_state = "expanded"
)

st.sidebar.title('K-pop Demon Hunters 분석')

with st.echo():
  import pandas as pd
from itertools import combinations
from collections import Counter
import matplotlib.pyplot as plt
import koreanize_matplotlib
import re
from konlpy.tag import Okt

df = pd.read_csv('./kdh_newsdata.csv')

headline = ''.join(df['title'].tolist())
headline

def cleanString(text):
  pattern = r'<[^>]*>'
  text = re.sub(pattern=pattern, repl='', string=text)
  
  pattern = r'[^\w\s\n]'
  text = re.sub(pattern=pattern, repl='', string=text)
  
  return text

from matplotlib import font_manager

han_font_path = font_manager.findfont('Malgun Gothic')

s = open('../Stopwords/stopwords.txt','r')
stopwords = s.read().splitlines()
print(stopwords)

headline_cleaned = cleanString(headline)

okt = Okt()

words_morphs = okt.morphs(headline_cleaned)

words = [word for word in words_morphs if word not in stopwords]
print(words)

descriptions = ''.join(df['description'].tolist())

descriptions_cleaned = cleanString(descriptions)

okt_2 = Okt()

descriptions_morphs = okt_2.morphs(descriptions_cleaned)

words_des = [word for word in descriptions_morphs if word not in stopwords]
print(words_des)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordsdes = WordCloud().generate(descriptions_cleaned)
print(wordsdes.words_)

wordshead = WordCloud().generate(headline_cleaned)
print(wordshead.words_)

plt.imshow(wordsdes)

