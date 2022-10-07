import requests
from bs4 import BeautifulSoup as BS


def ria_get_hrefs():
    try:
        r = requests.get('https://ria.ru/export/rss2/archive/index.xml')
        soup = BS(r.content, features='xml')
        articles = soup.find_all('item')
        str_links = []
        for a in articles:
            link = a.find('link').text.encode().decode('cp1251', 'ignore')
            str_links.append(link)
        return str_links
    except Exception as e:
        print('The scraping job failed. ria_get_hrefs: ')
        print(e)


def ria_title(html_code):  # функцию можно проверить мб на None
    try:
        text = html_code.find("div", class_="article__title").text.encode().decode('cp1251', 'ignore')
        return text
    except Exception as e:
        print('The scraping job failed. ria_title: ')
        print(e)


def ria_text(html_code):
    try:
        html = html_code.find("div", class_="article__body js-mediator-article mia-analytics")
        blocks_of_text = html.find_all(class_="article__block")
        # .text[:2000].encode().decode('cp1251', 'ignore')

        return ' '.join([e.text.encode().decode('cp1251', 'ignore') for e in blocks_of_text])
    except Exception as e:
        print('The scraping job failed. ria_text: ')
        print(e)


def ria_lead_text(html_code):
    try:
        text = html_code.find("h1", class_="article__second-title").text.encode().decode('cp1251', 'ignore')
        return text
    except Exception as e:
        print('The scraping job failed. ria_lead_text: ')
        print(e)


def ria_tags(html_code):
    text = None
    try:
        text = html_code.find_all("a", class_="article__tags-item")
    except Exception as e:
        print('The scraping job failed. ria_tags: ')
        print(e)
    if text is None:
        return None
    ans = []
    for i in text:
        ans.append(i.text.encode().decode('cp1251', 'ignore'))
    return ans


def ria_views(html_code):  # не работает, так как грузится динамически
    return 2000
