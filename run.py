from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from urllib.request import urlretrieve

options = Options()
options.add_argument("--disable-notifications")

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome(options=options)

# 開啟 Pchome 首頁
browser.get("https://24h.pchome.com.tw/?gclid=CjwKCAjww5r8BRB6EiwArcckC1ltizGmpoNB0xeL7V2-Fuh-4NkxtIfMCMTGbaAt-bffMHt6v1viDRoCSdAQAvD_BwE")

time.sleep(0.5)

# 尋找網頁中的搜尋框
inputElement = browser.find_element_by_id("keyword")
time.sleep(0.5)

# 在搜尋框中輸入文字
inputElement.send_keys("藍牙耳機")
time.sleep(0.5)

# 送出搜尋
search = browser.find_element_by_id("doSearch")
search.click()
time.sleep(1)

for x in range(0, 4):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

content = BeautifulSoup(browser.page_source, 'html.parser')
images = content.select(".prod_img > img")

for image in images:
    imgName = image['src'].split('/')[4]
    print(imgName + ".jpg")
    urlretrieve("https:" + image['src'], "images/" + imgName + ".jpg")

browser.quit()