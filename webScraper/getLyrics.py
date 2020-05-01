from .webscraper import ChromeDriverBrowser

CHROMEDRIVER_PATH = "/Users/dhars/Downloads/chromedriver_win32/chromedriver"
SEARCH_URL = "https://www.ultimate-guitar.com/search.php?search_type=title&value="

SEARCH_TAG = "div"
SEARCH_ATTRIBUTE = "class" 
SEARCH_ATTRIBUTE_VALUE = "_31dWM"
REVIEWS_XPATH = "//"+SEARCH_TAG+"[@"+SEARCH_ATTRIBUTE+"='"+SEARCH_ATTRIBUTE_VALUE+"']"
REVIEWS_CLASS_NAME = "_31dWM"
VERSIONS_XPATH = "//div[@class='pZcWD']"
LINKS_XPATH = "//a[@class='_2KJtL _1mes3 kWOod']"
LINKS_CLASS_NAME = "_2KJtL _1mes3 kWOod"
CONTENT_XPATH = "//span[@class='_1zlI0']"
TIMEOUT = 10
a_tag = 'a'

def get_content(SEARCH_KEY) -> str:

    SEARCH_URL = "https://www.ultimate-guitar.com/search.php?search_type=title&value="

    list_of_search_words = SEARCH_KEY.split(' ')
    if(len(list_of_search_words) > 1):
        SEARCH_URL = SEARCH_URL + list_of_search_words.pop(0)
        for item in list_of_search_words:
            SEARCH_URL = SEARCH_URL + "%20" + item
    else:
         SEARCH_URL = SEARCH_URL + list_of_search_words[0]

    browser = ChromeDriverBrowser(CHROMEDRIVER_PATH)
    if(browser.load_url(SEARCH_URL, REVIEWS_XPATH,TIMEOUT) == False):
        return
    
    versions = browser.get_elements_by_XPATH(VERSIONS_XPATH)

    review_elements = browser.get_child_elements_by_class_name(versions, REVIEWS_CLASS_NAME)
    review_string_list = [browser.get_elements_as_text(review_element) for review_element in review_elements]
    review_strings = [''.join(x) for x in review_string_list]
    no_of_reviews = [convert_string_to_number(review) for review in review_strings]

    max_review = max(no_of_reviews)
    max_review_index = no_of_reviews.index(max_review)

    link_element = browser.get_child_element_by_tag_name(versions[max_review_index], a_tag)
    link = browser.get_link_from_element(link_element)

    if(browser.load_url(link, CONTENT_XPATH, TIMEOUT) == False):
        return

    content_elements = browser.get_elements_by_XPATH(CONTENT_XPATH)
    content = browser.get_elements_as_text(content_elements)

    return ('\n'.join(content))

def convert_string_to_number(item) -> int:
    if item:
        str = item.translate({ord(','): None})
        num = int(str)
        return num
    return 0
    