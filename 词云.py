from tkinter import W
import wordcloud
wordcloud=wordcloud.WordCloud(width=2000,height=2000,background_color='white')
txt='A,C,A,A'
wordcloud.generate(txt)
wordcloud.to_file("1.jpg")