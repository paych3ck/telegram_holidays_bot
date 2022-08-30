import datetime
import requests
import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


def show_holidays():
    now = datetime.datetime.now()
    r = requests.get("https://kakoysegodnyaprazdnik.ru/", headers=headers)
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    holidays = soup.find_all("span", itemprop="text")
    result = f"Праздники {now.strftime('%d.%m.%Y')}:\n"
    for holiday in holidays:
        result += holiday.text + "\n"
    return result
