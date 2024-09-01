import random
from moviepy.video.io.VideoFileClip import VideoFileClip
import moviepy.editor as mp
from pytube import YouTube

def download_main_video(video_id): #Broken for now
    path = "video_snippets"
    video_link = "youtube.com/watch?v=" + video_id
    
    yt = YouTube(video_link)
    d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    
    if d_video:
        d_video.download(output_path=path)
    else:
        print("No suitable stream found.")

def mini_video_creation(transcript, amount_of_clips):
    transcript = select_random_snippets(transcript, amount_of_clips)

    counter = 1
    for t_line in transcript:
        start_time = int(t_line['start'])
        end_time = start_time + int(t_line['duration'])
        create_snippet(counter, start_time, end_time)
        counter += 1
        
    return transcript

def select_random_snippets(transcript, amount_of_clips):
    random_snippets = []
    if amount_of_clips < len(transcript):
        for i in range(amount_of_clips):
            line = random.randint(0, len(transcript)-1)
            t_line = transcript.pop(line)
            random_snippets.append(t_line)
            
    return random_snippets       

def create_snippet(video_number, start_time, end_time):
    video_name = "video_snippets/" + str(video_number) + ".mp4"
    try:
        video = VideoFileClip("video_snippets/main.mp4")
        
        if end_time >= video.duration:
            end_time = video.duration
        
        cropped_video = video.subclip(start_time, end_time)
        cropped_video.write_videofile(video_name, codec="libx264", audio_codec="aac")
    except Exception as e:
        print(f"An error occurred: {e}")

def play_video(video_number):
    video_name = "video_snippets/" + str(video_number) + ".mp4"
    
    clip = mp.VideoFileClip(video_name)
    try:
        clip.preview(fullscreen=False)
    finally:
        clip.close()