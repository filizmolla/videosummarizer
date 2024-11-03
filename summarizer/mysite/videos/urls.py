from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.IndexView.as_view(), name="Index"),
    path("videos", views.VideoTableView.as_view(), name="Video Table"),
    path("videolar", views.VideoTabloView.as_view(), name="Video Tablosu"),
    path("videos/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add_video', views.add_video, name='add_video')
]