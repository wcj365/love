#!/usr/bin/bash

# Transform files for PDF
python pandoc_pdf.py

# Transform files for epub
python pandoc_epub.py

# Generate PDF and epub files

BOOKS="classic_poems modern_poems proses english"
#BOOKS="classic_poems"


for book in $BOOKS
do
    pandoc --pdf-engine=xelatex  `find ../_pandoc_pdf/$book -name '*.md' | sort` -o ../pdf/wcj365_$book.pdf
    pandoc --pdf-engine=xelatex  `find ../_pandoc_epub/$book -name '*.md' | sort` -o ../pdf/wcj365_$book.epub
#    pandoc --pdf-engine=xelatex  `find ../_pandoc/$book -name '*.md' | sort` -o ../pdf/wcj365_$book.docx
#    pandoc --pdf-engine=xelatex  `find ../_pandoc/$book -name '*.md' | sort` -o ../pdf/wcj365_$book.html
done

# Push the changes to GitHub

cd ../

git add .
git commit -m "Built the PDF verion of the books."
git push