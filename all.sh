#!/usr/bin/bash

. jupyter_book.sh > jupyter-book.log

cd pandoc

. pandoc.sh > pandoc.log
