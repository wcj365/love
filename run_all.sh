#!/usr/bin/bash

#1 Step 1 build static website using Jupyter Book

. jupyterbook.sh 


# Step 2 build pdf and epub version of the book

. pandoc.sh 

# Step 3  check-in

. git_all.sh