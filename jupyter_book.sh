#!/usr/bin/bash

if [ -d "_build" ] 
then
    rm -r _build 
fi

if [ -d "docs" ] 
then
    rm -r docs 
fi

# Build the static website for the book

jupyter-book build --path-output . src > jupyter_book.log
mkdir docs
cp -r pdf ./docs/
cp -r offline ./docs/
cp -r _build/html/* ./docs/
cp .nojekyll docs/

# Push the changes to GitHub

git add .
git commit -m "Built the static website."
git push
