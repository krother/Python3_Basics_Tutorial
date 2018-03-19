
# Animierter Scatterplot

In dieser Übung werden wir versuchen, die berühmte Animation von Hans Rosling nachzustellen (siehe [https://www.youtube.com/watch?v=jbkSRLYSojo](https://www.youtube.com/watch?v=jbkSRLYSojo)).

Dazu erstellen wir eine Serie von Bildern, die wir zu einem animierten GIF verbinden.

### Schritt 1

Erstelle einen Scatterplot für die Korrelation zwischen Lebenserwartung und Fruchtbarkeit wie in der ersten Übung für *jedes* Jahr zwischen 1960 und 2015
(davor sind die Daten sehr lückenhaft).

### Schritt 2

Passe Dein Programm so an, dass die Größe der Kugeln die Bevölkerung aus den Gapminder-Daten repräsentiert.

### Schritt 3

Speichere jeden Scatterplot als eigene Datei mit der Jahreszahl im Dateinamen ab, z.B. `lifeexp_..` .


### Schritt 4

Installiere das Python-Modul `imageio`, indem Du auf der Kommandozeile eingibst:

    pip install imageio

(kein Problem unter Linux/Mac, unter Windows mußt Du eventuell vorher Anaconda installieren.)


### Schritt 5

Passe das folgende Skript an und führe es aus:

    import imageio

    images = []

    for i in range(0, 100):
        filename = 'lifeexp_{}.png'.format(i)
        images.append(imageio.imread(filename))

    imageio.mimsave('output.gif', images, fps=20)

