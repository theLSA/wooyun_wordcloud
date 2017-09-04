# coding: utf-8


import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = open("wooyunBugTitle.txt","r").read()
cutData = jieba.cut(data, cut_all=True)
word = " ".join(cutData)

cloud = WordCloud(
    #设置字体，不指定可能会出现中文乱码
    font_path="msyh.ttf",
    #font_path=path.join(e,'xxx.ttc'),
    #设置背景色
    background_color='white',
    #词云形状
    #mask=color_mask,
    #允许最大词汇
    max_words=2000,
    #最大号字体
    max_font_size=40
    )

wc = cloud.generate(word)
wc.to_file("wooyunwordcloud.jpg") 
plt.imshow(wc)
plt.axis("off")
plt.show()