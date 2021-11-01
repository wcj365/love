if [ -d "_build" ] 
then
    rm -r _build 
fi

jupyter-book build --path-output . src --builder pdfhtml
