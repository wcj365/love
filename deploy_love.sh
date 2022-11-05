#!/usr/bin/bash
 
# this script is to be placed in the home directory in PythonAnywhere.com
# Running this script will refresh the website with the latest from GitHub

#wget --user=wcj365 --ask-password --auth-no-challenge https://github.com/wcj365/love/archive/refs/heads/main.zip
wget https://github.com/wcj365/love/archive/refs/heads/main.zip                                                                                 

unzip main.zip
 
cp -r love-main/docs/* love/
 
rm main.zip

rm -rf love-main
