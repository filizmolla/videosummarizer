from django.urls import path 

from . import views 

urlpatterns = [
    path("", views.IndexView.as_view(), name="Index"),
    path("videos", views.VideoTableView.as_view(), name="Video Table"),
    path("videolar", views.VideoTabloView.as_view(), name="Video_Tablosu"),
    path("videos/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('add_video', views.add_video, name='add_video'),
    path('delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('get_item_details/<int:item_id>/', views.get_item_details, name='get_item_details'),
    path('get_item_details_for_delete/<int:item_id>/', views.get_item_details_for_delete, name='get_item_details_for_delete'),
]