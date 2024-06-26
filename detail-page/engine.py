import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    try:
        episodesSectionElement = element.find_element(By.ID, "browse-episodes-season").find_element(By.XPATH, '../../../../../..')
    except:
        episodesSectionElement = None
        
    preReviewCardElement = element.find_elements(By.CLASS_NAME, "ipc-icon--more-vert")
    if len(preReviewCardElement) == 0:
        review = ''
    else:
        preReviewCardElementIdx = 1 if len(preReviewCardElement) > 1 else 0
        reviewCardElement = preReviewCardElement[preReviewCardElementIdx].find_element(By.XPATH, '../../../../..')
        review = getText(reviewCardElement, By.CLASS_NAME, "ipc-html-content-inner-div")
    try:
        seasonCount = getAttribute(element.find_element(By.ID, "browse-episodes-season"), "aria-label").split()[0]
    except:
        seasonCount = 1

    return {
        "duration": headerSectionElement.find_element(By.XPATH, '..').find_elements(By.TAG_NAME, "li")[-1].text, 
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
        "seasons": seasonCount,
        "episodes": '1' if episodesSectionElement == None else getText(episodesSectionElement, By.CLASS_NAME, "ipc-title__subtext"),
        "review": review
    }

def getDetailByLink(url: str):
    # options = Options()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome()#options=options)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    detail = getDetail(driver)
    driver.quit()
    return detail

# url = "https://www.imdb.com/title/tt10541088/?ref_=sr_t_1"
# driver = webdriver.Chrome()
# driver.get(url)
# driver.implicitly_wait(10)
# print(getDetail(driver))
# df = pd.DataFrame(dataset)
# df.to_csv("./out_final2.csv")
# driver.quit()
