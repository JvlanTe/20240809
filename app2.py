from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chromeを使う宣言
driver = webdriver.Chrome()

time.sleep(3)

try:
    driver.get("https://plotacademy.jp/login")

    email_input = driver.find_element(By.NAME, "email")

    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys("test1@test.jp")

    password_input.send_keys("test1111")

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
