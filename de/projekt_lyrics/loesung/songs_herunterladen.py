"""
TEIL 3

Lade alle Songs für einen Künstler herunter
"""

import requests
import os
import time
from songlinks_auslesen import links_auslesen

# headers, damit die Seite denkt, wir seien ein Browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def song_herunterladen(link):
    """Lädt einen Song herunter und speichert ihn in einer Textdatei"""
    dateiname = link
    # prüfe ob die Datei schon existiert
    if not os.path.exists(dateiname):
        # wenn nicht lade sie herunter
        url = "http://www.azlyrics.com/lyrics/{}".format(link)
        print(url)  # ganz wichtig zur Fehlerdiagnose!
        seite = requests.get(url, headers=headers)
        # speichere die komplette Seite in einer Textdatei
        open(dateiname, 'w', encoding="utf-8").write(seite.text)
        time.sleep(30)
        # WARTEN IST EXTREM WICHTIG,
        # WEIL UNS DER SERVER SONST AUSSPERRT


# Verzeichnis für die Ausgabe anlegen
if not os.path.exists('direstraits'):
    os.mkdir('direstraits')

for link in links_auslesen('verzeichnis_direstraits.html'):
    song_herunterladen(link)
