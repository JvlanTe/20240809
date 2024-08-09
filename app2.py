from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

# .envを使う宣言
load_dotenv()

# Chromeを使う宣言
driver = webdriver.Chrome()

# .envの変数を使うよ（パスワードとか見れないようなやつ）
URL = os.getenv("URL")
email = os.getenv("email")
password = os.getenv("password")

time.sleep(3)

try:
    driver.get(URL)

    email_input = driver.find_element(By.NAME, "email")

    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys(email)

    password_input.send_keys(password)

    time.sleep(3)

    # どうやらシングルクォーテーションでないといけないらしい
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    login_button.click()

    time.sleep(3)

    download_link = driver.find_element(By.LINK_TEXT, "ファイルをダウンロード")

    download_link.click()

    time.sleep(5)

finally:
    driver.quit()
