#!/usr/bin/bash

# Step 1
# Install required Python packages

pip install -r requirements.txt

# Step 2
# Instsall system packages required for generating PDF version using Puppeteer
# https://developers.google.com/web/tools/puppeteer

sudo apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

# Step 3 
# Install 楷体 font for Chinese Character
# https://gist.github.com/allex/11203573

sudo apt-get install fonts-arphic-ukai
