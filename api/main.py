from googleapiclient.discovery import build
import httplib2
import json


# let's request a specific channel & one of it's videos

channel_id = "UC5RxNUZ9_c94ZEfJGnJZmTw" # Jeenine Media

# set up the youtube object

api_key = 'AIzaSyBo6OalCqZKSDmTiKVfW-kjv0_55WUSKNU'
youtube = build('youtube', 'v3', developerKey = api_key)


# set up the http package calling object 

http = httplib2.Http()


# read in response and content of the youtube channel api call

(resp, content) = http.request("https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&id={}&key=AIzaSyBo6OalCqZKSDmTiKVfW-kjv0_55WUSKNU".format(channel_id)) # %2C for a list of request parms such as snippet and statistics alongside the contentDetails.

# content is type bytes, resp is <class 'httplib2.Response'> and includes status i.e. 403 or 200
channel_content = content.decode('utf-8')

# extract uploads playlist id

playlist_id = channel_content.split("uploads\": \"")[1].split("\"")[0]


# Request for playlistItems, most notably the snippet content which contains video ids and title. Include logic so if title and id are the same in database - stop executing.

(resp, content) = http.request("https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&maxResults=1&key=AIzaSyBo6OalCqZKSDmTiKVfW-kjv0_55WUSKNU".format(playlist_id))

items_content = content.decode('utf-8')

description = items_content.split("description\": \"")[1].split("thumbnails")[0]

print(description)


