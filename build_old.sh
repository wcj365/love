if [ -d "_build" ] 
then
#    rm -r _build 
fi

jupyter-book build --path-output . src

if [ -d "docs" ] 
then
    rm -r docs 
fi

git add .
git commit -m "."
git push

mkdir docs

cp -r _build/html/* docs/
cp .nojekyll docs/
# rm -r _build/

git add .
git commit -m "."
git push
