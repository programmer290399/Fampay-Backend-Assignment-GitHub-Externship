from rest_framework.decorators import api_view
from rest_framework.response import Response
from youtube_rest_api.models import Video
from youtube_rest_api.serializers import VideoSerializer

# Create your views here.
@api_view(["GET"])
def video_collection(request):
    if request.method == "GET":
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
