import requests
from bs4 import BeautifulSoup as BS


def banki_get_hrefs(page_number):
    try:
        r = requests.get(f'https://www.banki.ru/news/lenta/?page={page_number}')
        html = BS(r.content, 'html.parser')
        href_in_code = html.find_all("a", class_="lf473447f")
        str_links = []
        for i in href_in_code:
            str_links.append(str(i.get("href")))

        return str_links
    except:
        return []


def banki_title(html_code):
    try:
        text = html_code.find("h1", class_="text-header-0").text.encode().decode('cp1251', 'ignore')
    except:
        return
    return text


def banki_text(html_code):
    try:
        text = html_code.find("div", class_="la1303898").text[:2000].encode().decode('cp1251', 'ignore')
    except:
        return banki_lead_text(html_code)
    return text


def banki_lead_text(html_code):
    return banki_title(html_code)


def banki_tags(html_code):
    try:
        text = html_code.find_all("a", class_="_3YMaz")
    except:
        return
    ans = []
    for i in text:
        ans.append(i.text.encode().decode('cp1251', 'ignore'))
    return ans


def banki_views(html_code):
    try:
        texts = html_code.find_all("span", class_="l51e0a7a5") #.encode().decode('cp1251', 'ignore')
        text = texts[1].text
    except:
        return 2000
    return text
