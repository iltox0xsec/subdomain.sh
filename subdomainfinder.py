from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import sys

# Domaini komut satırı argümanından al
domain = sys.argv[1]


# WebDriver'ı başlat
driver = webdriver.Chrome()

# Hedef URL
url = 'https://subdomainfinder.c99.nl/'

# Web sayfasını aç
driver.get(url)

# Domaini kullanıcıdan al

# Input alanını bul ve veriyi gönder
input_element = driver.find_element("name", "domain")
input_element.send_keys(domain)

# "Enter" tuşunu simüle etmek için ActionChains kullan
actions = ActionChains(driver)
actions.move_to_element(input_element)
actions.click(input_element)
actions.perform()


# Butonu bul ve tıklamak için bekleyelim
button = driver.find_element("name", "scan_subdomains")
button.click()

# 5 saniye bekleyelim
time.sleep(5)

# HTML içeriğini alalım
html_content = driver.page_source

# BeautifulSoup ile HTML içeriğini parse edelim
soup = BeautifulSoup(html_content, 'html.parser')

# Tabloyu bulalım
table_div = soup.find('div', {'class': 'table-responsive'})

# Tablonun içindeki verileri alalım
if table_div:
    table_rows = table_div.find_all('tr')
    for row in table_rows:
        columns = row.find_all('td')
        for column in columns:
            print(column.text.strip())
else:
    print("Tablo bulunamadı.")


# WebDriver'ı kapat
driver.quit()
