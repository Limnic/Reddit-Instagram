from InstagramAPI import InstagramAPI
import praw
import requests
import urllib.request
import time
import keyboard
from PIL import Image
import math
 
api = InstagramAPI("username", "password")
api.login()
 
 
#prew
reddit = praw.Reddit(client_id='id of reddit',
    client_secret='from reddit',
    username='reddit_username',
    password='password',
    user_agent='name of the project')
 
def DLimage(url, filePath, fileName):
    fullPath = filePath + fileName + '.jpg'
    urllib.request.urlretrieve(url, fullPath)
 
 
#folder where it saves the memes
f = open('C:/Users/RealS3nji/Desktop/MEMES/teste.txt', mode='r')
filePath = open(r'C:/Users/RealS3nji/Desktop/MEMES')
filePath = "C:/Users/RealS3nji/Desktop/MEMES/"
  

subreddit = reddit.subreddit('dankmemes')
 
 
 
# hashtags
captionTags = "#memes"
 
#Description
captionText = "Follow for more content"
 
waitTime = 2
 
numRounds = 100 #number of posts
 
postFrequency = 4000 # hour posts in seconds
 
numPics = 1 #how many photos per post
 
for x in range(numRounds):
    new_memes = subreddit.rising(limit=numPics) #.hot/.rising/.new  (i would like to select top from 24h/week/month  but i dont know how)
    authors = []
    photoAlbum = [] 
    print("Round/post number:", x)
    for subbmission in new_memes:
        print(subbmission.is_self)
        if subbmission.is_self == True: #see if it is text or not
            print("Post was text, skipping to next post.")
            continue
        else:
            print("here")
        url = subbmission.url
        time.sleep(waitTime)
        fileName = str(subbmission)
        fullPath = filePath + fileName + '.jpg'
        print(fullPath )
        #print destination
        time.sleep(waitTime)
        #print url
        try:
            DLimage(url, filePath, fileName)
        except:
            print("scratch that, next post.")
            continue
        time.sleep(waitTime)
        author = str(subbmission.author)
        authors.append(author)
        time.sleep(waitTime)
        img = Image.open(fullPath)
        width, height = img.size
        img = img.resize((1000, 1000), Image.NEAREST) #resize
        img = img.convert("RGB")
        img.save(fullPath)
        photoAlbum.append({
                'type': 'photo',
                'file': fullPath,
            })
 
    authors = ''.join(str(e + ', ') for e in authors)
    print(photoAlbum)
    api.uploadAlbum(photoAlbum, caption=(captionText + '\n' + 'Created by redditors: ' + authors[0:(len(authors)-2)] + '.' + '\n' + captionTags))
    time.sleep(postFrequency)