from __future__ import annotations
from models import GemineModel, ChatGPTModel, OllamaModel
from logic import VideoSummarizer, VideoSummaryRequest, TextSplitter
from downloader import VideoResult, VideoDownloader
import unittest
import os 
import pathlib as pl 
import datetime
"""
class Test_GemineModel(unittest.TestCase):

    def setUp(self):
        self.api_key = "AIzaSyDon9tlna2EgPfq34jVFiC7IoWvW6KZZww"

    def test_gemini_is_reponse_pass(self):
        model = GemineModel()
        model.setApiKey(self.api_key)
        result = model.generateContent("Hello")
        print(result.text)

    def test_gemini_is_reponse_failed(self):
        model = GemineModel()
        model.setApiKey(f"{self.api_key}wrong_api_key")
        result = model.generateContent("Hello")
        print(result.text)

        self.assertIn("API key not valid.", str(result.exception))
        self.assertEqual(type(result.exception).__name__, "InvalidArgument")
 

class Test_GeminiModel(unittest.TestCase):

    def setUp(self):

        self.gemini_model = GemineModel()
        self.gemini_model.setApiKey("AIzaSyDon9tlna2EgPfq34jVFiC7IoWvW6KZZww")


    def test_gemini_is_reponse_pass(self):
        title = "My favorite resources and tools for coding"
        filename = f".\\..\\summarizer\\test videos\\output\\transcripts\\{title}.txt"
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


class Test_ChatGPTModel(unittest.TestCase):
    
    def setUp(self):
        self.chatgpt_model =  ChatGPTModel()
        self.chatgpt_model.setApiKey(os.getenv("OPENAI_API_KEY"))

    def test_ollama_is_response_pass(self):
        title = "My favorite resources and tools for coding"
        filename = f".\\..\\summarizer\\test videos\\output\\transcripts\\{title}.txt"
        transcript = ""
        with open(filename, 'r') as f:
            transcript = f.read()

        summarizer = VideoSummarizer(llm_model=self.chatgpt_model)

        request = VideoSummaryRequest(id = "123", title = filename, transcript=transcript)
        result = summarizer.summarize(request)
        print(result.summary.summary_text)

        self.assertIn("Fluid", str(result.summary.summary_text))
        self.assertIn("Flexbox", str(result.summary.summary_text))
        self.assertIn("MDN", str(result.summary.summary_text))
        self.assertIn("Google Web Fonts Helper", str(result.summary.summary_text))

    def test_chatgpt_response_assistant(self):
        result = self.chatgpt_model.generateContent("Who are you?", system_prompt="You are a helpful assistant, this is who you are.")
        print(result.text) 
        self.assertIn("assistant", str(result.text))

    #def test_chatgpt_response_assistant_fail(self):
    #    self.chatgpt_model.setApiKey("wrong")
    #    result = self.chatgpt_model.generateContent("Who are you?", system_prompt="You are a helpful assistant, this is who you are.")
    #    print(result.text) 
    #    self.chatgpt_model.setApiKey(os.getenv("OPENAI_API_KEY"))
    #    self.assertIn("API key not valid.", str(result.exception))
    #    self.assertEqual(type(result.exception).__name__, "openai.AuthenticationError")

    def test_chatgpt_count_tokens_pass(self):
        pass

    def test_chatgpt_get_model_name_pass(self):
        pass 

    def test_chatgpt_get_model_info_pass(self):
        pass 

#class Test_OllamaModel(unittest.TestCase):
#   
#   def setUp(self):
#       self.ollama_model =  OllamaModel()
#       self.ollama_model.setApiKey(api_key="ollama")
#    
#    # Output is not good! Tests are failing  
#   def test_ollama_is_response_pass(self):
#       title = "My favorite resources and tools for coding"
#       filename = f".\\..\\summarizer\\test videos\\output\\transcripts\\{title}.txt"
#       transcript = ""
#       with open(filename, 'r') as f:
#           transcript = f.read()
#
#       summarizer = VideoSummarizer(llm_model=self.ollama_model)
#
#       request = VideoSummaryRequest(id = "123", title = filename, transcript=transcript)
#       result = summarizer.summarize(request)
#       print(result.summary.summary_text)
#
#       #self.assertIn("Fluid", str(result.summary.summary_text))
#       self.assertIn("Google Web Fonts Helper", str(result.summary.summary_text))
#       #self.assertIn("Flexbox", str(result.summary.summary_text))
#       #self.assertIn("MDN", str(result.summary.summary_text))
 
class Test_VideoDownloader(unittest.TestCase):
    
    def setUp(self):
        self.path = "C:\\workdir\\pkm\\summarizer\\test videos\\output\\audios\\Kung Fu Fighting.m4a"
        if os.path.exists(self.path):
            os.remove(self.path)
            print("Deleted existing file.\n")
        else:
            print("The file does not exist.\n") 

    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

    def test_if_downloader_downloads(self):
        video = VideoResult("https://www.youtube.com/watch?v=QspjKVTMlL8")
        downloader = VideoDownloader(video)
        videoresult = downloader.download_video()

        pl_path = pl.Path(self.path)
        self.assertIsFile(pl_path)
        self.assertEqual(videoresult.title, "Kung Fu Fighting")
        self.assertEqual(videoresult.title_with_ext, "Kung Fu Fighting.m4a")
        self.assertEqual(videoresult.ext, "m4a")
        self.assertEqual(videoresult.url, "https://www.youtube.com/watch?v=QspjKVTMlL8")
        self.assertIn("Provided to YouTube by Universal Music Group", videoresult.description)
        self.assertEqual("CeeLo Green", videoresult.channel_name)
        self.assertEqual("https://www.youtube.com/channel/UCQlJSs4QNKLLt1sHgRXkVYg", videoresult.channel_url)
        self.assertEqual(datetime.datetime(2019, 1, 31, 0, 0), videoresult.upload_date_youtube)
        self.assertEqual(150, videoresult.duration)
        self.assertEqual(r"C:\workdir\pkm\summarizer\test videos\output\audios\Kung Fu Fighting.m4a", videoresult.audio_path)

    #def test_if_wrong_link_fail(self): #anlamadım
    #    video = VideoResult("https://www.youtube.com/watch?v=WRONG")
    #    downloader = VideoDownloader(video)
    #    videoresult = downloader.download_video()
    #    print(videoresult)
    #    self.assertEqual(type(videoresult.exception).__name__, "UnboundLocalError: local variable 'title_with_ext' referenced before assignment")
"""

class Test_TextSplitter(unittest.TestCase):

    def setUp(self):
        return super().setUp()
    
    def test_split_sentence_wordsperchunk_is_two(self):
        splitter = TextSplitter("Bu bir örnek metindir ve parçalara bölünecektir.", 2)
        chunks=splitter.split_text()
        print(chunks)
        self.assertIsInstance(chunks, list)
        self.assertEqual(chunks[0], "Bu bir")
        self.assertEqual(chunks[1], "örnek metindir") 
        self.assertEqual(chunks[2], "ve parçalara")
        self.assertEqual(chunks[3], "bölünecektir.")

    def test_split_sentence_wordsperchunk_is_six(self):
        splitter = TextSplitter("Bu bir örnek metindir ve parçalara bölünecektir.", 6)
        chunks=splitter.split_text()
        print(chunks)
        self.assertIs(type(chunks), list)
        self.assertEqual(chunks[0], "Bu bir örnek metindir ve parçalara")
        self.assertEqual(chunks[1], "bölünecektir.")

if __name__ == '__main__':
     unittest.main()
