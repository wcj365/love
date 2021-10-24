jupyter-book build --path-output . docs2
mkdir docs
mv -r _build/html/* docs/
cp .nojekyll docs/
rm -r _build/
git add .
git commit -m "."
git push
