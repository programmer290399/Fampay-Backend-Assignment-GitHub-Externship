from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Fampay_Backend_Assignment.settings import (
    DEVELOPER_KEY,
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
)


def youtube_search(query, check_int, max_results):
    try:
        youtube = build(
            YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY
        )

        target_ts = (datetime.now() - timedelta(minutes=check_int)).isoformat() + "Z"

        search_response = (
            youtube.search()
            .list(
                q=query,
                part="snippet",
                maxResults=max_results,
                order="date",
                publishedAfter=target_ts,
            )
            .execute()
        )

        return search_response
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
        return dict()
