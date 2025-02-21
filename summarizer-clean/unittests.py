from __future__ import annotations
from models import GemineModel
import unittest
from logic import VideoSummarizer, VideoSummaryRequest
import unittest

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
 

class Test_GemineModel(unittest.TestCase):

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

        self.assertIn("ResourceExhausted", str(result.summary.summary_text))
        self.assertIn("Fluid", str(result.summary.summary_text))
        self.assertIn("Flexbox", str(result.summary.summary_text))
        self.assertIn("MDN", str(result.summary.summary_text))
        # self.assertEqual(type(result.exception).__name__, "InvalidArgument")
                
if __name__ == '__main__':
     unittest.main()
