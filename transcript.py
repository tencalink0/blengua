from youtube_transcript_api import YouTubeTranscriptApi

import json

def get_transcripts(video_id, languages):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
    return transcript_list

def create_local_copy(transcript, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        transcript_string = ''
        for i in range(len(transcript)):
            t_line = transcript[i]
            if i >= len(transcript)-1:
                transcript_string += json.dumps(t_line, ensure_ascii=False)
            else:
                transcript_string += json.dumps(t_line, ensure_ascii=False) + ","
            
        file.write("[" + transcript_string + "]")

def read_local_copy(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = file.read()
        
    return json.loads(data)