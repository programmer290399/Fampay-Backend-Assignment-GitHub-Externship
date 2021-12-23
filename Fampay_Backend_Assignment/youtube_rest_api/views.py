from rest_framework.decorators import api_view
from rest_framework.response import Response
from youtube_rest_api.models import Video
from youtube_rest_api.serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination


# Create your views here.
@api_view(["GET"])
def video_collection(request):
    paginator = PageNumberPagination()
    query_set = Video.objects.all()
    context = paginator.paginate_queryset(query_set, request)
    serializer = VideoSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)
