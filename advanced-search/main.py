import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def clickNTimes(data_count, driver):
    PAGINATION_LIMIT = 50
    click_count = math.ceil(data_count / PAGINATION_LIMIT)
    more_button = driver.find_element(By.CLASS_NAME, 'ipc-see-more')
    for i in range(click_count):
        time.sleep(5)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        more_button.click()

def getListItemData(element):
    try:
        content = element.find_element(By.CLASS_NAME, 'dli-plot-container').find_element(By.CLASS_NAME, 'ipc-html-content-inner-div').text
    except: 
        content = ''
    return {
        'title': element.find_element(By.CLASS_NAME, 'ipc-title__text').text,
        'year': element.find_element(By.CLASS_NAME, 'dli-title-metadata-item').text,
        'rating': element.find_element(By.CLASS_NAME, 'ratingGroup--imdb-rating').text,
        'content': content,
        'link': element.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper').get_attribute('href')
    }


url = 'https://www.imdb.com/search/title/?user_rating=6,10&genres=reality-tv'
data_count = 1000

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
clickNTimes(data_count, driver)

elems = driver.find_elements(By.CLASS_NAME, 'dli-parent')
dataset = []
for elem in elems:
    dataset.append(getListItemData(elem))
df = pd.DataFrame(dataset)
df.to_csv('./out.csv')
driver.quit()