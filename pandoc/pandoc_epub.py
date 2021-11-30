#!/usr/bin/env python3

import glob
import os
import shutil

SOURCE = "../src/"
TARGET = "../_pandoc_epub/"

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
            with open(BOOK_TARGET + file, "w") as f_write:
                with open(SOURCE + file, "r") as f_read:
                    lines = f_read.readlines()
                    for line in lines:
                        if line.startswith("![]"):
                            f_write.write("![](" + SOURCE + line[4:])
                        else:
                            f_write.write(line)
                    f_write.write("\n\n")
                    f_write.write("\\newpage")
                    f_write.write("\n\n")   

        SECTIONS = ["01_wu_jue", "02_wu_lv","03_qi_jue", "04_qi_lv", "05_ci_ling", "06_dui_lian", "07_other"]
        
    elif book == "modern_poems":
        SECTIONS = ["01_nature", "02_solitude","03_wisdom", "04_homesick", "05_love", "06_birthday", "07_english"]
    elif book == "proses":
        SECTIONS = ["01_politics", "02_econ_tech","03_life", "04_health", "05_fun", "06_wisdom", "07_poetry","08_wordgame"]
    else:    # book == "english"
        SECTIONS = ["01_academic", "02_system", "03_tea"]

    for section in SECTIONS:

        section_folder = BOOK_SOURCE + section[3:]
        files = glob.glob(section_folder + "/*.md")

        for file in files:

            if "README" in file:
                
                with open(file, "r") as f_read:
                    title = " ".join(f_read.readline().split(" ")[1:])

                with open(f"{BOOK_TARGET}{section}_00.md", "w") as f_write:
                    f_write.write("# " + "第" + CHAPTERS_CN[int(section.split("_")[0]) - 1] + "辑 " + title)
            else:
                with open(file, "r") as f_read:
                    lines = f_read.readlines()

                with open(f"{BOOK_TARGET}{section}_{file.split('/')[-1]}", "w") as f_write:

                    for line in lines:
                        if line.startswith("![]"):
                            f_write.write("![](" + section_folder + "/" + line[4:])
                        else:
                            f_write.write(line)

                    f_write.write("\n")
                        
