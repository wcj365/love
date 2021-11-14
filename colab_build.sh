#!/usr/bin/bash

pip install -r requirements.txt

if [ -d "_build" ] 
then
    rm -r _build 
fi

if [ -d "docs" ] 
then
    rm -r docs 
fi

# Build the static website for the book

jupyter-book build --path-output . src
mkdir docs
cp -r _build/html/* ./docs/
cp .nojekyll docs/
rm -r _build/

# Push the changes to GitHub
git config --global user.name wcj365
git config --global user.email wcj365@gmail.com
git add .
git commit -m "Built the static website of the book."
git push