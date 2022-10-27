from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Beatriz")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Dile")

my_mail = driver.find_element(By.NAME, "email")
my_mail.send_keys("beatriz@gmail.com")

button = driver.find_element(By.XPATH, "/html/body/form/button")
button.click()
