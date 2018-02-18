"""
TEIL 1

Lade eine Webseite mit Songtiteln und Links
für einen Künstler von www.azlyrics.com herunter.
"""
import requests
import os

# Name des Künstlers
ARTIST = 'direstraits'
PATH = ARTIST

# erstelle ein Verzeichnis mit dem Namen des Künstlers (ohne Leerzeichen)
if not os.path.exists(PATH):
    os.mkdir(PATH)


# gehe im Browser auf azlyrics.com und
# finde die URL mit Songtexten dieses Künstlers
BASE_URL = 'http://www.azlyrics.com/'

# headers, damit die Seite denkt, wir seien ein Browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# verwende requests, um die Seite mit dem Songverzeichnis zu lesen
url = BASE_URL + '{}/{}.html'.format(PATH[0], PATH)
print(url)
catalog = requests.get(url, headers=headers)

# speichere die Seite in einer Textdatei
f = open('verzeichnis_{}.html'.format(PATH), 'w')
f.write(catalog.text)
f.close()
