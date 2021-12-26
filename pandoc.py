#!/usr/bin/env python3

import os
import sys
import shutil
from glob import glob


def main(source_folder, target_folder):

    print(source_folder, "\n", target_folder)

    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)

    os.mkdir(target_folder)

    # 第一步 - 处理存在根文件夹下的内容（序，自序等)
    # 序，自序等的文件名要以001，002等开头。
    # 000保留给书的首页和目录

    shutil.copyfile(f"{source_folder}/_pandoc.md", f"{target_folder}/000_title_toc.md")     

    files = glob(f"{source_folder}/*.md")

    for file in files:
        if file.split("/")[-1].startswith("_"):    # 非内容的系统文件，比如 _toc.yml, _config.yml，_pandoc.md
            continue  
        elif file.split("/")[-1] == "index.md":    # 网站首页，不必加入电子版里
            continue
        elif file.split("/")[-1] == "00.md":    # 目录，不必加入电子版里
            continue
        else:
            target = target_folder + "/" + file.split("/")[-1]

            with open(file, "r") as f:
                lines = f.readlines()

            with open(target, "w") as f:
                if not lines[0].startswith("# "):
                    f.write("# ")

                for line in lines:
                    if line.startswith("!["):           # 图像
                        f.write(line.split("]")[0] + "](" + f"{source_folder}/" + line.split("]")[1].lstrip("("))
                    else:
                        f.write(line)

                f.write("\n\n")
                f.write("\\newpage")
                f.write("\n\n")

    # 第二步 - 处理存于子文件夹下的正文（各辑，各章)

    folders = glob(f"{source_folder}/*/")


    for folder in folders:
        print(folder)
        if "/_static/" in folder:           # 非内容的网站静态文件存于此文件夹
            continue
        files = glob(folder + "*.md")
        files.sort()
        if not folder + "00.md" in files:   # 存放内容的子文件夹必须有一个 00.md 文件作为该辑的目录
            continue
        chapter_file = folder.split("/")[:2] + "/" + folder.split("/")[2] + ".md"
        print("chapter file:", chapter_file)
        if os.path.exists(chapter_file):
            os.remove(chapter_file)
        with open(chapter_file, "a") as f_append:
            for file in files:
                with open(file, "r") as f_read:
                    if not "00.md" in file:
                        f_append.write("#")
                    lines = f_read.readlines()
                    for line in lines:
                        if line.startswith("!["):
                            f_append.write(line.split("]")[0] + "](" + folder + line.split("]")[1].lstrip("("))
                        else:
                            f_append.write(line)
                    f_append.write("\n\n")
                    f_append.write("\\newpage")
                    f_append.write("\n\n")



if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])