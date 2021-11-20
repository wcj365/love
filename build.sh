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

jupyter-book build --path-output . src
mkdir docs
cp -r _build/html/* ./docs/
cp .nojekyll docs/
rm -r _build/

# Note: The zip file has exceeded 50MB, the limit of GitHub.
# zip up website contents (docs folder name is preserved) 
# if [ -f "docs.zip" ]
# then
#     rm docs.zip
# fi
# zip -r docs.zip ./docs/

# Build the PDF version of the book 

#jupyter-book build --path-output . src --builder pdfhtml
#cp _build/pdf/book.pdf ./pdf/
#rm -r _build/

# Push the changes to GitHub

git add .
git commit -m "Built the static website and the PDF verion of the book."
git push
