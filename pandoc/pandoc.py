#!/usr/bin/env python3

import glob
import os
import shutil

SOURCE = "../src/"
TARGET = "../_pandoc/"

BOOKS = ["classic_poems", "modern_poems", "proses", "english"]

if os.path.exists(TARGET):
    shutil.rmtree(TARGET) 

os.mkdir(TARGET) 

for book in BOOKS:

    BOOK_SOURCE = f"{SOURCE}{book}/"
    BOOK_TARGET = f"{TARGET}{book}/"

    os.mkdir(BOOK_TARGET) 

    shutil.copy(f"00_{book}.md",f"{BOOK_TARGET}00_{book}.md")

    if book == "classic_poems":
        files = os.listdir(SOURCE)
        for file in files:
            if not file.startswith("0"):
                continue      
            shutil.copy(SOURCE + file, BOOK_TARGET)
            if file.endswith(".md"):
                with open(BOOK_TARGET + file, "a") as f_append:
                    f_append.write("\n\n")
                    f_append.write("\\newpage")
                    f_append.write("\n\n")   

        CHAPTERS = ["07_wu_jue", "08_wu_lv","09_qi_jue", "10_qi_lv", "11_ci_ling", "12_other"]
        
    elif book == "modern_poems":
        CHAPTERS = ["01_nature", "02_solitude","03_wisdom", "04_homesick", "05_love", "06_birthday", "07_english"]
    elif book == "proses":
        CHAPTERS = ["01_politics", "02_econ_tech","03_life", "04_health", "05_fun", "06_wisdom", "07_poetry","08_wordgame"]
    else:    # book == "english"
        CHAPTERS = ["01_academic", "02_system", "03_tea"]

    for chapter in CHAPTERS:
        chapter_folder = BOOK_SOURCE + chapter[3:]
        files = glob.glob(chapter_folder + "/*.md")
        files.sort()
        chapter_file = BOOK_TARGET + chapter + ".md"
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