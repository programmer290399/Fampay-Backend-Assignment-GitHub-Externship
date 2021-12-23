import os
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from Fampay_Backend_Assignment.settings import (
    YOUTUBE_API_SERVICE_NAME,
    YOUTUBE_API_VERSION,
    NUM_KEYS,
    API_KEYS,
)


def youtube_search(query, check_int, max_results):
    for key_num in range(1, NUM_KEYS + 1):
        DEVELOPER_KEY = API_KEYS[f"API_KEY_{key_num}"]
        try:
            youtube = build(
                YOUTUBE_API_SERVICE_NAME,
                YOUTUBE_API_VERSION,
                developerKey=DEVELOPER_KEY,
            )

            target_ts = (
                datetime.now() - timedelta(minutes=check_int)
            ).isoformat() + "Z"

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
            print(f"Request Succeeded with API_KEY_{key_num}")
            return search_response
        except HttpError as e:
            print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
            if e.resp.status == 403:
                print(f"Request Failed with API_KEY_{key_num}")
                continue
            return dict()
