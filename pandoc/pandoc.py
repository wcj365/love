#!/usr/bin/env python3

import glob
import os
import shutil

books = ["classic_poems", "modern_poems", "proses", "english"]

for book in books:

    SOURCE_FOLDER = f"../src/{book}"
    TARGET_FOLDER = f"./{book}"

    if os.path.exists(TARGET_FOLDER):
        shutil.rmtree(TARGET_FOLDER) 

    os.mkdir(TARGET_FOLDER) 

    shutil.copy(f"00_{book}.md",f"{TARGET_FOLDER}/00_{book}.md")
    shutil.copy("Makefile",TARGET_FOLDER + "/Makefile")

    if book == "classic_poems":
        files = os.listdir("../src/")
        for file in files:
            if not file.startswith("0"):
                continue      
            shutil.copy("../src/" + file,TARGET_FOLDER)
            if file.endswith(".md"):
                with open(TARGET_FOLDER + file, "a") as f_append:
                    f_append.write("\n\n")
                    f_append.write("\\newpage")
                    f_append.write("\n\n")   

        CHAPTERS = ["05_wu_jue", "06_wu_lv","07_qi_jue", "08_qi_lv", "09_ci_ling", "10_other"]
        
    elif book == "modern_poems":
        CHAPTERS = ["01_nature", "02_solitude","03_wisdom", "04_homesick", "05_love", "06_birthday", "07_english"]
    elif book == "proses":
        CHAPTERS = ["01_politics", "02_econ_tech","03_life", "04_health", "05_fun", "06_wisdom", "07_poetry","08_wordgame"]
    else:    # book == "english"
        CHAPTERS = ["01_academic", "02_system", "03_tea"]

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