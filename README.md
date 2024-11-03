This project is web project that takes youtube URL's and summarizes the youtube video using Gemini LLM. Project uses whisper to transcribe the videos and Gemini's genai API the transcript is summarized. Project consists of two different apps one is a web app made with django that contains the frontend and the other is a python app that has FastAPI api. The user enters the url in the front end, than API sends app a request and url is sent to the python app to summarize. 

This project uses: Python, django web framework. 
Database: postgreSQL

## Running 
- To create a miniconda/conda environment for this project: 
```
conda create --name <env_name> --file requirements.txt
conda activate <env_name>
```

- Change the database connection to your database in the ``Summarizer/summarizer/mysite/settings.py`` change DATABASES variable. 
- Change the database connection in the videodb.py. 
- Make migrations to create the database using the commands.
```
cd Summarizer\summarizer\mysite
python manage.py makemigrations
python manage.py migrate 
```

To start the web application: 
```
cd Summarizer\summarizer\mysite
python manage.py runserver  
```

To start the API: 
```
cd Summarizer\app
python videoapi.py 
```