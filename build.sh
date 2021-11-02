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

# zip up website contents (not to include docs folder name)

cd docs
zip -r ../docs.zip .
cd ../


# Build the PDF version of the book

jupyter-book build --path-output . src --builder pdfhtml
cp _build/pdf/book.pdf ./pdf/
rm -r _build/

# Push the changes to GitHub

git add .
git commit -m "Built the static website of the book."
git push