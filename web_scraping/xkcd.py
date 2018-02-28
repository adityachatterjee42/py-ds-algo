import requests
from requests_html import HTMLSession
import urllib

session = HTMLSession()
comic_id = 1
while True:
    file_name=str(comic_id)+'.jpg'
    base_url='https://xkcd.com/'
    final_url=base_url+str(comic_id)
    r = session.get(final_url)
    if r.status_code != 200:
        break
    pics = r.html.find('img')[1]
    f = open(file_name, 'wb')
    f.write(requests.get('http:'+pics.attrs['src']).content)
    f.close()
    comic_id+=1