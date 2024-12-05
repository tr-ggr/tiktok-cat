from moviepy.editor import *
from os import walk
import os
    
files = []
directory = "pinterest"
sfx_audio = AudioFileClip("./audios/myloveisallmine_spedup.mp3")

ctr = 0
result_name = f"part{ctr}.mp4"

def getResultName():
    global ctr, result_name
    DIR = os.listdir('.')

    print(DIR)
    
    for directory in DIR:
        if directory.startswith("part"):
            ctr+=1

    result_name = f"part{ctr+1}.mp4"

def getFileNames():
    for (dir_path, dir_names, file_names) in walk(f"./raw_videos/{directory}"):
        files.extend(file_names[:int(sfx_audio.duration//3) + 1])
        # files.extend(file_names[:13])


def createVideo():
    global sfx_audio
    clips = []

    for file in files:
        print(f"Starting {file}")
        clip = VideoFileClip(f"./raw_videos/{directory}/{file}", target_resolution=(1080,1920))
        # clip = clip.without_audio()
        clip = clip.fx(vfx.multiply_speed, 2)
        clip = clip.subclip(0,3)
        clips.append(clip)
        print(f"Done {file}")
    
    final_clip = concatenate_videoclips(clips, method='compose')
    final_clip = final_clip.subclip(0, sfx_audio.duration)
    new_audioclip = CompositeAudioClip([sfx_audio])
    final_clip.audio = new_audioclip
    final_clip.write_videofile(f"{result_name}")

def cleanFiles():
    for file in files:
        os.remove(f"./raw_videos/{directory}/{file}")

def createMagic():
    print("Getting File names...")
    getFileNames()
    getResultName()
    
    print("Done getting Files")

    print(f"creating video {result_name}")
    createVideo()
    print(f"done creating {result_name}")

    
    print("Done creating video!")

    # Clean
    print("Cleaning files...")
    cleanFiles()
    print("Done cleaning files!")


if __name__ == '__main__':
    createMagic()

