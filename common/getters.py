from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def getText(element: WebElement, by: By, by_value: str):
    try:
        return element.find_element(by, by_value).text
    except Exception:
        return ""


def getTexts(element: WebElement, by: By, by_value: str, delim: str = ","):
    try:
        return delim.join([x.text for x in element.find_elements(by, by_value)])
    except Exception:
        return ""


def getTextByIndex(element: WebElement, by: By, by_value: str, idx: int = 0):
    try:
        return element.find_elements(by, by_value)[idx].text
    except Exception:
        return ""


def getAttribute(element: WebElement, attribute_name: str):
    try:
        return element.get_attribute(attribute_name)
    except Exception:
        return ""
