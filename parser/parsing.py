import requests
from bs4 import BeautifulSoup as BS
import csv
from tj import *
from lenta import *
from commersant import *
from consultant import *
from ixbt import *
from banki import *
from ria import *


def parse(f_text, f_title, f_lead_text, f_tags, f_views, get_hrefs, href):
    str_links = get_hrefs
    for str_link in str_links:
        try:
            r = requests.get(f'{href}{str_link}')
            html = BS(r.content, 'html.parser')
            print(str_link)
            text = f_text(html)
            title = f_title(html)
            undername = f_lead_text(html)
            tags = f_tags(html)
            views = f_views(html)
            writer.writerow((text, 0, title, tags, undername, f'{href}{str_link}', views, 0))
        except:
            continue


istochniki = [[ria_text, ria_title, ria_lead_text, ria_tags, ria_views, ria_get_hrefs(), ''],
              [tj_text, tj_title, tj_lead_text, tj_tags, tj_views, tj_get_hrefs(), 'https://journal.tinkoff.ru/'],
              [lenta_text, lenta_title, lenta_lead_text, lenta_tags, lenta_views, lenta_get_hrefs(1),
               'https://lenta.ru'], #именно этот источник работает супер медленно, его можно бует удалить
              [cms_text, cms_title, cms_lead_text, cms_tags, cms_views, kommersant_get_hrefs(), ''],
              [consultant_text, consultant_title, consultant_lead_text, consultant_tags,
               consultant_views, consultant_get_hrefs(1), 'http://www.consultant.ru'],
              [ixbt_text, ixbt_title, ixbt_lead_text, consultant_tags, consultant_views, ixbt_get_hrefs(), 'https://www.ixbt.com'],
              [banki_get_hrefs, banki_title, banki_lead_text, banki_tags, banki_views, banki_get_hrefs(1),
               'https://www.banki.ru']
              ]


with open("csv_file.csv", "w", encoding="cp1251") as file:  # human_text в модельке убираем, это тлько для аналитика
    writer = csv.writer(file)
    writer.writerow(("human_text", "machine_text", "title", "tags", "undername", "href", "views", "rating"))
    for i in range(0, len(istochniki)):
        print(i)
        parse(*istochniki[i])
