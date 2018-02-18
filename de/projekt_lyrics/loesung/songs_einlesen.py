"""
TEIL 4

Songtexte aus den heruntergeladenen HTML-Dateien 
einlesen, so daß ein Textkorpus entsteht.
"""
import os


def song_einlesen(dateiname):
    """Liest EINEN Song ein und gibt einen String mit dem Text zurück."""
    f = open(dateiname, encoding="utf-8")
    text = f.read()
    anfang = text.find('Sorry about that. -->')  # Hier fängt der Inhalt an
    ende = text.find('MxM banner')               # Hier hört der Inhalt auf
    return text[anfang + 22:ende - 23]


def songtexte_einlesen(verzeichnis):
    """Liest ALLE Songs aus einem Verzeichnis ein."""
    texte = []
    for dateiname in os.listdir(verzeichnis):
        songtext = song_einlesen(verzeichnis + dateiname)
        texte.append(songtext)
    return texte


if __name__ == '__main__':
    korpus = songtexte_einlesen('direstraits/')
    for text in korpus:
        print(text)
        print('-' * 60)
