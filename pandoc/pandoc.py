#!/usr/bin/env python3

import glob
import os
import shutil

SOURCE_FOLDER = "../src/classic_poems"
TARGET_FOLDER = "./classic_poems"

if not os.path.exists(TARGET_FOLDER):
    os.mkdir(TARGET_FOLDER) 

shutil.copy("../src/xu.md",TARGET_FOLDER + "/01_xu.md")
shutil.copy("../src/zi_xu.md",TARGET_FOLDER + "/02_zi_xu.md")
shutil.copy("../src/ya_ge.md",TARGET_FOLDER + "/03_ya_ge.md")
shutil.copy("../src/word_cloud.md",TARGET_FOLDER + "/04_word_cloud.md")

CHAPTERS = ["05_wu_jue", "06_wu_lv","07_qi_jue", "08_qi_lv", "09_ci_ling", "10_other"]


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



    

