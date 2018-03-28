
import re
import os

PFAD = 'cash/'
MUSTER = "Sorry about that.....(.+).....MxM banner"

def songtexte_auslesen(pfad):
    songs = []    
    for dateiname in os.listdir(pfad):
        text = open(pfad + dateiname, encoding='utf-8').read()
        text = re.sub("<br>|</div>|\n", ' ', text)
        treffer = re.findall(MUSTER, text, re.DOTALL)
        if len(treffer) == 1:
            text = treffer[0]
            songs.append(text)
            print("{:30s} {:4d}".format(dateiname, len(text)))
        else:
            print("KEINE TREFFER BEI DATEI", dateiname)
    print(len(songs))
    return songs
