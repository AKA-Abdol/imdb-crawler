import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import sys
import os

# Add the parent directory of 'common' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from common.getters import getTexts, getTextByIndex

# from selenium.webdriver.support import expected_conditions as EC

def getDetail(element: WebElement):
    return {
        "duration": getTextByIndex(element, By.CLASS_NAME, "ipc-title__text", 4),
        "genres": getTexts(
            element.find_element(By.CLASS_NAME, "ipc-chip-list__scroller"),
            By.CLASS_NAME,
            "ipc-chip__text",
        ),
        "stars": getTexts(
            element.find_element(
                By.CLASS_NAME, "ipc-metadata-list-item__content-container"
            ),
            By.CLASS_NAME,
            "ipc-metadata-list-item__list-content-item",
        ),
    }


url = "https://www.imdb.com/title/tt10541088/?ref_=sr_t_1"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
print(getDetail(driver.find_element(By.CLASS_NAME, "ipc-page-content-container")))
# df = pd.DataFrame(dataset)
# df.to_csv("./out_final2.csv")
driver.quit()
