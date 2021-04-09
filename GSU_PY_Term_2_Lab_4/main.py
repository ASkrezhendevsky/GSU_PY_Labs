from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import requests as req
import re

site = 'https://www.imdb.com'

resp = req.get(site + "/name/nm0000233/")
soup = BeautifulSoup(resp.text, 'lxml')

writer_id_re = re.compile("^writer-tt")
rating = 'ratingValue'

films = {"year": [], "name": [], "rating": []}

films_tags = soup.findAll("div", {'id': writer_id_re})
for film_tag in films_tags:
    film_ref = film_tag.b.a['href']
    film_name = film_tag.b.a.string
    film_year = film_tag.span.string
    film_soup = BeautifulSoup(req.get(site + film_ref).text, 'lxml')
    film_rating = film_soup.find("span", {'itemprop': rating})
    print(film_rating)
    if film_rating:
        print(film_tag['class'], film_ref, film_name, film_rating.string)
        films["year"].append(film_year)
        films["name"].append(film_name)
        films["rating"].append(float(film_rating.string))

films["year"].reverse()
films["name"].reverse()
films["rating"].reverse()
films_table = pd.DataFrame(films, index=films["year"])

plot = films_table.plot(figsize=(8, 6), linewidth=2, )

plt.show()
