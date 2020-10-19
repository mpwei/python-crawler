from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--disable-notifications")

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 開啟頁面
URL = "http://localhost:8080/"
browser.get(URL)
time.sleep(1)

# 輸入帳號
inputElement = browser.find_element_by_css_selector("#LoginArea input[name='Account']")
inputElement.send_keys("yaon4")
time.sleep(0.5)

# 輸入密碼
inputElement = browser.find_element_by_css_selector("#LoginArea input[name='Password']")
inputElement.send_keys("123456")
time.sleep(0.5)

# 驗證碼處理
# 抓取 backend/captcha/{SR}
SR = int(browser.find_element_by_css_selector("#LoginArea .VerificationFrame > img").get_attribute('src').replace(URL, "").split('/')[2])
pCodeArray = [9697, 3673, 4549, 2671, 5981, 3911, 2243, 9479, 9743, 5981, 4999, 7411, 3259, 7211, 4397, 1789, 4139,
              8923, 8009, 7321, 1973, 7687, 1723, 4253, 7883, 4789, 9049, 3847, 9769, 1511, 1871]
qCodeArray = [8387, 3919, 1279, 5653, 6569, 8297, 6043, 2141, 2341, 2741, 4129, 6967, 3617, 8731, 3947, 9203, 8269,
              9719, 8599, 4973, 7927, 6599, 4159, 7591, 7883, 6959, 6991, 7333, 8837, 6277, 7901]
nowDateMinus = int(time.strftime('%d')) - 1
pCodeM = pCodeArray[nowDateMinus] - 1
qCodeM = qCodeArray[nowDateMinus] - 1
randCode = int(SR / (pCodeM * qCodeM))
checkCode = int(randCode * (pCodeM + 1) / 1000)

# 輸入驗證碼
inputElement = browser.find_element_by_css_selector("#LoginArea input[name='VerificationCode']")
inputElement.send_keys(checkCode)
time.sleep(0.5)

# 登入
browser.find_element_by_id("LoginArea").submit()
time.sleep(5)

browser.quit()