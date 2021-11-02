if [ -d "_build" ] 
then
    rm -r _build 
fi

jupyter-book build --path-output . src --builder pdfhtml

cp _build/pdf/book.pdf ./pdf/
rm -r _build/

git add .
git commit -m "built the PDF version of the book."
git push
