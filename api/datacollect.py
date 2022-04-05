from distutils.command.upload import upload
from googleapiclient.discovery import build
import httplib2
import json
from time import time, sleep

# Script is the medium for youtube api hits and storing into the db relevant data
# Could separate into 2 scripts, one for api calls and one for db methods, but will turn it into two once it becomes a mess (if it seems)


def retrieve_description(channel_id):

    # let's request a specific channel & one of it's videos
    channel_id = channel_id

    # set up the youtube object
    api_key = 'AIzaSyBo6OalCqZKSDmTiKVfW-kjv0_55WUSKNU'
    youtube = build('youtube', 'v3', developerKey = api_key)
    # set up the http package calling object 
    http = httplib2.Http()


    # youtube api channel id : 
    # params : request contentDetails, channel id
    # response : 'uploads' playlist id
    (resp, content) = http.request("https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&id={}&key=AIzaSyBo6OalCqZKSDmTiKVfW-kjv0_55WUSKNU".format(channel_id)) # %2C for a list of request parms such as snippet and statistics alongside the contentDetails.
    channel_content = content.decode('utf-8')

    # extract uploads playlist id from response
    playlist_id = channel_content.split("uploads\": \"")[1].split("\"")[0]


    # youtube api playlist item :
    # params : 'uploads' playlist id
    # returns : max 2 videos with full details
    (resp, content) = http.request("https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId={}&maxResults=1&key=AIzaSyBo6OalCqZKSDmTiKVfW-kjv0_55WUSKNU".format(playlist_id))
    items_content = content.decode('utf-8')

    # extract description(s)
    description = items_content.split("description\": \"")[1].split("thumbnails")[0] # has some trailing ", " - but for the most part it won't affect the parsing logic

    # extract upload time 
    upload_date = items_content.split("publishedAt\" : \"")[1].split("channelID")[0] # ISO 8601 format
    
    # Logic below:
    # condition 1: return early on any sign of no new upload (same original upload date)
    # condition 2: new upload and proceed to store in database
    print(description) 
    


def retrieve_channel_ids():
    # Have this hit the db and call retrieve description
    return


#
# includes calls to the database interface and to the youtube api
#
if __name__ == '__main__':

    while True:
    # have this be a while loop that executes once every ten minutes
    # call a retreive from database function
        sleep(60 - time() % 60)
        retrieve_description("UC5RxNUZ9_c94ZEfJGnJZmTw")
    
    # end while