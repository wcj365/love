#!/usr/bin/env python3

import glob
import os

source_folder = "src/classic_poems"
pandoc_folder = "pandoc/classic_poems"

if not os.path.exists(pandoc_folder):
    os.mkdir(pandoc_folder) 

chapter_folders = ["wu_jue", "wu_lv","qi_jue", "qi_lv", "ci_ling", "other"]

for chapter_folder in chapter_folders:
    files = glob.glob(f"{source_folder}/{chapter_folder}/*.md") 
    chapter_file = pandoc_folder + chapter_folder + ".md"
    if os.path.exists(chapter_file):
        os.remove(chapter_file)
    with open(chapter_file, "a") as f_append:
        for file in files:
            if "README.md" in file:
                continue
            with open(file, "r") as f_read:
                f_append.writelines(f_read.readlines())



    

