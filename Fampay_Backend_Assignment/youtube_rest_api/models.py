from django.db import models

# Create your models here.

#  Video title, description, publishing datetime, thumbnails URLs
class Video(models.Model):
    video_title = models.CharField("Video Title", max_length=255)
    description = models.TextField("Description")
    published_on = models.DateTimeField("publishing datetime")
    thumb_url = models.URLField(
        "Thumbnail URL", max_length=255, help_text="The URL to the video thumbnail"
    )
    link = models.URLField(
        "Video Link", max_length=255, help_text="The URL to the video page"
    )

    class Meta:
        verbose_name = "video"
        verbose_name_plural = "videos"
        ordering = ["-published_on"]  # To sort in reverse chronological order

    def __str__(self):
        return self.video_title
