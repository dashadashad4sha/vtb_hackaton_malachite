import requests
from bs4 import BeautifulSoup as BS


def ixbt_get_hrefs():
    try:
        r = requests.get(f'https://www.ixbt.com/')
        html = BS(r.content, 'html.parser')
        html = html.find("div", class_="g-grid_column g-grid_column__middle grid-slide-right")
        href_in_code = html.find_all("a", class_="hyphens") #Есть и другие новости, но я не буду брать все. Сайт делал криворучка
        str_links = []
        for i in href_in_code:
            str_links.append(str(i.get("href")))
        return str_links
    except:
        return []


def ixbt_title(html_code):
    try:
        text = html_code.find("h1", itemprop="name").text #.encode().decode('cp1251', 'ignore')
    except:
        return
    return text


def ixbt_lead_text(html_code):
    try:
        text = html_code.find("h4").text.encode().decode('cp1251', 'ignore')
    except:
        return ixbt_title(html_code)
    return text


def ixbt_text(html_code):
    try:
        text = html_code.find("div", class_="b-article__content").text[:2000].encode().decode('cp1251', 'ignore')
    except:
        return ixbt_lead_text(html_code)
    return text


def consultant_tags(html_code):
    try:
        text = html_code.find_all("a", class_="news-tag")
    except:
        return
    ans = []
    for i in text:
        ans.append(i.text).encode().decode('cp1251', 'ignore')
    return ans


def consultant_views(html_code):
    return 2000
