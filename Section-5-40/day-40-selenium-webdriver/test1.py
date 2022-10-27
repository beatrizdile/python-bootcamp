from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Midnight-5/dp/B094WL86N5/ref=sr_1_1?crid=7YVSNUZWFMX5&keywords=dual%2Bsense&qid=1666730901&qu=eyJxc2MiOiIyLjY1IiwicXNhIjoiMi4yMiIsInFzcCI6IjIuMjAifQ%3D%3D&sprefix=dual%2Bsense%2Caps%2C199&sr=8-1&th=1")

price = driver.find_element("id", "priceblock_ourprice")
print(price.text)

search_bar = driver.find_element("q")
print(search_bar.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME, "nav-logo-link nav-progressive-attribute")

documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, '//*[@id="contextualIngressPtLabel_deliveryShortLine"]/span[1]')
print(bug_link.text)