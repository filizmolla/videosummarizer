from __future__ import annotations
from abc import ABC, abstractmethod
import google.generativeai as genai 
from abc import ABC, abstractmethod
import google.generativeai as genai 
from openai import OpenAI
import os 
import tiktoken 
import json

#class LLMCompletionUsage:
#    
#    def __init__(self, completion_tokens=0, prompt_tokens=0, total_tokens=0 ):
#        self.completion_tokens = completion_tokens
#        self.prompt_tokens = prompt_tokens 
#        self.total_tokens = total_tokens 
#
#    def __str__(self):
#        return "Response token count:" + self.completion_tokens + " Prompt token count:" + self.prompt_tokens + " Sum:" + self.total_tokens

class LLMModelResponse:

    def __init__(self, text, is_successful = True, exception = None, completion_tokens=0, prompt_tokens=0, total_tokens=0):
        self.text = text
        self.is_successful = is_successful
        self.exception = exception
        self.completion_tokens = completion_tokens
        self.prompt_tokens = prompt_tokens 
        self.total_tokens = total_tokens 

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
        ct = self.client.count_tokens(text)
        token_count = ct.total_tokens
        return token_count

    def getModelName(self):
        return self.model_name
    
    def getModelInfo(self):
        gpt_info = genai.get_model(f"models/{self.model_name}")
        gpt_information = json.dumps(gpt_info.__dict__)
        gpt_input_token_count = gpt_info.input_token_limit
        gpt_output_token_count = gpt_info.output_token_limit 
        return "GPT info: " + str(gpt_information) + " GPT Input Token Count: " + str(gpt_input_token_count) + " GPT Output Token Count: " + str(gpt_output_token_count)

class ChatGPTModel(LLMModel):

    def __init__(self, model_name = "gpt-4o", temperature=0.7):
        self.model_name = model_name
        self.client = None
        self.temperature = temperature

    def setApiKey(self, api_key):
        self.client =  OpenAI(api_key=api_key)

    def setTemperature(self, temperature):
        self.temperature = temperature

    def generateContent(self, prompt, system_prompt="You are a helpful assistant."):
        completion = self.client.chat.completions.create(
        model=self.model_name,
            messages=[
                {"role": "system", "content": f"{system_prompt}"},
                {"role": "user", "content": f"{prompt}"}
            ],
            temperature=self.temperature,
        )
        return LLMModelResponse(completion.choices[0].message.content, completion_tokens=completion.usage.completion_tokens, prompt_tokens=completion.usage.prompt_tokens, total_tokens=completion.usage.total_tokens)

    def countTokens(self, text):
        enc = tiktoken.encoding_for_model(self.model_name)
        tokens = enc.encode(text)
        return len(tokens)

    def getModelName(self):
        return self.model_name

    def getModelInfo(self):
        return self.client.models.retrieve(self.model_name)

class OllamaModel(LLMModel):

    def __init__(self, model_name = "llama3.1", temperature= 0.7):
        self.model_name = model_name
        self.client = None
        self.temperature = temperature

    def setApiKey(self, api_key, base_url="http://127.0.0.1:11434/v1"):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
    
    def setTemperature(self, temperature):
        self.temperature = temperature

    def generateContent(self, prompt, system_prompt="You are a helpful assistant."):
        completion = self.client.chat.completions.create(
        model=self.model_name,
            messages=[
                {"role": "system", "content": f"{system_prompt}"},
                {"role": "user", "content": f"{prompt}"}
            ],
            temperature=self.temperature,
        )
        return LLMModelResponse(completion.choices[0].message.content, completion_tokens=completion.usage.completion_tokens, prompt_tokens=completion.usage.prompt_tokens, total_tokens=completion.usage.total_tokens)
    
    def countTokens(self, text):
        tiktoken.model.MODEL_TO_ENCODING["llama3.1"] = "cl100k_base"
        enc = tiktoken.encoding_for_model(self.model_name)
        tokens = enc.encode(text)
        return len(tokens)

    def getModelName(self):
        return self.model_name

    def getModelInfo(self):
        return self.client.models.retrieve(self.model_name)


class EmbedingModel(ABC):

    @abstractmethod
    def getEmbedingVector(self, text):
        pass


if __name__ =="__main__": 
    gpt_model = ChatGPTModel()
    gpt_model.setApiKey(os.getenv("OPENAI_API_KEY"))
    result = gpt_model.generateContent(prompt="tell me a joke about artificial intelligence")
    print(result.text)
    print(result.response_token_count)
    print(gpt_model.countTokens(result.text))
    print(gpt_model.getModelName())
    print(gpt_model.getModelInfo())


    llama = OllamaModel()
    llama.setApiKey(api_key="ollama")
    result= llama.generateContent(prompt="tell me a joke about aliens")
    print(result.text)
    print(llama.countTokens(result.text))
    print(result.response_token_count)
    print(llama.getModelName())
    print(llama.getModelInfo())