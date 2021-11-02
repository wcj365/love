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

git add .
git commit -m "."
git push
