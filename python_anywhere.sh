#!/usr/bin/bash

wget https://github.com/wcj365/love/archive/refs/heads/main.zip

unzip main.zip

cp -r love-main/docs/* love/

rm main.zip

rm -rf love-main
