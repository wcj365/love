#!/usr/bin/env python3

import glob
import os
import shutil

SOURCE = "../src/"
TARGET = "../_pandoc_pdf/"

BOOKS = ["classic_poems", "modern_poems", "proses", "english"]

CHAPTERS_CN = ["一", "二", "三", "四", "五", "六", "七", "八"]

if os.path.exists(TARGET):
    shutil.rmtree(TARGET) 

os.mkdir(TARGET) 

for book in BOOKS:

    BOOK_SOURCE = f"{SOURCE}{book}/"
    BOOK_TARGET = f"{TARGET}{book}/"

    os.mkdir(BOOK_TARGET) 

    shutil.copy(f"{book}.md",f"{BOOK_TARGET}000_{book}.md")

    if book == "classic_poems":
        files = os.listdir(SOURCE)
        for file in files:
            if not (file.startswith("0") and file.endswith(".md")):    
                continue 

            with open(SOURCE + file, "r") as f_read:
                lines = f_read.readlines()

            with open(BOOK_TARGET + file, "w") as f_write:
                for line in lines:
                    if line.startswith("![]"):
                        f_write.write("![](" + SOURCE + line[4:])
                    else:
                        f_write.write(line)
                f_write.write("\n\n")
                f_write.write("\\newpage")
                f_write.write("\n\n")   

        CHAPTERS = ["01_wu_jue", "02_wu_lv","03_qi_jue", "04_qi_lv", "05_ci_ling", "06_dui_lian", "07_other"]
        
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

        with open(chapter_folder + "/README.md", "r") as f_read:
            title = " ".join(f_read.readline().split(" ")[1:])

        with open(chapter_file, "a") as f_append:
            f_append.write("# " + "第" + CHAPTERS_CN[int(chapter.split("_")[0]) - 1] + "辑 " + title)           
            f_append.write("\n\n")
            f_append.write("\\vspace{4in}")
            f_append.write("\n\n")
            f_append.write("\\begin{center}")
            f_append.write("{\huge " + title + "}")
            f_append.write("\\end{center}")
            f_append.write("\n\n")
            f_append.write("\\newpage")
            f_append.write("\n\n")

            for file in files:

                if "README.md" in file:
                    continue

                f_append.write("#")

                with open(file, "r") as f_read:
                    lines = f_read.readlines()

                for line in lines:
                    if line.startswith("![]"):
                        f_append.write("![](" + chapter_folder + "/" + line[4:])
                    else:
                        f_append.write(line)

                f_append.write("\n\n")
                f_append.write("\\newpage")
                f_append.write("\n\n")  