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

    return getImportantWord(topic)