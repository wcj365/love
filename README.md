# 乡愁永酒诗文集

## 参考资料

- [字体转换器在线转换生成书法艺术字体](http://www.diyiziti.com/)
- Book Name (乡愁永酒)
  - width 620 图像宽度
  - height 180 图像高度
  - size 90 汉字大小
- Signature
  - width 1100 图像宽度
  - height 100 图像高度
  - size 70 汉字大小
- 古典诗文佛经引用
  - 文鼎古印体繁或四库全书古籍字体
  - width 640 图像宽度
  - height 200 图像高度
  - size 36 汉字大小
  - 参见七律东方智慧引用金刚经

## vi Search and Replace 

**`6,10s/foo/bar/g`**

- s for Substitude 
- g for global search and replace
- 6, 10 for between line 6 and line 10

## How to Build

- 先生成网站再生成PDF文档
    - `$ . all.sh` 
- 只生成网站
    - `$ . jupyter_book.sh` 
- 只生成PDF文档
    - `$ cd pandoc`
    - `$ . pandoc.sh` 
- 生成第一册格律诗词云图
    - `$ cd word_cloud`
    - `$ python word_cloud.py`
    
## How to Deploy to PythonAnywhere.com

- `$ cd love_repo`
- `$ git pull`

## Miscellenous Notes

to support Chinese Latex generation for PDF `sudo apt install latex-cjk-all`

to install Pandoc


sudo apt-get update -y

sudo apt-get install -y pandoc

`pip install pyppeteer`

To install 楷体 font for Chinese Character:

`sudo apt-get install fonts-arphic-ukai`

https://gist.github.com/allex/11203573

~~~
sudo apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
~~~

    html_theme_options:
      search_bar_text: " "
