from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://pt.wikipedia.org/wiki/Wiki")

to_click = driver.find_element(By.XPATH, '//*[@id="ca-talk"]/a/span')
to_click.click()

to_write = driver.find_element(By.NAME, "search")
to_write.send_keys("Python")
to_write.send_keys(Keys.ENTER)