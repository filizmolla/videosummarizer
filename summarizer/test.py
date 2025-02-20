from __future__ import annotations
import unittest
import os 
from abc import ABC, abstractmethod
import google.generativeai as genai 
import time
import json

from time import localtime, strftime
from datetime import datetime as PyDateTime


class LLMModelResponse:

    def __init__(self, text, is_successful = True, exception = None):
        self.text = text
        self.is_successful = is_successful
        self.exception = exception

    def __str__(self):
        return self.text

class LLMModel(ABC):
    
    @abstractmethod
    def setApiKey(self, api_key):
        pass

    @abstractmethod
    def generateContent(self, prompt):
        pass

    @abstractmethod
    def countTokens(self, text):
        pass

    @abstractmethod
    def getModelName(self):
        pass

    @abstractmethod
    def getModelInfo(self):
        pass

class GemineModel(LLMModel):

    def __init__(self, model_name = "gemini-pro"):
        self.model_name = model_name 
        self.client = genai.GenerativeModel(model_name)

    def setApiKey(self, api_key):
        genai.configure(api_key=api_key)

    def generateContent(self, prompt):
        try: 
            response = self.client.generate_content(prompt)
            return LLMModelResponse(response.text)
        except Exception as e:
            return LLMModelResponse(f"Unexpected error: {repr(e)}", False, e)

    def countTokens(self, text):
        return self.client.count_tokens(text)

    def getModelName(self):
        return self.model_name
    
    def getModelInfo(self):
        return genai.get_model(f"models/{self.model_name}") 

class OllamaModel(LLMModel):

    def __init__(self, model_name = "llama3.1"):
        self.model_name = model_name


class Test_GemineModel(unittest.TestCase):

    def setUp(self):
        self.api_key = "AIzaSyDon9tlna2EgPfq34jVFiC7IoWvW6KZZww"

    def test_gemini_is_reponse_pass(self):
        model = GemineModel()
        model.setApiKey(self.api_key)
        result = model.generateContent("Hello")
        print(result.text)

    # def test_gemini_is_reponse_failed(self):
    #     with self.assertRaises(Exception) as context:
    #         model = GemineModel()
    #         model.setApiKey(f"{self.api_key}wrong_api_key")
    #         result = model.generateContent("Hello")
    #         print(result.text)
    #     self.assertIn("API key not valid.", str(context.exception))
    #     self.assertEqual(type(context.exception).__name__, "InvalidArgument")

    def test_gemini_is_reponse_failed(self):
        model = GemineModel()
        model.setApiKey(f"{self.api_key}wrong_api_key")
        result = model.generateContent("Hello")
        print(result.text)

        self.assertIn("API key not valid.", str(result.exception))
        self.assertEqual(type(result.exception).__name__, "InvalidArgument")

# if __name__ == '__main__':
#     unittest.main()




# ------------------------



class EmbedingModel(ABC):

    @abstractmethod
    def getEmbedingVector(self, text):
        pass




# ------------------------

WORDS_PER_CHUNK = 50000 #800

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
        s.gpt_information = json.dumps(gpt_info.__dict__)
        s.gpt_input_token_count = gpt_info.input_token_limit # not that necessary?
        s.gpt_output_token_count = gpt_info.output_token_limit
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
        ct = self.llm_model.countTokens(text=text)
        token_count = ct.total_tokens
        return word_count, char_count, token_count













class Test_GemineModel(unittest.TestCase):

    def setUp(self):

        self.gemini_model = GemineModel()
        self.gemini_model.setApiKey("AIzaSyDon9tlna2EgPfq34jVFiC7IoWvW6KZZww")


    def test_gemini_is_reponse_pass(self):
        title = "My favorite resources and tools for coding"
        filename = f".\\test videos\\output\\transcripts\\{title}.txt"
        transcript = ""
        with open(filename, 'r') as f:
            transcript = f.read()

        summarizer = VideoSummarizer(llm_model=self.gemini_model)

        request = VideoSummaryRequest(id = "123", title = filename, transcript=transcript)
        result = summarizer.summarize(request)
        print(result.summary.summary_text)

        self.assertIn("Fluid", str(result.summary.summary_text))
        self.assertIn("Flexbox", str(result.summary.summary_text))
        self.assertIn("MDN", str(result.summary.summary_text))
        # self.assertEqual(type(result.exception).__name__, "InvalidArgument")

if __name__ == '__main__':
    unittest.main()











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
    
class VideoChunkSumaryCombiner:
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
    
    def __init__(self, llm_model: LLMModel):
        self.llm_model = LLMModel
    



