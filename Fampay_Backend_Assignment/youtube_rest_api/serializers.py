from rest_framework import serializers
from youtube_rest_api.models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "video_title",
            "description",
            "published_on",
            "thumb_url",
            "link",
        )
