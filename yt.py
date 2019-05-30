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
            q=title,
            part='id,snippet',
            maxResults=10
        ).execute()

        videos = []
        ids = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s' % (search_result['snippet']['title']))
                ids.append(search_result['id']['videoId'])

        # print ('Videos:\n', '\n'.join(videos), '\n')

        return videos, ids

    parser = argparse.ArgumentParser()

    return youtube_wp(title)

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


##########

def getTitles(topic):
    import random
    ids = youtube_search(topic)[1]

    def getRandomAnswer(id):
        comments = []
        comments.extend(youtube_comments(id))
        return comments[random.randint(0, len(comments) - 1)]

    titles = youtube_search(topic)[0][:3]

    idx = random.randint(0,2)

    return titles,getRandomAnswer(ids[idx]),idx # idx e indexul titlului corespondet al comentariului din titles
#print(getTitles('kim kardashian'))

def chooseTitle(response,topic):
    title, comm, idx = getTitles(topic)

    if response == idx:
        return 'Good job kim'
    else:
        return 'Try again kim'


def getThumbnail(topic):
    def getImportantWord(com):
        import urllib.response
        import random
        import re
        import requests

        docA = com

        def gif(what, howMany=1):

            url = 'http://api.giphy.com/v1'
            giphy_api_key = 'oq1hqDDGKgpbFewztUQrDr6bIzLGs1IO'
            url = 'https://api.giphy.com/v1/gifs/search?api_key=oq1hqDDGKgpbFewztUQrDr6bIzLGs1IO&q={}&limit=3&offset=0&rating=G&lang=en'.format(
                what)
            r = requests.get(url)
            lists = []
            for item in r.json()['data']:
                html = urllib.request.urlopen(item['url']).read().decode()
                rr = re.findall('<meta property="og:url" content="(.*)"', html)
                lists.append(rr[0] + '\n')
            random.shuffle(lists)
            return lists[0]

        bowA = docA.split(" ")
        wordSet = set(bowA)
        wordDictA = dict.fromkeys(wordSet, 0)
        for word in bowA:
            wordDictA[word] += 1

        def computeTF(wordDict, bow):
            tfDict = {}
            bowCount = len(bow)
            for word, count in wordDict.items():
                tfDict[word] = count / float(bowCount)
            return tfDict

        def computeIDF(docList):
            import math
            idfDict = {}
            N = len(docList)

            idfDict = dict.fromkeys(docList[0].keys(), 0)
            for doc in docList:
                for word, val in doc.items():
                    if val > 0:
                        idfDict[word] += 1

            for word, val in idfDict.items():
                idfDict[word] = math.log10(N / float(val))

            return idfDict

        def computeTFIDF(tfBow, idfs):
            tfidf = {}
            for word, val in tfBow.items():
                tfidf[word] = val * idfs[word]
            return tfidf

        stats = computeTFIDF(computeTF(wordDictA, bowA), computeIDF([wordDictA]))

        def keywithmaxval(d):
            v = list(d.values())
            k = list(d.keys())
            return k[v.index(max(v))]

        return gif(keywithmaxval(stats))


    titles,comm,idx = getTitles(topic)
    return (getImportantWord(titles[idx]))

#print(getThumbnail('kim'))

def search_yt(what):
    import urllib.parse
    import urllib.request
    import re

    query_string = urllib.parse.urlencode({"search_query": what})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    #webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])

    return "http://www.youtube.com/watch?v=" + search_results[0]


# a,b,c = getTitles('kim')
# print(a,b,c)
# print(a[c])
# print(search_yt(a[c]))