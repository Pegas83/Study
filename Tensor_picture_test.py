from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://yandex.ru/")
picture_link = browser.find_element(By.XPATH, "//a[contains(@href, 'https://yandex.ru/images/?utm_source"
                                              "=main_stripe_big')]")


def test_picture_link():
    assert picture_link, 'There is no picture link'


old_tabs = browser.window_handles
picture_link.click()
time.sleep(2)
new_tabs = browser.window_handles
for tab in new_tabs:
    if tab not in old_tabs:
        new_tab = tab
browser.switch_to.window(new_tab)


def test_new_tab_link():
    assert 'https://yandex.ru/images/' in browser.current_url, f"New tab link is not 'https://yandex.ru/images/'. It " \
                                                               f"is '{browser.current_url} "


first_category = browser.find_element(By.CSS_SELECTOR, '.PopularRequestList-Item_pos_0')
first_category_name = first_category.get_attribute('textContent')
time.sleep(3)
old_tabs = browser.window_handles
first_category.click()
time.sleep(2)
new_tabs = browser.window_handles
for tab in new_tabs:
    if tab not in old_tabs:
        new_tab = tab
browser.switch_to.window(new_tab)
search_first_category = browser.find_element(By.XPATH, "//a[contains(text(), 'Поиск')]")
search_first_category.click()
name = browser.find_element(By.CSS_SELECTOR, "div.search2__input span.input__box input.input__control").get_attribute('value')
# time.sleep(2)


def test_correct_text_in_search_field():
    assert first_category_name == name, f'The text in search field is incorrect! Must be: {first_category.text}. Now is: {name}'


browser.switch_to.window(old_tabs[1])
link = browser.find_element(By.XPATH, """//div[@data-grid-position='{"row":0,"col":0}']""")
link.click()

first_picture = browser.find_element(By.XPATH, "//*[@class='MMImage-Origin']")
first_picture_link = first_picture.get_attribute("src")


def test_open_picture():
    assert first_picture, 'Picture is not opened!'


time.sleep(2)
print(first_picture_link)

browser.find_element(By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_next').click()
time.sleep(2)
second_picture = browser.find_element(By.XPATH, "//*[@class='MMImage-Origin']")
second_picture_link = second_picture.get_attribute("src")
print(second_picture_link)


def test_picture_change():
    assert first_picture_link != second_picture_link, "Picture wasn't changed!"


browser.find_element(By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_prev').click()
new_first_picture = browser.find_element(By.XPATH, "//*[@class='MMImage-Origin']")
new_first_picture_link = first_picture.get_attribute("src")
print(new_first_picture_link)
time.sleep(2)
"""Выявлена следующая особенность Яндекс.Картинок:
Ссылка на первую картинку при первом клике по ней и ссылка на нее же после возвращения отличаются!
При повторной смене картинки и возвращения на нее, ссылки совпадают.
Для учета этой особенности выполнен повторный переход с первой картинки на вторую и обратно"""

browser.find_element(By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_next').click()
time.sleep(2)
browser.find_element(By.CSS_SELECTOR, 'div.CircleButton.CircleButton_type_prev').click()
new_first_picture_duplicate = browser.find_element(By.XPATH, "//*[@class='MMImage-Origin']")
new_first_picture_duplicate = first_picture.get_attribute("src")
time.sleep(2)
print(new_first_picture_duplicate)


def test_return_to_the_same_picture():
    assert new_first_picture_duplicate == new_first_picture_link, 'The picture is not the same!'


