def create_json(j,name='what.json'):
    import json
    with open(name, 'w') as outfile:
        json.dump(j, outfile, indent=4)

def youtube_search(title):
    
    import argparse
    from googleapiclient.discovery import build
    
    
    def youtube_wp(options):


        DEVELOPER_KEY = 'AIzaSyBU_VEw-MvbYrLOjbEebqnR796rCajJUTY'
        YOUTUBE_API_SERVICE_NAME = 'youtube'
        YOUTUBE_API_VERSION = 'v3'

        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)

        search_response = youtube.search().list(
            # q=options.q,
            part='id,snippet',
            # maxResults=options.max_results
        ).execute()

        videos = []
        ids = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s (%s)' % (search_result['snippet']['title'],
                                           search_result['id']['videoId']))
                ids.append(search_result['id']['videoId'])

        # print ('Videos:\n', '\n'.join(videos), '\n')

        return videos, ids
    parser = argparse.ArgumentParser()
    args = "something"
    # try:
    #     parser.add_argument('--q', help='Search term', default=title)
    #     parser.add_argument('--max-results', help='Max results', default=10)
    #     args = parser.parse_args()
    # except Exception as e:
    #     return str('Failed to upload to ftp: '+ str(e))
    
    
    # return "something"
    return youtube_wp(args)

def youtube_comments(video_id):
    import googleapiclient.discovery

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCG51VZFkuoWi9yHTAeRDHwTOSwMqpRH8c"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    results = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"

    ).execute()

    #create_json(results)
    commments = []
    for i in results['items']:
        commments.append(i['snippet']['topLevelComment']['snippet']['textDisplay'])

    return commments

def getRandomAnswer(topic):
    import random
    ids = youtube_search(topic)[1]
  
    comments = []
    for id in ids:
        comments.extend(youtube_comments(id))
    return comments[random.randint(0,len(comments)-1)]

# print(getRandomAnswer("something"))

