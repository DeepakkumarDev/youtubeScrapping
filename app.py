import requests 
import pandas as pd 
from googleapiclient.discovery import build
import config 


youtube = build('youtube','v3',developerKey=config.API_KEY)

BASE_VIDEO_URL = "https://www.youtube.com/watch?v="


def get_youtube_genres(region_code):
    url = 'https://www.googleapis.com/youtube/v3/videoCategories'
    params = {
        'part': 'snippet',
        'regionCode': region_code,
        'key': config.API_KEY
    }
    response = requests.get(url,params=params)
    categories = response.json().get('items', [])
    for category in categories:
        print(f"ID: {category['id']} | Genre: {category['snippet']['title']}")

def get_videos_by_genre(genre,max_results=500):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    videos_ids = []
    params = {
        'part':'snippet',
        'q':genre,
        'type':'video',
        'maxResults':50,
        'key': config.API_KEY
    }

    while len(videos_ids) < max_results:
        response = requests.get(search_url,params=params)
        result = response.json()

        videos_ids += [item['id']['videoId'] for item in result['items'] if 'videoId' in item['id']]
        if 'nextPageToken' in result:
            params['pageToken'] = result['nextPageToken']
        else:
            break

        if len(videos_ids) > max_results:
            videos_ids = videos_ids[:max_results]
            break
    return get_video_details(videos_ids)


def get_video_details(video_ids):
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    all_video_data = []

    for i in range(0,len(video_ids),50):
        chunk_ids = video_ids[i:i+50]
        params ={
            'part': 'snippet,statistics,contentDetails,recordingDetails',
            'id': ','.join(chunk_ids), 
            'key':config.API_KEY       
        }
        response = requests.get(video_url, params=params)
        result = response.json()

        for item in result['items']:
            video_data = {
                'Video URL': BASE_VIDEO_URL + item['id'],
                'Title': item['snippet'].get('title', 'N/A'),
                'Description': item['snippet'].get('description', 'N/A'),
                'Channel Title': item['snippet'].get('channelTitle', 'N/A'),
                'Video Published At': item['snippet'].get('publishedAt', 'N/A'),
                'Tags': ', '.join(item['snippet'].get('tags', [])),
                'Category ID': item['snippet'].get('categoryId', 'N/A'),
                'Topic Details': item.get('topicDetails', {}).get('topicCategories', 'N/A'),
                'View Count': item['statistics'].get('viewCount', 'N/A'),
                'Comment Count': item['statistics'].get('commentCount', 'N/A'),
                'Captions Available': item['contentDetails'].get('caption', 'false'),
                'Location of Recording': item.get('recordingDetails', {}).get('location', 'Not available')
            }
            all_video_data.append(video_data)
    
    return all_video_data


def save_to_csv(video_data, genre):
    df = pd.DataFrame(video_data)
    csv_file = f"youtube_{genre}_videos.csv"
    df.to_csv(csv_file, index=False, encoding='utf-8')
    print(f"Data saved to {csv_file}")


def main():
    genre = input("Enter the genre: ")
    print(f"Fetching top 500 videos for genre: {genre}")
    videos = get_videos_by_genre(genre, max_results=500)
    save_to_csv(videos, genre)

if __name__ == "__main__":
    # main()
    get_youtube_genres('IN')