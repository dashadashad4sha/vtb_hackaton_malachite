import requests
from bs4 import BeautifulSoup as BS
import csv
from create_dataset import create
from tj import *
from lemmanization import human_to_computer


def parse(f_text, f_title, f_lead_text, f_tags, f_views, href):
    with open("csv_file.csv", "w", encoding="cp1251") as file:  # Эти костыли надо срочно переделывать.
        writer = csv.writer(file) # Я хз как, но каждый раз бд перезаписывается заново
        create(("human_text", "machine_text", "title", "tags", "undername", "href", "views", "comments", "for_who"),
               writer)

        str_links = tj_get_hrefs()
        for str_link in str_links:
            r = requests.get(f'https://journal.tinkoff.ru{str_link}')
            html = BS(r.content, 'html.parser')
            print(str_link)
            text = f_text(html)
            title = f_title(html)
            undername = f_lead_text(html)
            tags = f_tags(html)
            views = f_views(html)
            writer.writerow((text, 0, title, tags, undername, str_link, views, 0, 0))


def main():
    parse(tj_text, tj_title, tj_lead_text, tj_tags, tj_views, 'https://journal.tinkoff.ru/')


if __name__ == '__main__':
    main()
