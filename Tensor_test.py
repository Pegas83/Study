from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://yandex.ru/")

search_field = browser.find_element(By.XPATH, '//*[@id="text"]')
search_field.send_keys("Тензор")


def test_search_field():
    # search_field = browser.find_element(By.XPATH, '//*[@id="text"]')
    assert search_field, "There is no search field"
    # search_field.send_keys("Тензор")


# search_field = browser.find_element(By.XPATH, '//*[@id="text"]')
# search_field.send_keys("Тензор")

def test_suggest():
    suggest = browser.find_element(By.XPATH, '/html/body/div[3]')
    assert suggest, "Suggest didn't appear"


time.sleep(3)
search_field.send_keys(Keys.RETURN)


def test_search_result():
    search_result = browser.find_element(By.XPATH, '//*[@id="search-result"]')
    assert search_result, "Search result didn't appear"


def test_first_5_links_to_tensor():
    links = browser.find_elements(By.CSS_SELECTOR, '.Path.Organic-Path.organic__path > a > b')
    link_list = [elem.text for elem in links[:5]]
    tensor_number = link_list.count('tensor.ru')
    assert tensor_number == 5, f'There are no first five links leading to tensor.ru. Only {tensor_number} of them'

# time.sleep(3)
# browser.close()
# //*[@id="search-result"]/li[2]/div/div[1]/div[1]/a/b
# //*[@id="search-result"]/li[1]/div/div[1]/div[1]/a/b
# //*[@id="search-result"]/li[1]/div/div[1]/div[1]

# Path Organic-Path Organic-Path_verified path organic__path
# //*[@id="search-result"]/li[1]/div/div[1]/div[1]/div[1]
#
# Path Organic-Path path organic__path
# //*[@id="search-result"]/li[2]/div/div[1]/div[1]
#
# Path Organic-Path path organic__path
# //*[@id="search-result"]/li[3]/div/div[1]/div[1]
