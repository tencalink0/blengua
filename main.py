#from flask import Flask
from transcript import get_transcripts, create_local_copy, read_local_copy
from video import download_main_video, mini_video_creation, select_random_snippets, create_snippet, play_video

import time, json, os

def clean_videos():
    for filename in os.listdir("video_snippets"):
        if filename != "main.mp4":
            os.remove(os.path.join("video_snippets", filename))

#Parameters to mess with:
video_id = "aZTUJm8O2Ds"
languages = ['el']
amount_of_clips = 5
question_msg = "τι ειπε;" 

clean_videos()

file_name = "local_copy.txt"
#transcript = get_transcripts(video_id, languages)
#create_local_copy(transcript, file_name)
transcript = read_local_copy(file_name)
    
new_transcript = mini_video_creation(transcript, amount_of_clips)

video_count = 1
while video_count <= amount_of_clips:
    play_video(video_count)
    time.sleep(0.2)
    unfinished = True
    while unfinished:
        user_input = input(question_msg)
        print(new_transcript[video_count-1]['text'])
        
        user_input = input()
        if user_input.strip() == "1":
            unfinished = False
        else:
            play_video(video_count)
        
    video_count += 1