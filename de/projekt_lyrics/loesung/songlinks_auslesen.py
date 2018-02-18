"""
TEIL 2

Lies die Links zu einzelnen Songs
aus der in Teil 1 heruntergeladenen Seite aus
und gib diese auf dem Bildschirm aus (ohne Webzugriff)
"""

import re


def links_auslesen(dateiname):
    """Gibt eine Liste aller Links zurück"""
    links = []
    for line in open(dateiname):
        if 'href="../lyrics' in line:
            anfang = line.find('../lyrics')
            ende = line.find('.html')
            links.append(line[anfang + 10:ende + 5])
    return links


def links_auslesen_mit_regex(dateiname):
    """Wie oben, aber mit regulärem Ausdruck"""
    text = open(dateiname).read()
    muster = 'href\=\"\.\.\/lyrics/([\w\.\/]+.html)'
    return re.findall(muster, text)


# das if verhindert, daß der Code beim Importieren ausgeführt wird
if __name__ == '__main__':
    # for link in links_auslesen('verzeichnis_direstraits.html'):
    for link in links_auslesen_mit_regex('verzeichnis_direstraits.html'):
        print(link)
