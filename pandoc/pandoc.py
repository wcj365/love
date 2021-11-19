#!/usr/bin/env python3

import glob
import os

SOURCE_FOLDER = "../src/classic_poems"
TARGET_FOLDER = "./classic_poems"

if not os.path.exists(TARGET_FOLDER):
    os.mkdir(TARGET_FOLDER) 

CHAPTERS = ["01_wu_jue", "02_wu_lv","03_qi_jue", "04_qi_lv", "05_ci_ling", "06_other"]


for chapter in CHAPTERS:
    chapter_folder = SOURCE_FOLDER + "/" + chapter[3:]
    files = glob.glob(chapter_folder + "/*.md")
    files.sort()
    chapter_file = TARGET_FOLDER + "/"+ chapter + ".md"
    if os.path.exists(chapter_file):
        os.remove(chapter_file)
    with open(chapter_file, "a") as f_append:
        with open(chapter_folder + "/README.md", "r") as f_read:
            f_append.write(f_read.readline())
            f_append.write("\n")
        for file in files:
            if "README.md" in file:
                continue
            with open(file, "r") as f_read:
                f_append.write("#")
                lines = f_read.readlines()
                for line in lines:
                    if "![]" in line:
                        f_append.write("![](" + "../" + chapter_folder + "/" + line[4:])
                    else:
                        f_append.write(line)
                f_append.write("\n\n")
                f_append.write("\\newpage")
                f_append.write("\n\n")



    

