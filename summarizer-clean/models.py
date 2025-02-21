from __future__ import annotations
from abc import ABC, abstractmethod
import google.generativeai as genai 
from abc import ABC, abstractmethod
import google.generativeai as genai 

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

class EmbedingModel(ABC):

    @abstractmethod
    def getEmbedingVector(self, text):
        pass
