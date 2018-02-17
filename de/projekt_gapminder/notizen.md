pandas:
df.index = [1,2,3]
df.columns = [a,b,c]
df.iloc[a:b, c:d]

## Beispieldatensätze

* Gapminder-Datensatz (Grundlagen + Datenaufbereitung + Visualisierung)
* imdb (Aggregation)
* Flugzeugabstürze ODER Terrorismusdatenbank (Zeitreihen + Geo)


### Problem: Bestehende Spalte als zusätzliche Ebene in den Index
  merge + concat mit hierarchischer Indizierung
  stack
  unstack
  Optionen: level, on rows, on cols
  sortlevel
  swaplevel

### Aufgabe 5

Erstelle ein neues DataFrame

  erstellen aus: Series, dict, list
  erstellen, Optionen: index, columns (p.124)

## Kreuztabellen 
* Kreuztabellen
  crosstab
* Pivot-Tabellen
  pivot_table


  * %matplotlib inline
* Arten von Diagrammen
  * bar
  * scatterplot
  * heatmap
  * multi-panel figures
* qualitativ hochwertige Diagramme generieren
* matplotlib gallery
andere: Bokeh, D3.js, seaborn, http://home.gna.org/veusz/


## Tag 1

### Einführung in pandas

* Die Arbeitsumgebung zur interaktiven Datenanalyse
* Kurzübersicht zu `pandas`
* Series
* DataFrame
* Neuerungen in Python 3
* Jupyter Notebooks


### Datenaufbereitung

* CSV- und Excel-Dateien in `pandas` einlesen
* Daten sortieren
* Daten filtern
* Tabellen transponieren
* Auswahl von Zeilen und Spalten
* `pandas`-Tabellen speichern

### Daten zusammenfassen

* statistische Kenngrößen ermitteln
* Tabellen zusammenführen
* hierarchische Indizierung
* Kreuztabellen
* Pivot-Tabellen

### Datenvisualisierung

* Diagramme mit `matplotlib` erstellen
* `matplotlib` aus `pandas` verwenden
* Daten in Jupyter notebooks visualisieren
* Heatmaps
* Multi-Panel-Diagramme
* qualitativ hochwertige Diagramme generieren
* andere Bibliotheken zur Datenvisualisierung

## Tag 2

### Aggregatfunktionen

* Iteration über Zeilen und Spalten
* Gruppieren
* Aggregieren
* Transformieren
* Anwenden eigener Funktionen

### Analyse von Zeitreihen

* Serien von Datumsstempeln
* Umskalieren von Zeitreihen
* Anpassen von Zeitzonen
* Umgang mit lückenhaften Daten
* rollender Durchschnitt
* einfache Prognosen

### Umgang mit geographischen Daten

* Speichern von Koordinaten in `pandas`
* Zeichnen von Karten mit `Basemap`


### Pandas in der Praxis

* Mythen und Fakten
* Numpy
* Modellbildung in scikit-learn
* alternative Programmpakete und Strategien zur Datenmodellierung
* Umgang mit großen Datenmengen
* Best Practices
