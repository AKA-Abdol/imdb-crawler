import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver 

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
import math


def getText(element: WebElement, by: By, by_value: str):
    try:
        return element.find_element(by, by_value).text
    except Exception:
        return ""


def getAttribute(element: WebElement, attribute_name: str):
    try:
        return element.get_attribute(attribute_name)
    except Exception:
        return ""


def clickNTimes(data_count, driver: WebDriver):
    PAGINATION_LIMIT = 50
    click_count = math.ceil(data_count / PAGINATION_LIMIT)
    more_button = driver.find_element(By.CLASS_NAME, "ipc-see-more")
    for i in range(click_count):
        time.sleep(5)
        driver.execute_script(
            """
        const button = document.getElementsByClassName('ipc-see-more')[0];
        button.scrollIntoView();
        """
        )
        time.sleep(1)
        while True:
            try:
                more_button.click()
                break
            except Exception:
                time.sleep(1)
                print('retrying clicking ...')



def getListItemData(element: WebElement):
    return {
        "title": getText(element, By.CLASS_NAME, "ipc-title__text"),
        "year": getText(element, By.CLASS_NAME, "dli-title-metadata-item"),
        "rating": getText(element, By.CLASS_NAME, "ratingGroup--imdb-rating"),
        "content": getText(element, By.CLASS_NAME, "ipc-html-content-inner-div"),
        "link": getAttribute(
            element.find_element(By.CLASS_NAME, "ipc-title-link-wrapper"), "href"
        ),
    }


url = "https://www.imdb.com/search/title/?title_type=tv_series&user_rating=6,10&genres=reality-tv&sort=num_votes,desc"
data_count = 6800

driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
clickNTimes(data_count, driver)

elems = driver.find_elements(By.CLASS_NAME, "dli-parent")
dataset = []
for idx, elem in enumerate(elems):
    dataset.append(getListItemData(elem))
    if idx != 0 and idx % 50 == 49:
        print(f'progress {"{:.2f}".format((idx + 1) / len(elems))}%')

df = pd.DataFrame(dataset)
df.to_csv("./out_final2.csv")
driver.quit()
