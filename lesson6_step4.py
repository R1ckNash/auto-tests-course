from selenium import webdriver
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element_by_tag_name('[name="first_name"]')
    button_1.send_keys("Ivan")

    button_2 = browser.find_element_by_name(name='last_name')
    button_2.send_keys("Petrov")

    button_3 = browser.find_element_by_class_name('form-control.city')
    button_3.send_keys("Smolensk")

    button_4 = browser.find_element_by_css_selector('.form-group:nth-child(4) #country')
    button_4.send_keys("Russia")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(30)
    browser.quit()
