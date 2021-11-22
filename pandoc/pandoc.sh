#!/usr/bin/bash

# Transform files 

#python pandoc.py

# Generate PDF files

#BOOKS="classic_poems modern_poems proses english"

BOOKS="classic_poems"

for book in $BOOKS
do
    pandoc --pdf-engine=xelatex  `find ../_pandoc/$book -name '*.md' | sort` -o ../pdf/wcj365_$book.pdf
done