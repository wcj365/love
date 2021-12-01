#!/usr/bin/bash

# Transform files for PDF and epub format
python pandoc.py

# Generate PDF and epub files

BOOKS="classic_poems modern_poems proses english"
#BOOKS="english"

if [ ! -d "../src/offline" ] 
then
    mkdir ../src/offline 
fi

for book in $BOOKS
do
    pandoc --pdf-engine=xelatex  `find ../_pandoc_pdf/$book -name '*.md' | sort` -o ../src/offline/wcj365_$book.pdf
    pandoc --pdf-engine=xelatex  `find ../_pandoc_epub/$book -name '*.md' | sort` -o ../src/offline/wcj365_$book.epub
done

# Push the changes to GitHub
cd ../

git add .
git commit -m "Built the PDF verion of the books."
git push