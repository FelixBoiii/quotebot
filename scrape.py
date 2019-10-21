#beste plaatjes om te gebruiken tussen de 800 en 3000 pixels in de breedte

import praw, textwrap, math, random, os
import pandas as pd
import datetime as dt
from PIL import Image, ImageDraw, ImageFont
import urllib.request

def whole():
    print('loading..')
    #zoekt plaatje op met random hoogte en breedte
    widthurlimage = random.randint(800, 2000)
    heighturlimage = random.randint(500, widthurlimage+1)
    urllib.request.urlretrieve("https://picsum.photos/"+str(widthurlimage)+"/"+str(heighturlimage), "tempimage.jpg")

    #setup plaatje
    image = Image.open('tempimage.jpg')
    imagewidth, height = image.size
    rootnumber = imagewidth**0.65
    specialsize = math.floor(0.65*rootnumber)

    #reddit praw api moet je zelf invullen met eigen account
    reddit = praw.Reddit(client_id='', \
                     client_secret='', \
                     user_agent='', \
                     username='', \
                     password='')

    #de goede subreddit
    subreddit = reddit.subreddit('Showerthoughts')

    #pakt de titel van de 3 na hoogste post in hot
    randdd = random.randint(3, 50)
    for submission in subreddit.hot(limit=randdd):
        hottitle = submission.title

    #laat de text niet van het scherm af gaan
    splithottitle = textwrap.wrap(hottitle, width=math.floor(0.011*imagewidth+27))

    #PIL image manipulatie
    draw = ImageDraw.Draw(image)

    #font = ImageFont.truetype('impact.ttf', size=math.floor(imagewidth/20))
    font = ImageFont.truetype('impact.ttf', size=specialsize)

    #variabelen voor de opmaak van de tekst
    (x, y) = (20,40)
    color = 'rgb(255, 255, 255)'

    #loopt door alle lijnen tekst en plkt deze in het plaatje waarbij het y cordinaat steeds vergroot wordt.
    for line in splithottitle:
        #maakt een zwarte border rond de tekst
        draw.text((x-3, y-3), line, fill='rgb(0,0,0)', font=font)
        draw.text((x+3, y-3), line, fill='rgb(0,0,0)', font=font)
        draw.text((x-3, y+3), line, fill='rgb(0,0,0)', font=font)
        draw.text((x+3, y+3), line, fill='rgb(0,0,0)', font=font)
        #tekend de boveste laag en zet de hoogte van de volgede lijn lager
        draw.text((x, y), line, fill=color, font=font)
        y += specialsize

    #delete achtergrond plaatje
    os.remove("tempimage.jpg")

    #slaat het plaatje op
    randomnummer = str(random.randint(0, 10000))
    image.save('E:/Users/Bart/Documents/python/reddit quote bot/pics/nieuwpic'+randomnummer+'.png')
def looping():
    whole()
    print("done!")
    goagain = input("want to do it again? type: yes: ")
    if goagain == 'yes':
        looping()

looping()
