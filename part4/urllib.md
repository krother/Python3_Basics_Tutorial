
# urllib

The HTML code of web pages and downloadable files from the web can be accessed in a similar way as reading files:

    import urllib2
    url = 'http://www.academis.eu'
    page = urllib.urlopen(url)
    print(page.read())

## Exercises

### Exercise 1

Download the homepage of your academic institution or company and print it to the screen.
