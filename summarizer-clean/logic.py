from __future__ import annotations
from models import LLMModel, GemineModel, ChatGPTModel
import os 
import time
import json

from time import localtime, strftime
from datetime import datetime as PyDateTime


WORDS_PER_CHUNK = 50000 

class VideoSummaryRequest:

    def __init__(self, id, title, transcript):
        self.id = id
        self.title = title
        self.transcript = transcript

class SummaryResult:

    def __init__(self, title, summary_text):
        self.id = None #  Mapped[int] = mapped_column(primary_key=True)
        self.title = title #  Mapped[Optional[str]] 
        self.summary_text = summary_text #  Mapped[Optional[str]] = mapped_column(Text, nullable=True) 
        self.gpt_information = None #  Mapped[Optional[str]] = mapped_column(Text, nullable=True) 
        self.gpt_model_name = None #  Mapped[Optional[str]]
        self.gpt_input_token_count = None #  Mapped[Optional[int]]
        self.gpt_output_token_count = None #  Mapped[Optional[int]]
        self.summary_path = None #  Mapped[Optional[str]] 
        self.summary_start_date = None #  Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.summary_end_date = None #  Mapped[Optional[DateTime]] = mapped_column(DateTime, nullable=True)
        self.summary_time = None #  Mapped[Optional[int]] 
        self.summary_token_count = None #  Mapped[Optional[int]]
        self.summary_word_count = None #  Mapped[Optional[int]]
        self.summary_char_count = None #  Mapped[Optional[int]]
        self.created_at = None #  Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), nullable=False)
        self.updated_at = None #  Mapped[Optional[DateTime]] = mapped_column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
        self.video_id = None #  Mapped[int] = mapped_column(ForeignKey("videos_video.id"))

    def __str__(self):
        return self.summary_text

class VideoSummaryResponse:

    def __init__(self):
        self.transcript_word_count: int = None
        self.transcript_character_count:int = None
        self.transcript_token_count:int = None
        self.transcript_chunks: list[str] = None
        self.summary: SummaryResult = None
        self.is_summarized: bool = False
        self.status: str = None

    def setTranscriptWordCount(self, transcript_word_count):
        self.transcript_word_count = transcript_word_count

    def setTranscriptCharacterCount(self, transcript_character_count):
        self.transcript_character_count = transcript_character_count

    def setTranscriptTokenCount(self, transcript_token_count):
        self.transcript_token_count = transcript_token_count

    def setSummary(self, summary):
        self.summary = summary

    def setIsSummarized(self, is_summarized):
        self.is_summarized = is_summarized

    def setStatus(self, status):
        self.status = status


# Objeyi oluştururken dışarıdan LLM model alacak
# Verilen video title ve transcript için summary oluştur
class VideoSummarizer:

    PATH = os.getcwd()
    notes_path = PATH + "\\test videos\\output\\notes"
    
    USER_PROMPT = """
    Please Present this transcript in a more readable manner using lists, bullet points etc.
    Highlight any any actionable advice, references to research, examples, or specific techniques mentioned.
    Please use the exact sentences creator uses in the video. Use the language creator uses in their video. 
    Avoid phrases like "this video summarises", "creator says" just present the information in the video from a third person point of view.  
    Please present the information in the same order as the creator of the video. 
    Do not miss any point or information. 
    Do not leave out information such as definitions, explanations, interesting facts or words that are out of the ordinary, key concepts, main points, and valuable insights presented. 

    Title:
    \"""{title}\"""
    Script:
    \"""{transcript}\"""
    """

    def __init__(self, llm_model: LLMModel):
        self.llm_model = llm_model

    def summarize(self, request: VideoSummaryRequest) -> VideoSummaryResponse:
        start_time = time.time()
        response = VideoSummaryResponse()
        print("#######################################")
        prompt = self.USER_PROMPT.format(title=request.title, transcript=request.transcript)
        word, char, token = self.get_text_information(prompt)
        response.transcript_word_count = word # video.prompt_word_count? 
        response.transcript_character_count = char 
        response.transcript_token_count = token
        # TODO: The maximum number of api calls for a minute is 15. So i need to make sure  transcript word count / words_per_chunk < 15 

        if response.transcript_word_count < WORDS_PER_CHUNK:
            llm_response = self.llm_model.generateContent(prompt)
            summary = llm_response.text
        # else:
        #     transcript_chunks = self.split_text_by_words(video.transcript, WORDS_PER_CHUNK) # split the transcript into chunks!   
        #     for chunk in transcript_chunks: 
        #         print(chunk[:100])
        #         print("\n")
        #     response.transcript_chunks = transcript_chunks
        #     summaries = [self.get_summary(video, chunk) for chunk in transcript_chunks] # get summary of each chunk! 
        #     final_summary = " ".join(summaries)
        #     summary = final_summary

        end_time = time.time()
        summary_time = end_time - start_time 
        note_filename = self.notes_path + "\\" + request.title + ".txt" 
        # self.save_summary(summary, note_filename)
            
        s = SummaryResult(title=request.title, summary_text=summary)
        s.summary_time = summary_time 
        s.gpt_model_name = self.llm_model.model_name
        
        gpt_info = self.llm_model.getModelInfo()
        s.gpt_information = gpt_info

        word, char, token = self.get_text_information(summary)
        s.summary_word_count = word 
        s.summary_char_count = char
        s.summary_token_count = token 

        start_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(start_time))
        s.summary_start_date = PyDateTime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
        end_time_str = strftime('%Y-%m-%d %H:%M:%S', localtime(end_time))
        s.summary_end_date = PyDateTime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
        s.summary_path = note_filename
        response.summary = s
        response.is_summarized = True
        response.status = "Done."
        return response

    def get_text_information(self, text):
        word_count = len(text.split())
        char_count = len(text)
        token_count = self.llm_model.countTokens(text=text)
        return word_count, char_count, token_count


class VideoChunkSummarizer:
    USER_PROMPT = """
    Please Present this transcript part in a more readable manner using lists, bullet points etc.
    Highlight any any actionable advice, references to research, examples, or specific techniques mentioned.
    Please use the exact sentences creator uses in the video. Use the language creator uses in their video. 
    Avoid phrases like "this video summarises", "creator says" just present the information in the video from a third person point of view.  
    Please present the information in the same order as the creator of the video. 
    Do not miss any point or information. 
    Do not leave out information such as definitions, explanations, interesting facts or words that are out of the ordinary, key concepts, main points, and valuable insights presented. 

    Title:
    \"""{title}\"""
    Script:
    \"""{transcript}\"""
    """
    
    def __init__(self, llm_model: LLMModel):
        self.llm_model = LLMModel


    def summarize(self, request: VideoSummaryRequest) ->VideoSummaryResponse:
        pass 

class VideoChunkSummaryCombiner:
    USER_PROMPT = """
    Please combine this given transcript summary of same transcript with .
    Highlight any any actionable advice, references to research, examples, or specific techniques mentioned.
    Please use the exact sentences creator uses in the video. Use the language creator uses in their video. 
    Avoid phrases like "this video summarises", "creator says" just present the information in the video from a third person point of view.  
    Please present the information in the same order as the creator of the video. 
    Do not miss any point or information. 
    Do not leave out information such as definitions, explanations, interesting facts or words that are out of the ordinary, key concepts, main points, and valuable insights presented. 

    Title:
    \"""{title}\"""
    Script:
    \"""{transcript}\"""
    """
    
    def __init__(self, llm_model: LLMModel, transcript_chunks):
        self.llm_model = LLMModel
        self.transcript_chunks = transcript_chunks 

class TextSplitter: 

    def __init__(self, text, words_per_chunk):
        self.text = text
        self.words_per_chunk = words_per_chunk

    def split_text(self):
        words = self.text.split()
        chunks = [" ".join(words[i:i + self.words_per_chunk]) for i in range(0, len(words), self.words_per_chunk)]
        return chunks


if __name__ == "__main__":
    splitter = TextSplitter("Bu bir örnek metindir ve parçalara bölünecektir.", 2)
    chunks=splitter.split_text()
    print(chunks)


    splitter = TextSplitter("Bu bir örnek metindir ve parçalara bölünecektir.", 6)
    chunks=splitter.split_text()
    print(chunks)