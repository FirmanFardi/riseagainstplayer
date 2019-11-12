import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='C:/FYP/chromedriver.exe')

browser.get("https://store.ubi.com/sea/all-games?lang=en_SG")
time.sleep(1)
browser.maximize_window()
elem = browser.find_element_by_tag_name("body")

no_of_pagedowns = 20

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

while True:
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'load-more-button button btn-dblue tag-commander-event')]")))
        browser.find_element_by_xpath("//button[contains(@class, 'load-more-button button btn-dblue tag-commander-event')]").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'load-more-button button btn-dblue tag-commander-event')]")))
    except Exception as e:
        print(e)
        break


game = browser.find_element_by_class_name("samples")
post_elems = game.find_elements_by_xpath("//div[@class='product-tile card    full-tile-link']/a[@href]")

for post in post_elems:
    print ( post.get_attribute("href"))