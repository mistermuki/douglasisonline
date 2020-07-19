import sys
import os
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
# Version 1.2

auth = tweepy.OAuthHandler('4MWWQHdsbatnBvEagSl1uB9OZ', '5HEB4M35aH51YnxrPqGmsf21zk1nyDsE7ZNhn4B2IwLCBvLen0')
auth.set_access_token('1187492688938975232-h4th2vLBh09NlgH0s9EO1e51CHrrCi','MlXkUUNmyduJYHi6EQmIgU8XV8Jq8Cuvbt6fyQmLesMIr')
douglasAPI = tweepy.API(auth)

if douglasAPI.verify_credentials():
    print("Douglas has awoken from his slumber once again to deliver revelations.")

sentenceArray = []
randSentence = 0


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

    for x in range(len(randSentenceArray)):
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

# Tweets every 30 seconds, displays Pacific Time, and the tweet he said.
while True:
    vTemp = preach()
    print(datetime.datetime.now(pytz.timezone('US/Pacific')))
    print(vTemp)
    douglasAPI.update_status(vTemp)
    time.sleep(3600)





