from selenium import webdriver

chrome_driver_path = MY_CHROME_DRIVER_PATH

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/PlayStation-DualSense-Wireless-Controller-Midnight-5/dp/B094WL86N5/ref=sr_1_1?crid=7YVSNUZWFMX5&keywords=dual%2Bsense&qid=1666730901&qu=eyJxc2MiOiIyLjY1IiwicXNhIjoiMi4yMiIsInFzcCI6IjIuMjAifQ%3D%3D&sprefix=dual%2Bsense%2Caps%2C199&sr=8-1&th=1")

price = driver.find_element("id", "priceblock_ourprice")
print(price.text)

