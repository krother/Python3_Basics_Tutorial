import ijson

f = open('streets.geojson', encoding="iso-8859-2")
objects = ijson.items(f, 'features.item')

with open('strassen.csv', 'w') as out:
    for i, o in enumerate(objects):
        p = o['properties']
        plz = p['PLZ']
        gemeinde = p['GEMEINDE'].encode('iso-8859-2').decode('utf-8')
        if p['NAME']:
            street = p['NAME'].encode('iso-8859-2').decode('utf-8')
        else:
            street = '-'
        lon = p['CENTR_LON']
        lat = p['CENTR_LAT']
        line = "{:35s} {:30s} {:5.2f}/{:5.2f}   {:20s}".format(gemeinde, street, lon, lat, plz)
        line = "{};;{};;{};;{};;{}\n".format(gemeinde, street, lon, lat, plz)
        out.write(line)
        if i % 10000 == 0:
            print(i)
