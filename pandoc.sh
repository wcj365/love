#!/usr/bin/bash

# Step 1. Transform the contents for Pandoc

if [ -d "_pandoc" ] 
then
    rm -r _pandoc 
fi

mkdir _pandoc

# Step 2. Generate PDF version of the book


BOOKS="01_classic_poems 02_modern_poems 03_proses 04_english"

for book in $BOOKS
do
    python pandoc.py src/$book _pandoc/$book

    if [ "$book" = "01_classic_poems" ]
    then
        python classic_poems.py    # (序，自序等放在第一册格律诗中)
    fi

    pandoc --pdf-engine=xelatex  `find _pandoc/$book -name '*.md' | sort` -o docs/offline/$book.pdf
    pandoc --pdf-engine=xelatex  `find _pandoc/$book -name '*.md' | sort` -o docs/offline/$book.epub
    pandoc --pdf-engine=xelatex  `find _pandoc/$book -name '*.md' | sort` -o docs/offline/$book.docx
done

# Step 3. Push the changes to GitHub

git add .
git commit -m "Built the offline versions of the books (pdf | epub | docx)."
git push