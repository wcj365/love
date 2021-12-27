import pandoc   
from glob import glob
import shutil

source_files = glob("src/00*")

for source in source_files:
    target = "_pandoc/01_classic_poems/" + source.split("/")[-1]
    if not source.endswith("md"):
        shutil.copyfile(source, target)   
    else:
        with open(source, "r") as f_read:
            lines = f_read.readlines()
        with open(target, "w") as f_write:
            if not lines[0].startswith("# "):
                f_write.write("# ")
            pandoc.process_lines(f_write, lines, "src/")