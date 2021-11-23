#!/usr/bin/bash 

import os
import glob

from PIL import Image
import numpy as np

import wordcloud
import jieba

#BOOKS = ["classic_poems", "modern_poems", "proses", "english"]
BOOKS = ["classic_poems"]

for book in BOOKS:
    wc_file = "wc_" + book + ".txt"
    if os.path.exists(wc_file):
        os.remove(wc_file) 
    with open(wc_file, "a") as f_append:
        files = glob.glob(f"../src/{book}/**/*.md", recursive=True)
        files.sort()
        for file in files:
            if "README.md" in file:
                continue
            with open(file, "r") as f_read:
                lines = f_read.readlines()
                for line in lines:
                    if line.startswith("![]") or line.startswith("\\newpage"):
                        continue
                    else: 
                        f_append.write(line)
            f_append.write("\n")


WC_ALL = "wc_all.txt"

if os.path.exists(WC_ALL):
    os.remove(WC_ALL) 

with open(WC_ALL, "a") as f_append:
    for book in BOOKS:
        if book == "english":
            continue
        wc_file = "wc_" + book + ".txt"
        with open(wc_file, "r") as f_read:
            f_append.writelines(f_read.readlines())
            f_append.write("\n")
    

mask = np.array(Image.open('china_map.png'))

# This is specifically created according to my document

my_stopwords = ["美","中","有","一","二","三","四","五", "七", "新","年","字","更", "其","指",
    "不","不要", "不能", "一天", "一种","新韵","有感", "一首", "里","", "而", "太","皆", "拉", "出自",
    "出", "自","正", "莫", "作","生", "日", "偶", "文章","出","入","外", "成", "比利", "BQ", "波士",
    "萍","韵","猴","哥","注","附","群","微","信","拉松","代表"]


cn_stopwords = []
with open("cn_stopwords.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        cn_stopwords.append(line.strip())

# wordcloud comes with its default stop words list which include English words
stopwords = my_stopwords + cn_stopwords + list(wordcloud.STOPWORDS)  

#BOOKS.append("all")

for book in BOOKS:
    wc_file = "wc_" + book + ".txt"

    # read the source data (saved from Word to plain text with Chinese Simpled GB2312 encoding)
    with open(wc_file, "r") as f:
        txt = f.read()

    word_list = jieba.lcut(txt,cut_all=True)   # 结巴词库切分词 精准模式
 #   word_list = [word for word in word_list if len(word.strip())>1]   #清洗一个字的词
    word_clean = " ".join(word_list)
    with open("wc_" + book + "_clean.txt", "w") as f:
        f.write(word_clean)

    w = wordcloud.WordCloud(width=1000,
                            height=700,
                          #  max_words=150,
                          #  min_font_size=8,
                            stopwords=stopwords,
                            background_color='white',
                            font_path='/usr/share/fonts/truetype/arphic-bkai00mp/bkai00mp.ttf',
                            mask=mask, 
                            contour_width=3, 
                            contour_color='steelblue',
                            scale=15)

    w.generate(word_clean)

    w.to_file("../src/04_word_cloud.png")
