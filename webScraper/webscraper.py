from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException


class ChromeDriverBrowser:

    def __init__(self, CHROMEDRIVER_PATH):
        option = webdriver.ChromeOptions()
        option.add_argument(" - icognito")

        self.browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=option)

    def load_url(self, URL, XPATH, timeout) -> bool:
        self.browser.get(URL)

        # Wait 10 seconds for page to load
        try:
            WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((By.XPATH, XPATH)))
        except TimeoutException:
            print("Timed out waiting for page to load")
            return (bool(False))
        return (bool(True))

    def get_elements_by_XPATH(self, XPATH) -> list:
        elements = self.browser.find_elements_by_xpath(XPATH)
        return elements

    def get_child_elements_by_class_name(self, elements, class_name) -> list:
        child_elements = [element.find_elements_by_class_name(class_name) for element in elements]
        return child_elements

    def get_child_element_by_tag_name(self, element, tag_name) -> str:
        child_element = element.find_element_by_tag_name(tag_name)
        return child_element

    def get_elements_as_text(self, element) -> list:
        text = [x.text for x in element]
        return text

    def get_link_from_element(self, element) -> str:
        link = element.get_attribute("href")
        return link

    def __del__(self):
        self.browser.quit()