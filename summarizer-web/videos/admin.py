from django.contrib import admin

from .models import Video, Summary

class SummaryInline(admin.TabularInline):
    model = Summary 
    extra = 1

class VideoAdmin(admin.ModelAdmin):
    list_display = ["url","title" ,"created_at", "updated_at", "status"]
    fieldsets = [
        (None, {"fields": ["url"]}),
        #("Date information", {"fields": ["upload_date_youtube"]}),
    ]
    list_filter = ["upload_date_youtube"]  # kenardaki filter Any Date, Today etc.
    search_fields = ["title"] # adds search functionality 
    #inlines = [SummaryInline]

admin.site.register(Video, VideoAdmin)