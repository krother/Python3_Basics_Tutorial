
# Das Modul requests

### Wofür ist es gut?

Webseiten aus Python herunterladen.

`requests` sends HTTP requests to web pages and allows you to read their content. Most standard tasks are a lot easier compared to the standard module `urllib`. `requests` can sending data to web forms via HTTP GET and POST, submit files and manage cookies. 


### Standardmäßig mit Python installiert

Nein

### Teil der Anaconda-Distribution

Ja

### Beispiel

Die Homepage des Autors lesen.

    >>> import requests
    >>> r = requests.get('http://www.academis.eu')
    >>> print(r.text)

Wissenschaftliche Artikel auf PubMed suchen:

    >>> url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    >>> param_dict = {'db':'pubmed', 'term':'escherichia', 'rettype':'uilist'}

    >>> r = requests.get(url, params=param_dict)
    >>> print(r.text)


### Wo kannst Du mehr erfahren?

[http://docs.python-requests.org/en/latest/index.html](http://docs.python-requests.org/en/latest/index.html)
