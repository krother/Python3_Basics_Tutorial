
# xml

## What is xml?

`xml` is a Python module for reading XML documents.

The XML documents are parsed to a tree-like structure of Python objects.

## Exercises

### Exercise 1

Store the following in an XML document:

    <?xml version="1.0" encoding="UTF-8" ?>
    <movieml name="XML example for teaching" author="Kristian Rother">

    <movielist name="movies">
    <movie id="1" name="Slumdog Millionaire (2008)">
       <rating value="8.0" votes="513804"></rating>
    </movie>
    <movie id="2" name="Planet of the Apes (1968)">
        <rating value="8.0" votes="119493"></rating>
    </movie>
    <movie id="3" name="12 Angry Men (1957)">
        <rating value="8.9" votes="323565"></rating>
    </movie>
    <movie id="4" name="Pulp Fiction (1994)">
        <rating value="8.9" votes="993081"></rating>
    </movie>
    <movie id="5" name="Schindler's List (1993)">
        <rating value="8.9" votes="652030"></rating>
    </movie>
    </movielist>

    <movielist name="serials">
    <movie id="6" name="Breaking Bad (2008)
        {To'hajiilee (#5.13)}">
        <rating value="9.7" votes="14799"></rating>
    </movie>
    <movie id="7" name="Game of Thrones (2011) 
        {The Laws of Gods and Men (#4.6)}">
        <rating value="9.7" votes="13343"></rating>
    </movie>
    <movie id="8" name="Game of Thrones (2011) 
        {The Lion and the Rose (#4.2)}">
        <rating value="9.7" votes="17564"></rating>
    </movie>
    <movie id="9" name="Game of Thrones (2011) 
        {The Rains of Castamere (#3.9)}">
        <rating value="9.8" votes="27384"></rating>
    </movie>
    <movie id="10" name="Breaking Bad (2008) 
        {Ozymandias (#5.14)}">
        <rating value="10.0" votes="55515"></rating>
    </movie>
    </movielist>

    </movieml>

### Exercise 2

Run the following program:

    from xml.dom.minidom import parse

    document = parse('movies.xml')

    taglist = document.getElementsByTagName("movie")
    for tag in taglist:
        mid = tag.getAttribute('id')
        name = tag.getAttribute('name')
        print(mid, name)

        subtags = tag.getElementsByTagName('rating')
        print(subtags)

### Exercise 3

Calculate the total number of votes.