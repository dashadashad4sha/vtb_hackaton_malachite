import requests
from bs4 import BeautifulSoup as BS

hrefs = ['https://www.kommersant.ru/rubric/3?from=burger&page=1',
         'https://www.kommersant.ru/rubric/2?from=burger',
         'https://www.kommersant.ru/rubric/5?from=burger',
         'https://www.kommersant.ru/rubric/4?from=burger',
         'https://www.kommersant.ru/finance?from=burger',
         'https://www.kommersant.ru/rubric/41?from=burger'
         ]


def kommersant_get_hrefs(hrefs_cms=hrefs):
    ans = []
    for href in hrefs:

        r = requests.get(href)
        html = BS(r.content, 'html.parser')

        news = html.find("main")
        news = news.find_all('section', class_='main grid')

        for n in news:
            k = n.find_all("div", class_='rubric_lenta')
            for rubric in k:
                r = rubric.find_all('article', class_='uho rubric_lenta__item js-article')
                for t in r:
                    ans.append(t.get('data-article-url'))
    return ans


def cms_title(html_code):
    try:
        text = html_code.find("h1", class_="doc_header__name js-search-mark").text.encode().decode('cp1251', 'ignore')
    except:
        return
    return text


def cms_text(html_code):
    try:
        text = html_code.find("div", class_="doc__body article_text_wrapper js-search-mark").text[:2000].encode().decode('cp1251', 'ignore')
    except:
        return cms_lead_text(html_code)
    return text


def cms_lead_text(html_code):
    try:
        text = html_code.find("h2", class_="doc_header__subheader").text.encode().decode('cp1251', 'ignore')
    except:
        return cms_title(html_code)
    return text


def cms_tags(html_code):
    try:
        text = html_code.find("a", class_="decor").text.encode().decode('cp1251', 'ignore')
    except:
        return
    ans = [text]
    return ans


def cms_views(html_code):
    try:
        text = html_code.find("div", class_="sharing__text").text  # .encode().decode('cp1251', 'ignore')
    except:
        return
    if text[-1] == "K":
        text = int(text[:-1]) * 1000
    return text
