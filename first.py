from selenium import webdriver
import os
import time

useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/79.0.3945.8 Chrome/79.0.3945.8 Safari/537.36"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--allow-popups-during-page-unload")
chrome_options.add_argument("--disable-background-timer-throttling")
chrome_options.add_argument(f'user-agent={useragent}')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.get("https://k1dragon.blogspot.com/")
print("Opened the website")
driver.find_element_by_link_text("New Post").click()
time.sleep(5)
driver.find_element_by_link_text("link").click()
time.sleep(1700)

driver.quit()

print("Finished !")
