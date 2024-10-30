from __future__ import annotations
import os 
from openai import OpenAI
import time 
from time import localtime, strftime
from datetime import datetime as PyDateTime
from models import Video, Summary, Base


exit()

class Summarizer:
    PATH = os.getcwd()
    notes_path = PATH + "\\output\\pdfchapters"
   
    client =  OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    system_prompt = """"""
    user_prompt = """
    Please summarize this text.
    Text:
    \"""{text}\"""
    """

    def __init__(self, video: Video, pdfdocument: PDFDocument):
        self.video = video
        self.pdfdocument = pdfdocument

    def start(self):
        self.summarize(self.video)

    def summarize(self, video: Video, pdfdocument: PDFDocument):
        start_time = time.time()
        completion = self.client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": self.user_prompt.format(title=video.title, transcript=video.transcript)}
        ],
        temperature=0.1,
        )

        summary = completion.choices[0].message.content
        end_time = time.time()
        summary_time = end_time - start_time 
        note_filename = self.notes_path + "\\" + video.title + ".txt" 
        self.save_summary(summary, note_filename)
            
        s = Summary(title=video.title, summary_text=summary)
        s.summary_time = summary_time 
        s.gpt_information = completion.model

        start_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))
        s.summary_start_date = PyDateTime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        end_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
        s.summary_end_date = PyDateTime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        s.summary_path = note_filename
        video.summaries.append(s)
        video.is_summarized = True
        video.status = "Done."
        
        return summary

    def save_summary(self, summary_text, note_filename):
        with open(note_filename, "w", encoding="utf-8") as file: 
            file.write(summary_text) 

        print(f"Note saved to {note_filename}")
