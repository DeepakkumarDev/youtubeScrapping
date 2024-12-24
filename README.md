This project allows you to fetch YouTube videos based on a specific genre and save their details (such as title, description, views, and more) to a CSV file. The code interacts with the YouTube Data API to retrieve video information.


for more detial follow the docs.txt and methods.text to obtain the some useful link 
and create a config.py file first  and write your API_KEY there 

Run app.py and follow the below instruction 

Features
Fetch YouTube Genres: Get a list of available video genres/categories for a specific region.
Fetch Videos by Genre: Search for videos based on a specified genre and retrieve up to 500 videos.
Get Video Details: Retrieve detailed information about each video, including views, description, tags, location, and more.
Save Video Data to CSV: Save the fetched video data to a CSV file for further analysis.

Requirements
Before using this code, ensure you have the following:

Python 3.x installed.
The YouTube Data API v3 key (Follow this guide to get your API key).
The following Python libraries installed:
requests (for making API requests)
pandas (for saving video data to CSV)
google-api-python-client (for interacting with the YouTube API)

How It Works
Functions
get_youtube_genres(region_code)

Purpose: Fetch and display available YouTube video categories (genres) for a given region.
Input: region_code (string, e.g., 'IN' for India).
Output: Prints a list of genre IDs and their titles.

get_youtube_genres('IN')  # Replace 'IN' with your desired region code.


get_videos_by_genre(genre, max_results=500)

Purpose: Fetch up to max_results (default 500) YouTube videos for a specific genre.
Input:
genre (string): The genre name or keyword you want to search for.
max_results (integer): The maximum number of video results you want to fetch (default is 500).
Output: A list of video IDs to be used in the next function to get detailed information.
Usage:
get_videos_by_genre('music')  # Replace 'music' with your desired genre.

get_video_details(video_ids)

Purpose: Retrieve detailed information for a list of YouTube video IDs.
Input: video_ids (list of strings): List of YouTube video IDs to fetch details for.
Output: A list of dictionaries containing detailed video information such as title, views, description, and more.
Usage:
video_data = get_video_details(['video_id1', 'video_id2', 'video_id3'])  # Replace with actual video IDs

save_to_csv(video_data, genre)

Purpose: Save the fetched video details into a CSV file.
Input:
video_data (list): List of video details (from get_video_details).
genre (string): Genre used to search for the videos (used to name the CSV file).
Output: Saves the video data to a CSV file named youtube_<genre>_videos.csv.

save_to_csv(video_data, 'music')  # Replace 'music' with the genre for file naming.


Main Workflow
Fetch Genres: First, you can call get_youtube_genres() to see the available video categories for a region.
Search Videos by Genre: Use get_videos_by_genre() to search for videos related to a specific genre.
Get Detailed Video Data: Call get_video_details() to retrieve detailed information about each video.
Save Data to CSV: Use save_to_csv() to save the gathered video details to a CSV file.


# Step 1: Get the list of genres for India
get_youtube_genres('IN')

# Step 2: Fetch videos related to 'music' genre
videos = get_videos_by_genre('music')

# Step 3: Get detailed information about the fetched videos
video_data = get_video_details(videos)

# Step 4: Save the video data to a CSV file
save_to_csv(video_data, 'music')


for more detial follow the docs.txt and methods.text to obtain the link 
and 
create a config.py file first  and write your API_KEY there 