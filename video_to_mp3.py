# Converts videos to mp3
import os
import subprocess

files = [file for file in os.listdir("videos") if not file.startswith(".")]

for file in files:
    print(file)
    tutorial_num = file.split("#")[1].split(".")[0]
    tutorial_title = file.split(" _ ")[0]
    print(tutorial_num, tutorial_title)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{tutorial_num}_{tutorial_title}.mp3"])