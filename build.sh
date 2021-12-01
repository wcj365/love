#!/usr/bin/bash

# Step 1 - Start from scratch

if [ -d "_build" ] 
then
    rm -r _build 
fi

if [ -d "docs" ] 
then
    rm -r docs 
fi


# Step 2 - Build the static website for the book
# The interim results are in _build folder

jupyter-book build --path-output . src > jupyter_book.log


# Step 3 - Copy the genreated website to docs folder 

mkdir docs
mkdir docs/offline            # to store pdf and epub version of the book
cp -r _build/html/* ./docs/   # This is the contents of the generated website
cp .nojekyll ./docs/          # required for GitHub pages to render without using jekyll
cp -r pdf ./docs/             # pdf files of academic writings


# Step 4 - Transform markdown files for PDF and epub geeration

cd pandoc
python pandoc.py


# Step 5 - Generate PDF and epub files

BOOKS="classic_poems modern_poems proses english"

for book in $BOOKS
do
    pandoc --pdf-engine=xelatex  `find ../_pandoc_pdf/$book -name '*.md' | sort` -o ../docs/offline/wcj365_$book.pdf
    pandoc --pdf-engine=xelatex  `find ../_pandoc_epub/$book -name '*.md' | sort` -o ../docs/offline/wcj365_$book.epub
done


# Step 6 - Push the changes to GitHub

cd ../

git add .
git commit -m "Built the static website."
git push