from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from videos.models import Video
from videos.serializers import VideoSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
import requests


from django.http import HttpResponseRedirect
from django.shortcuts import render

from videos.forms import NameForm, VideoForm
import json

def add_video(request):
    submitted = False 
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            # TODO: Control if the input from user is a YouTube Video URL or not. 
            create_record_and_notify(request)  
            return HttpResponseRedirect('add_video?submitted=True')
    else:
        form = VideoForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'videos/add_video.html', {'form': form, 'submitted':submitted })


class IndexView(generic.ListView):
    template_name = "videos/index.html"
    context_object_name = "latest_video_list"

    def get_queryset(self):
        """    
        Return the last five created videos. 
        """
        return Video.objects.filter().order_by("-created_at")[:5]

class VideoTableView(generic.ListView):
    template_name = "videos/list.html"
    context_object_name = "video_list"

    def get_queryset(self):
        """    
        Return all the videos in the database.
        """
        return Video.objects.all()
    

class VideoTabloView(generic.ListView):
    template_name = "videos/liste.html"
    context_object_name = "video_list"

    def get_queryset(self) -> QuerySet[Video]:
        return Video.objects.all()
    
class DetailView(generic.DetailView):
    model = Video
    template_name = "videos/detail.html"

    def get_queryset(self):
        return Video.objects.all()

@api_view()
def view_dtl(request):
    return Response({'success': 409, 'message': 'api'})

@api_view(['POST'])
def create_record_and_notify(request):
    url = request.POST.get('url')
    print(url)

    python_app_url = "http://127.0.0.1:5000/notify_new_data"
    payload = {
        "url": url
    }

    try:
        response = requests.post(python_app_url, json=payload)
        response.raise_for_status()  
        return JsonResponse({"message": "Record created and Python app notified."}, status=201)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Failed to notify Python app: {str(e)}"}, status=500)


@api_view(['POST'])
def notify_app(request):
    python_app_url = "http://127.0.0.1:5000/notify_new_data"
    try:
        response = requests.post(python_app_url)
        response.raise_for_status()  
        return JsonResponse({"message": "Record created and Python app notified."}, status=201)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"Failed to notify Python app: {str(e)}"}, status=500)



