import random, twitter, datetime, time, os
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

#connect to twitter api
print "[" + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + "] Roleplaying initialised."
with open('twitinfo.txt', 'a+') as f:
    twitinfo = f.readlines()
    twitinfo = [line.strip('\r\n') for line in twitinfo]
conKey = twitinfo[0]
conSec = twitinfo[1]
accKey = twitinfo[2]
accSec = twitinfo[3]
api = twitter.Api(consumer_key=conKey,
                  consumer_secret=conSec,
                  access_token_key=accKey,
                  access_token_secret=accSec)
                  
while True:
    now = datetime.datetime.now()
    if str(now.second) == '0':
        if int(now.minute) == 0:
            #read text files
            with open("prefix.txt") as f:
                prefix = [x.strip('\r\n') for x in f.readlines()]
            with open("suffix.txt") as f:
                suffix = [x.strip('\r\n') for x in f.readlines()]
            with open("wildcard.txt") as f:
                wildcard = [x.strip('\r\n') for x in f.readlines()]
            with open("hissatsu.txt") as f:
                hissatsu= [x.strip('\r\n') for x in f.readlines()]

            #create character name
            sufA = random.choice(suffix)
            sufB = sufA
            if (random.randint(0,2) == 0):
                sufB = random.choice(suffix)
            preA = random.choice(prefix)
            preB = random.choice(prefix)
            titl = ""
            while preB == preA:
                preB = random.choice(prefix)
            if (preA == 'q' and not sufA.startswith('u')):
                preA += 'u'
            if (preB == 'q' and not sufA.startswith('u')):
                preB += 'u'
            nameA = preA + sufA
            if (random.randint(0,1) == 0):
                nameA = random.choice(wildcard)
            nameB = preB + sufB
            if (random.randint(0,3) == 0):
                titl = " the " + random.choice(wildcard)
                
            #create stats
            Class = random.choice(prefix) + random.choice(suffix)
            hp = random.choice(wildcard)
            atk = random.choice(wildcard)
            def_ = random.choice(wildcard)
            agi = random.choice(wildcard)
            mag = random.choice(wildcard)
            spell = nameB + ' ' + random.choice(hissatsu)
            
            #pick image
            imgtitle = random.choice(os.listdir("img/"))
            imgpath = ("img/" + imgtitle)

            message = 'name: ' + nameA + ' ' + nameB + titl + '\nclass: ' + Class + '\nhealth: ' + hp + '\nattack: ' + atk + '\ndefence: ' + def_ + '\nagility: ' + agi + '\nmagic: ' + mag + '\nspell: ' + spell
            while (len(message.replace('\n', ' ')) > 140):
                newMessage = message.split('\n')
                del newMessage[-1]
                message = "\n".join(newMessage)

            #tweet
            tweeted = api.PostMedia(message, imgpath)
            print "[" + str(now.hour) + ":" + str(now.minute) + "] Tweeted profile for " + nameA + " " + nameB