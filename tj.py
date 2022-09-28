from lemmanization import human_to_computer


def tj_title(html_code):
    try:
        text = html_code.find("h1", class_="article-header__title").text.encode().decode('cp1251', 'ignore')
    except:
        return
    return text


def tj_text(html_code):
    try:
        text = html_code.find("div", class_="article-body").text[:2000].encode().decode('cp1251', 'ignore')
    except:
        return tj_lead_text(html_code)
    return text


def tj_lead_text(html_code):
    try:
        text = html_code.find("p", class_="lead").text.encode().decode('cp1251', 'ignore')
    except:
        return tj_title(html_code)
    return text


def tj_tags(html_code):
    try:
        text = html_code.find_all("a", class_="_3YMaz")
    except:
        return
    ans = []
    for i in text:
        ans.append(i.text.encode().decode('cp1251', 'ignore'))
    return ans


def tj_views(html_code):
    try:
        text = html_code.find("div", class_="_27USv _3KBfn").text  #.encode().decode('cp1251', 'ignore')
    except:
        return
    if text[-1] == "K":
        text = int(text[:-1]) * 1000
    return text
