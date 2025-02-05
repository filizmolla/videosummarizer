# Video Summarizer using Gemini

## About
This project is web project that takes youtube URL's and summarizes the youtube video using Gemini LLM. Project uses yt-dlp to download the video audios then uses whisper to transcribe the downloaded audios, then uses Gemini's Genai API to generate summaries from the transcripts. 

This project has two folders: 
1. summarizer 
2. sumarizer-web
summarizer is a Python app that manages the downloading, summarizing and an API that is listening to the Web Application. summarizer-web is the Web Application. When user enters a youtube url, the application sends a request to the API so that it can start summarizing. 

This project uses Django Web Framework which is a web framework for Python. Python FastAPI is used for the API. 

## Running 

### Getting Dependencies
Using pip: 
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### Database
1. Change the database connection to your database in the ``summarizer-web/mysite/settings.py`` change DATABASES variable. 
2. Change the database connection in the ``summarizer/videodb.py``.

3. Make migrations to create the database using the commands:
```
cd summarizer-web
python manage.py makemigrations
python manage.py migrate 
```

### Gemini API Key
1. Create a ``gemini-api-key.txt`` file in the ``summarizer`` folder and copy paste your Gemini API. 

### Start the Web Application and API   
To start the API: 
```
cd summarizer
python videoapi.py 
```

To start the web application: 
```
cd summarizer-web
python manage.py runserver  
```