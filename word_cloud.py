import wordcloud

import jieba

from PIL import Image
import numpy as np

import os
import glob



WC_FILE = "word_cloud_all.md"

BOOKS = ["classic_poems", "modern_poems", "proses"]

if os.path.exists(WC_FILE):
    os.remove(WC_FILE) 

with open(WC_FILE, "a") as f_append:
    for book in BOOKS:
        files = glob.glob(f"./src/{book}/**/*.md", recursive=True)
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

# read the source data (saved from Word to plain text with Chinese Simpled GB2312 encoding)
with open(WC_FILE, "r", encoding="utf8") as f:
    txt = f.read()

word_list = jieba.lcut(txt,cut_all=False)   # 结巴词库切分词
word_list = [word for word in word_list if len(word.strip())>1]   #清洗一个字的词
word_clean = " ".join(word_list)

#Use the map of China as the background imapge

mk = np.array(Image.open('china_map.png'))

#w = wordcloud.WordCloud(mask=mk)
#w = wordcloud.WordCloud(font_path="/usr/share/fonts/truetype/arphic-bkai00mp/bkai00mp.ttf")
# This is generally used for Chinese text


# This is specifically created according to my document
stopwords_2 = ["打一两字常用词","一天","一种","一起", "", "一次", "很多", "一首", "附", "不能", "不同", "有", "以后", "其","不","不要","只有","理","不可","什么", "重要", "怎么", "乃至", "知", "不知",
"只是","可是", "其中","更加","不再","也是", "是","https", "只好", "乃至", "意思", "超芳", "不到","不好","不少","十分",
"萍", "和", "字", "比如", "故", "答", "意思是","猴哥",
"新韵", "注","这里的","一", "二", "三", "例外","其次","等等","另外", "所以", "你们说", "有一天", "是的"]

# wordcloud comes with its default stop words list which include English words
#stopwords = stopwords_1 + stopwords_2 + list(wordcloud.STOPWORDS)  

stopwords = []
with open("cn_stopwords.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        stopwords.append(line.strip())



# 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        stopwords=stopwords + stopwords_2 + list(wordcloud.STOPWORDS),
                        background_color='white',
                        font_path='/usr/share/fonts/truetype/arphic-bkai00mp/bkai00mp.ttf',
                        mask=mk, 
                        contour_width=3, 
                        contour_color='steelblue',
                        scale=15)

# 将txt变量传入w的generate()方法，给词云输入文字
w.generate(word_clean)

# 将词云图片导出到文件夹
w.to_file('word_cloud.png')
