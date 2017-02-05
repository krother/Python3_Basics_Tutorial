
# Wiederholungsübung

### Aufgabe 1

Das folgende Programm verbindet eine Liste von Namen mit einer Liste von Zahlen und gibt diese aus.

Das Programm enthält **drei Defekte**. Finde und behebe diese.


    top_names = ['Jacob', 'Michael', 'Matthew', 'Joshua', 'Christopher', 
                 'Nicholas', 'Andrew' 'Joseph', 'Daniel', 'Tyler']

    top_numbers [34465, 32025, 28569, 27531, 24928,
                   24928, 23632, 22818, 22307, 21500]

    if len(top_names) == len(top_numbers):
       print("Achtung: die Listen sind unterschiedlich lang!")
       print(len(top_names), len(top_numbers))

    for i in range(len(top_names)):
        name = top_names[i]
        number = top_numbers[i]
        print("{:10s} {:6d}".format(name, number))


### Aufgabe 2

Verwende `zip()`, um das Programm zu vereinfachen.

### Aufgabe 3

Schreibe ein Programm, welches *die drei häufigsten* Vornamen für Jungen und Mädchen in jedem Jahrgang ermittelt und ausgibt.

