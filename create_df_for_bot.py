import csv
from parser.tj import *
from parser.lenta import *
from parser.commersant import *
from parser.consultant import *
from parser.ixbt import *
from parser.banki import *
from parser.ria import *


def parse(f_text, f_title, f_lead_text, get_hrefs, href):
    str_links = get_hrefs
    for str_link in str_links:
        print(str_link)
        try:
            r = requests.get(f'{href}{str_link}')
            html = BS(r.content, 'html.parser')
            text = f_text(html)
            title = f_title(html)
            lead_text = f_lead_text(html)

            writer.writerow((text, title, lead_text, f'{href}{str_link}', 0))
        except:
            continue


istochniki = [[tj_text, tj_title, tj_lead_text, tj_get_hrefs(), 'https://journal.tinkoff.ru/'],
              [lenta_text, lenta_title, lenta_lead_text, lenta_get_hrefs(1), 'https://lenta.ru'],
              [cms_text, cms_title, cms_lead_text, kommersant_get_hrefs(), ''],
              [consultant_text, consultant_title, consultant_lead_text, consultant_get_hrefs(1), 'http://www.consultant.ru'],
              [ixbt_text, ixbt_title, ixbt_lead_text, ixbt_get_hrefs(), 'https://www.ixbt.com'],
              [banki_text, banki_title, banki_lead_text, banki_get_hrefs(1), 'https://www.banki.ru'],
              [ria_text, ria_title, ria_lead_text, ria_get_hrefs(), '']]


def start_parse():
    with open("csv_file.csv", "w", encoding="cp1251") as file:
        writer = csv.writer(file)
        writer.writerow(("text", "title", "lead_text", "href", "rating"))
        for i in range(0, len(istochniki)):
            parse(*istochniki[i])
