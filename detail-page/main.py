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
from common.getters import getTexts, getTextByIndex, getAttribute, getText

# from selenium.webdriver.support import expected_conditions as EC

def getDetail(element: WebDriver):
    headerSectionElement = element.find_element(By.TAG_NAME, "h1")
    episodesSectionElement = element.find_element(By.ID, "browse-episodes-season").find_element(By.XPATH, '../../../../../..')
    return {
        "duration": headerSectionElement.find_element(By.XPATH, '..').find_elements(By.TAG_NAME, "li")[3].text, 
        "genres": getTexts(
            headerSectionElement.find_element(By.XPATH, '../../..').find_element(By.CLASS_NAME, "ipc-chip-list__scroller"),
            By.CLASS_NAME,
            "ipc-chip__text",
        ),
        "stars": getTexts(
            headerSectionElement.find_element(By.XPATH, '../../..').find_element(
                By.CLASS_NAME, "ipc-metadata-list-item__content-container"
            ),
            By.CLASS_NAME,
            "ipc-metadata-list-item__list-content-item--link",
        ),
        "seasons": getAttribute(element.find_element(By.ID, "browse-episodes-season"), "aria-label").split()[0],
        "episodes": getText(episodesSectionElement, By.CLASS_NAME, "ipc-title__subtext")
    }


url = "https://www.imdb.com/title/tt10541088/?ref_=sr_t_1"
driver = webdriver.Chrome()
driver.get(url)
driver.implicitly_wait(10)
print(getDetail(driver))
# df = pd.DataFrame(dataset)
# df.to_csv("./out_final2.csv")
driver.quit()
