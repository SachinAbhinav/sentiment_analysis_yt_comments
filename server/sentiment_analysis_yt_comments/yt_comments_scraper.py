from googleapiclient.discovery import build
import json

# Replace with your API key
api_key = 'AIzaSyASfeeRDgi5EHWZK8Rtr2v50ZRNCC6l--s'

# Function to extract video ID from YouTube URL
def get_video_id(url):
    import re
    regex = r'(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]{11})'
    match = re.match(regex, url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube URL")

# Function to get comments from a YouTube video
def get_youtube_comments(video_url, api_key):
    video_id = get_video_id(video_url)
    
    youtube = build('youtube', 'v3', developerKey=api_key)

    comments = []
    next_page_token = None

    while True:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            pageToken=next_page_token,
            maxResults=100,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response['items']:
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comments.append(comment)

        next_page_token = response.get('nextPageToken')

        if not next_page_token:
            break

    return comments

# Replace with the YouTube video URL you want to scrape comments from
# video_url = 'https://www.youtube.com/watch?v=xh9JMASX5Ic'

# comments = get_youtube_comments(video_url, api_key)

# # Print or save comments
# for idx, comment in enumerate(comments, 1):
#     print(f"{idx}: {comment}")
