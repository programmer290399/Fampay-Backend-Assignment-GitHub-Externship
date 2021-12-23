from django.contrib import admin

# Register your models here.
from youtube_rest_api.models import Video


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)
