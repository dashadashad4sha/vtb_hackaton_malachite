import requests
from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def iz_get_hrefs():
    # try:
    #     r = requests.get('https://iz.ru/xml/rss/all.xml')
    #     soup = BS(r.content, features='xml')
    #     articles = soup.find_all('item')
    #     str_links = []
    #     for a in articles:
    #         link = a.find('link').text
    #         str_links.append(link)
    #     return str_links
    # except Exception as e:
    #     print('The scraping job failed. iz_get_hrefs: ')
    #     print(e)

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(10)
        driver.get('https://tass.ru/rss/v2.xml')
        html = driver.page_source
        soup = BS(html, features='xml')
        articles = soup.find_all('item')
        str_links = []
        for a in articles:
            link = a.find('link').text
            str_links.append(link)
        return str_links
    except Exception as e:
        print('The scraping job failed. ria_get_hrefs: ')
        print(e)


def iz_title(html_code):  # функцию можно проверить мб на None
    try:
        text = html_code.find("div", class_="top_big_img_article__info__inside__title").find('h1').text
        return text
    except Exception as e:
        print('The scraping job failed. iz_title: ')
        print(e)


def iz_text(html_code):
    try:
        html = html_code.find("div", class_="text-article__inside")
        blocks_of_text = html.find_all('p')
        # .text[:2000].encode().decode('cp1251', 'ignore')

        return ' '.join([e.text for e in blocks_of_text])
    except Exception as e:
        print('The scraping job failed. iz_text: ')
        print(e)


def iz_lead_text(html_code):
    try:
        text = html_code.find("div", class_="top_big_img_article__info__inside__description").text
        return text
    except Exception as e:
        print('The scraping job failed. iz_lead_text: ')
        print(e)


def iz_tags(html_code):
    text = None
    try:
        text = html_code.find("div", class_="hash_tags").find_all('a')
    except Exception as e:
        print('The scraping job failed. iz_tags: ')
        print(e)
    if text is None:
        return None
    ans = []
    for i in text:
        ans.append(i.text)
    return ans


def iz_views(html_code):  # !TODO
    return None
