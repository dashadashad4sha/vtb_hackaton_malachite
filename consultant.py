import requests
from bs4 import BeautifulSoup as BS


def consultant_get_hrefs(page_number):
    try:
        r = requests.get(f'http://www.consultant.ru/legalnews/?page={page_number}')
        html = BS(r.content, 'html.parser')
        href_in_code = html.find_all("a", class_="listing-news__item-title")
        str_links = []
        for i in href_in_code:
            str_links.append(str(i.get("href")))
        return str_links
    except:
        return []


def consultant_title(html_code):
    try:
        text = html_code.find("h1", class_="news-page__title").text.encode().decode('cp1251', 'ignore')
    except:
        return
    return text


def consultant_text(html_code):
    try:
        text = html_code.find("div", class_="news-page__text").text.encode().decode('cp1251', 'ignore')
    except:
        return consultant_lead_text(html_code)
    return text


def consultant_lead_text(html_code):
    return consultant_title(html_code)


def consultant_tags(html_code):
    try:
        text = html_code.find_all("span", class_="tags-news__item")
    except:
        return
    ans = []
    for i in text:
        ans.append(i.text).encode().decode('cp1251', 'ignore')
    return ans


def consultant_views(html_code):
    return 2000
