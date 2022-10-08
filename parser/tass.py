from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def tass_get_hrefs():
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


def tass_title(html_code):  # функцию можно проверить мб на None
    try:
        text = html_code.find("div", class_="NewsHeader_title__XjZLk").find('h1').text
        return text
    except Exception as e:
        print('The scraping job failed. ria_title: ')
        print(e)


def tass_text(html_code):
    try:
        html = html_code.find("article")
        blocks_of_text = html.find_all(class_="Paragraph_paragraph__nYCys")
        # .text[:2000].encode().decode('cp1251', 'ignore')

        return ' '.join([e.text for e in blocks_of_text])
    except Exception as e:
        print('The scraping job failed. ria_text: ')
        print(e)


def tass_lead_text(html_code):
    try:
        text = html_code.find("div", class_="NewsHeader_lead__6Z9If")
        if text is None:
            return None
        else:
            text = text.text
            return text
    except Exception as e:
        print('The scraping job failed. ria_lead_text: ')
        print(e)


def tass_tags(html_code):
    text = None
    try:
        text = html_code.find_all("a", class_="Tags_tag__tRSPs")
    except Exception as e:
        print('The scraping job failed. ria_tags: ')
        print(e)
    if text is None:
        return None
    ans = []
    for i in text:
        ans.append(i.text)
    return ans


def tass_views(html_code):
    try:
        text = html_code.find('div', class_="article__info-statistic")
        if text is None:
            return None
        else:
            text = text.text
            if text[-1] == "K":
                text = int(text[:-1]) * 1000
                return text
    except Exception as e:
        print('The scraping job failed. ria_views: ')
        print(e)
