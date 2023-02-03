import traceback

from django.test import TestCase

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from package.logger import Logger
log = Logger('/django/app/tests.py')

log.debug('PASS')

chrome_options = Options()
desired_capabilities = chrome_options.to_capabilities()

driver = webdriver.Remote(
    command_executor='http://selenium:4444/wd/hub',
    desired_capabilities=desired_capabilities
)

url = 'http://nginx:8000/'

driver.get(url)
log.debug(driver.current_url)

# なにかの処理
try:
    # 要素が見つかるまで30秒待機
    log.debug('WAIT')
    WebDriverWait(driver, 30).until(
        expected_conditions.presence_of_element_located((By.TAG_NAME, 'h1'))
    )
except:
    # 要素が見つからなかったら終了
    driver.close()
    driver.quit()
    traceback.print_exc()

# 要素が見つかったら要素内のテキストを取得
text = driver.find_element(By.TAG_NAME, 'h1').text
log.debug(text)

driver.close()
driver.quit()
