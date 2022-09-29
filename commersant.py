import requests
from bs4 import BeautifulSoup as BS

hrefs = {'economy': 'https://www.kommersant.ru/rubric/3?from=burger&page=1',
         'politic': 'https://www.kommersant.ru/rubric/2?from=burger',
         'world': 'https://www.kommersant.ru/rubric/5?from=burger',
         'business': 'https://www.kommersant.ru/rubric/4?from=burger',
         'finance': 'https://www.kommersant.ru/finance?from=burger',
         'potrebitelskiy_rynok': 'https://www.kommersant.ru/rubric/41?from=burger'
         }


def kommersant_get_hrefs(href):
    r = requests.get(href)
    html = BS(r.content, 'html.parser')

    news = html.find("main")
    news = news.find_all('section', class_='main grid')

    for n in news:
        k = n.find_all("div", class_='rubric_lenta')
        for rubric in k:
            r = rubric.find_all('article', class_='uho rubric_lenta__item js-article')
            for t in r:
                print(t.get('data-article-url'))


for i in hrefs:
    print(kommersant_get_hrefs(hrefs[i]))
