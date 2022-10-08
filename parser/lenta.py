import requests
from bs4 import BeautifulSoup as BS


def lenta_get_hrefs(page_number): #бязательно обработать исключения в дальнейшем, тк не все ссылки корректны.
    # Для каждой странницы массив свой, они не суммируются
    try:
        r = requests.get(f'https://lenta.ru/parts/news/{page_number}/')
        html = BS(r.content, 'html.parser')
        href_in_code = html.find_all("a", class_="card-full-news _parts-news")
        str_links = []
        for i in href_in_code:
            str_links.append(str(i.get("href")))
        return str_links
    except:
        return []


def lenta_title(html_code):
    try:
        text = html_code.find("span", class_="topic-body__title").text.encode().decode('cp1251', 'ignore')
    except:
        return
    return text


def lenta_text(html_code):
    try:
        text = html_code.find("div", class_="topic-body__content").text[:2000].encode().decode('cp1251', 'ignore')
    except:
        return lenta_lead_text(html_code)
    return text


def lenta_lead_text(html_code):
    try:
        text = html_code.find("div", class_="topic-body__title-yandex").text.encode().decode('cp1251', 'ignore')
    except:
        return lenta_title(html_code)
    return text


def lenta_tags(html_code):
    try:
        text = html_code.find_all("a", class_="rubric-header__link _active")
    except:
        return
    ans = []
    for i in text:
        ans.append(i.text.encode().decode('cp1251', 'ignore'))
    return ans


def lenta_views(html_code):
    return 2000
