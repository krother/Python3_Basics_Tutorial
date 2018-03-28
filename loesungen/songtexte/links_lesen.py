
import time
import os

songlinks = []
BASE_URL = "http://www.azlyrics.com"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Links zu Songs einlesen
for zeile in open('cash.html', encoding='utf-8'):
    if zeile.startswith('{s:'):
        start = zeile.find(', h:"')
        ende = zeile.find('", c:')
        link = zeile[start+5:ende]
        link = link.replace('..', BASE_URL)
        songlinks.append(link)
        print(link)

# einzelne Songs herunterladen
for link in songlinks:
    dateiname = 'cash/' + link.split('/')[-1]
    if not os.path.exists(dateiname):
        song = requests.get(link, headers=headers)
        print(dateiname)
        f = open(dateiname, 'w', encoding="utf-8")
        f.write(song.text)
        f.close()
        time.sleep(30)  # !! Wichtig !!
    else:
        print("GIBTS SCHON:", dateiname)
        
print(len(songlinks))












