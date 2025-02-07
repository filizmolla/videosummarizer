import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin
from pgvector.django import VectorField

class Video(models.Model):
    url = models.CharField()
    title = models.CharField(null=True)
    ext = models.CharField(null=True)
    title_with_ext = models.CharField(null=True)
    description = models.CharField(null=True)
    channel_name = models.CharField(null=True)
    channel_url = models.CharField(null=True)
    upload_date_youtube = models.DateTimeField("Date published on YouTube", null=True)
    duration = models.IntegerField(null=True)
    view_count = models.IntegerField(null=True)
    like_count = models.IntegerField(null=True)
    categories = models.CharField(null=True)
    tags = models.CharField(null=True)

    audio_path = models.CharField(null=True)
    subtitles = models.CharField(null=True)
    transcript = models.CharField(null=True)
    transcript_path = models.CharField(null=True)
    transcript_from = models.CharField(null=True)
    transcript_word_count = models.IntegerField(null=True)
    transcript_token_count = models.IntegerField(null=True)
    transcript_character_count = models.IntegerField(null=True)
    transcript_chunks = models.CharField(null=True)
    transcript_embedding = VectorField(dimensions=1536, null=True)

    date_uploaded = models.DateTimeField(null=True)
    download_start_datetime = models.DateTimeField(null=True)
    download_end_datetime = models.DateTimeField(null=True)
    download_time = models.IntegerField(null=True)
    transcribing_start_date = models.DateTimeField(null=True)
    transcribing_end_date = models.DateTimeField(null=True)
    transcribing_time = models.IntegerField(null=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_summarized = models.BooleanField(default=False)
    is_transcribed = models.BooleanField(default=False)
    status = models.CharField(default="Pending")

    playlist_id = models.CharField(null=True)
    playlist_order = models.IntegerField(null=True)
    is_in_playlist = models.BooleanField(null=True)

    def __str__(self):
        return self.url
        
class Summary(models.Model): 
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    title = models.CharField(null=True)
    summary_text = models.CharField(null=True)
    gpt_information = models.CharField(null=True)
    gpt_model_name = models.CharField(null=True)
    gpt_input_token_count = models.IntegerField(null=True)
    gpt_output_token_count = models.IntegerField(null=True) 

    summary_path = models.CharField(null=True)
    summary_start_date = models.DateTimeField(null=True)
    summary_end_date = models.DateTimeField(null=True)
    summary_time = models.IntegerField(null=True)
    summary_token_count = models.IntegerField(null=True)
    summary_word_count = models.IntegerField(null=True)
    summary_char_count = models.IntegerField(null=True)

    created_at = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Summary of" + self.title  
