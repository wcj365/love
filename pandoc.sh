#!/usr/bin/bash

# Step 1. Transform the contents for Pandoc

if [ -d "_pandoc" ] 
then
    rm -r _pandoc 
else
    mkdir _pandoc
fi

# Step 2. Generate PDF version of the book

#BOOKS="01_classic_poems 02_modern_poems 03_proses 04_english"
BOOKS="04_english"

for book in $BOOKS
do
    python pandoc.py src/$book _pandoc/$book
    pandoc --pdf-engine=xelatex  `find src/$book -name '*.md' | sort` -o docs/offline/$book.pdf
    pandoc --pdf-engine=xelatex  `find src/$book -name '*.md' | sort` -o docs/offline/$book.epub
done

pandoc --pdf-engine=xelatex `find _pandoc -name '*.md' | sort` --toc-depth=2 -V toc-title -o docs/offline/dao_de_jing.pdf
pandoc --pdf-engine=xelatex `find _pandoc -name '*.md' | sort` --toc-depth=2 -o docs/offline/dao_de_jing.epub

# Step 3. Push the changes to GitHub

git add .
git commit -m "Built the PDF verion of the book."
git push