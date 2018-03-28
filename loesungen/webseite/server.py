# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import pandas as pd
import folium

app = Flask(__name__)

# Laden der Tabelle mit Strassen
df = pd.read_csv('strassen_klein.csv', sep=';;', 
                 names=['ort', 'strasse', 'long', 'lat', 'plz'],
                 encoding='utf-8')


# Suchformular auswerten
@app.route('/suchen', methods=['GET', 'POST'])
def suchen():
    text = request.args.get('text', '')  # Inhalt des Suchfeldes

    inhalt = '<h2>Du hast {} gesucht</h2>'.format(text)
    
    # Karte erzeugen
    berlin_map = folium.Map(location=[52.50, 13.35], zoom_start=8)
    for i, row in df.iterrows():
        if str(row['strasse']).startswith(text):
            coord = [row['lat'], row['long']]
            folium.Marker(coord, popup='dummytext',
                icon=folium.Icon(icon='home',
                color='green')).add_to(berlin_map)
    berlin_map.save('templates/karte.html')
    
    # Tabelle erzeugen
    inhalt += '<table border="1" class="table">'
    for i, row in df.iterrows():
        if str(row['strasse']).startswith(text):
            inhalt += ''' 
              <tr>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
              </tr>'''.format(row['strasse'], row['ort'], row['plz'])
    inhalt += '</table>'
    
    return render_template('strassen.html', inhalt=inhalt)

@app.route('/strasse/<strassenname>')
def strasse_mit_name(strassenname):
    return render_template('strassen.html',
           inhalt='<p>Du bist in der {}</p>'.format(strassenname))

@app.route('/zuhause')
def zuhause():
    return render_template('strassen.html',
           inhalt='<h1>Musterstrasse, Musterstadt</h1>')

@app.route('/')
def startseite():
    inhalt = '''<h1>Unser Straßenverzeichnis</h1>
<p>Hier entsteht unsere Webseite</p>    
<a href="/zuhause">mein Zuhause</a>
'''
    return render_template('strassen.html', inhalt=inhalt)

app.run()
  