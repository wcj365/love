if [ -d "_build" ] 
then
    rm -r _build 
fi

if [ -d "docs" ] 
then
    rm -r docs 
fi

jupyter-book build --path-output . src --builder pdfhtml

mkdir docs

cp -r _build/html/* ./docs/
cp .nojekyll docs/
cp _build/pdf/book.pdf ./pdf/

rm -r _build/

git add .
git commit -m "Built the static website of the book."
git push
