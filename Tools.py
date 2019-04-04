
import time
from selenium.common.exceptions import NoSuchElementException



def findItem(driver,identifyBy, c):
    '''
    Determine
    whether
    elements
    exist
    Usage:
    isElement(By.XPATH, "//a")
    '''
    time.sleep(1)
    flag = None
    try:
        if identifyBy == "id":
            driver.find_element_by_id(c)
        elif identifyBy == "xpath":
            driver.find_element_by_xpath(c)
        elif identifyBy == "class":
            driver.find_element_by_class_name(c)
        elif identifyBy == "link text":
            driver.find_element_by_link_text(c)
        elif identifyBy == "partial link text":
            driver.find_element_by_partial_link_text(c)
        elif identifyBy == "name":
            driver.find_element_by_name(c)
        elif identifyBy == "tag name":
            driver.find_element_by_tag_name(c)
        elif identifyBy == "css selector":
            driver.find_element_by_css_selector(c)
        elif identifyBy == "accessibility id":
            driver.find_element_by_accessibility_id(c)
        flag = True
    except NoSuchElementException:
        flag = False
    finally:
        return flag



