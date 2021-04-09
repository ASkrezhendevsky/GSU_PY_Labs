from bs4 import BeautifulSoup
import requests as req
import re

site = 'https://www.imdb.com'

resp = req.get(site + "/name/nm0000233/")
soup = BeautifulSoup(resp.text, 'lxml')

films_tags = soup.findAll("div", {'id': re.compile("^writer-tt")})
for film_tag in films_tags:
    flim_ref = film_tag.b.a['href']
    flim_name = film_tag.b.a.string
    film_soup = BeautifulSoup(req.get(site + flim_ref).text, 'lxml')
    film_rating = film_soup.find("span", {'itemprop': 'ratingValue'})
    print(film_rating)
    if film_rating:
        print(film_tag['class'], flim_ref, flim_name, film_rating.string)
