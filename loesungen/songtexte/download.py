
import requests

url = 'https://www.azlyrics.com/c/cash.html'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
seite = requests.get(url, headers=headers)
seite.encoding = 'utf-8'

f = open("cash.html", 'w', encoding='utf-8')
f.write(seite.text)
f.close()
