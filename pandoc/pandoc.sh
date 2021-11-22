#!/usr/bin/bash

# Transform files 

python pandoc.py

# Generate PDF files

BOOKS="classic_poems modern_poems proses english"

for book in $BOOKS
do
    pandoc --pdf-engine=xelatex  `find ../_pandoc/$book -name '*.md' | sort` -o ../pdf/wcj365_$book.pdf
done

# Push the changes to GitHub

cd ../

git add .
git commit -m "Built the static website and the PDF verion of the book."
git push