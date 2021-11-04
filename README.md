# 乡愁永酒诗文集

## 参考资料

- [字体转换器在线转换生成书法艺术字体](http://www.diyiziti.com/)
- Book Name
  - width 620 图像宽度
  - height 180 图像高度
  - size 90 汉字大小
- Signature
  - width 1100 图像宽度
  - height 100 图像高度
  - size 70 汉字大小


- vi global search and find `6,10s/foo/bar/g`

# How to Build

1. run `$ pip install -r requirements.txt`
2. run `$ . build.sh` to generate the static website in docs folder
3. run `$ . buildpdf.sh` to generate the pdf version of the book

## How to Deploy to PythonAnywhere.com
1. Go to the docs folder `$cd docs`
2. Zip up contents in docs folder `$ zip -r docs.zip .`
3. Download the zip file
4. Upload the zip file to PythonAnywhere to the love folder
5. Unzip the file

## Notes

to support Chinese Latex generation for PDF `sudo apt install latex-cjk-all`

to install Pandoc


sudo apt-get update -y

sudo apt-get install -y pandoc

`pip install pyppeteer`

~~~
sudo apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
~~~

    html_theme_options:
      search_bar_text: " "
