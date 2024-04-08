from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.edge.service import Service as EdgeService

options = Options()
# options.add_argument("--headless")
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--enable-chrome-browser-cloud-management')
# options.add_experimental_option('useAutomationExtension', False)

service = EdgeService()
webdriver = webdriver.Edge(options=options, service=service)
url = "https://spb.cian.ru/kupit-kvartiru/"
webdriver.get(url)
soup = BeautifulSoup(webdriver.page_source, 'html.parser')
cards = list(soup.body.find_all('article'))

for card in cards:
    print(card)
