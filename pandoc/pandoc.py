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
        shutil.copy("../src/xu.md",TARGET_FOLDER + "/01_xu.md")
        shutil.copy("../src/zi_xu.md",TARGET_FOLDER + "/02_zi_xu.md")
        shutil.copy("../src/ya_ge.md",TARGET_FOLDER + "/03_ya_ge.md")
        shutil.copy("../src/ya_ge.jpg",TARGET_FOLDER + "/ya_ge.jpg")
        shutil.copy("../src/word_cloud.md",TARGET_FOLDER + "/04_word_cloud.md")
        shutil.copy("../src/word_cloud.png",TARGET_FOLDER + "/word_cloud.png")

        CHAPTERS = ["05_wu_jue", "06_wu_lv","07_qi_jue", "08_qi_lv", "09_ci_ling", "10_other"]
    elif book == "modern_poems":
        CHAPTERS = ["01_nature", "02_solitude","03_wisdom", "04_homesick", "05_love", "06_birthday", "07_english"]
    elif book == "proses":
        CHAPTERS = ["01_politics", "02_econ_tech","03_life", "04_health", "05_fun", "06_wisdom", "07_poetry","08_wordgame"]
    else:    # book == "english"
        CHAPTERS = ["01_system", "02_tea"]

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



    

