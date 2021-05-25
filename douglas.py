import tweepy
import threading
from numpy import loadtxt
import random
import datetime
import time
import pytz

# Douglas Is Online
# www.twitter.com/douglasisonline
# Made by @mooksmonster & @doonturz
# Version 1.4
keys = loadtxt("keys.txt", dtype=str)
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2],keys[3])
douglasAPI = tweepy.API(auth)

if douglasAPI.verify_credentials():
    print("Douglas has awoken from his slumber once again to deliver revelations.")
    print("Version 1.4 + Python 3.8.2 + Tweepy 3.9.0")

sentenceArray = []
randSentence = 0

# If Douglas chooses the last number as randX, the number will be too large for the array index.
def generateNoun():
    nounArray = loadtxt("noun.txt", dtype=str, comments="#", delimiter=",", unpack=False)
    randNoun = random.randrange(0, len(nounArray))
    return nounArray[randNoun]

def generateVerb():
    verbArray = loadtxt("verb.txt", dtype=str, comments="#", delimiter=",", unpack=False)
    randVerb = random.randrange(0, len(verbArray))
    return verbArray[randVerb]

def generateAdj():
    adjArray = loadtxt("adj.txt", dtype=str, comments="#", delimiter=",", unpack=False)
    randAdj = random.randrange(0, len(adjArray))
    return adjArray[randAdj]

def generateSentence():
    sentenceArray = loadtxt("sentence.txt", dtype=str, comments="#", delimiter=",", unpack=False)
    randSentence = random.randrange(0, len(sentenceArray))
    return sentenceArray[randSentence]

def preach():
    tempSent = []
    finalSent = ""
    sentenceVal = generateSentence()
    randSentenceArray = str(sentenceVal)
    _ = len(randSentenceArray)

    for x in range(_):
        if int(randSentenceArray[x]) == 1:
            tempSent.append(generateNoun())
        elif int(randSentenceArray[x]) == 2:
            tempSent.append(generateVerb())
        elif int(randSentenceArray[x]) == 3:
            tempSent.append(generateAdj())
        continue

    # Allows for any length of sentence to be input
    for x in range(0, len(tempSent)):
        finalSent += " " + tempSent[x]
        continue

    return(finalSent)

def replyToMentions():
    mentionsMemoryArray = loadtxt("mentionMemory.txt", dtype=str, comments="#", delimiter=",", unpack=False)
    twts = douglasAPI.mentions_timeline(mentionsMemoryArray[-1])
    for y in range(0, len(twts)):
        mentionsMemoryArray = loadtxt("mentionMemory.txt", dtype=str, comments="#", delimiter=",", unpack=False)
        if twts[y].id not in mentionsMemoryArray:
            douglasAPI.update_status(preach(), in_reply_to_status_id=twts[y].id, auto_populate_reply_metadata=True)
            mentionsMemory = open("mentionMemory.txt", 'a')
            mentionsMemory.write("\n")
            mentionsMemory.write(str(twts[y].id))
            mentionsMemory.close()
            return

class hourlyTweetThread(threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      
   def run(self):
       while True:
        print(self.name + ": Running.")
        vTemp = preach()
        print(datetime.datetime.now(pytz.timezone('US/Pacific')))
        print(vTemp)
        douglasAPI.update_status(vTemp)
        print(self.name + ": Task Complete.")
        time.sleep(3600)

class replyingToMention(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    
    def run(self):
        print(self.name + ": Running.")
        while True:
            replyToMentions()
            print(datetime.datetime.now(pytz.timezone('US/Pacific')))
            print(self.name + ": Complete.")
            time.sleep(120)

tweetingThread = hourlyTweetThread(1, "Preaching Thread")
try:
  tweetingThread.start()
except:
  print("An exception occurred with the hourly tweet thread.") 
  exit()

replyThread = replyingToMention(2, "Replying to Mention Thread")
try:
    replyThread.start()
except:
    print("An exception occurred with the replying to mention thread.")
    exit()