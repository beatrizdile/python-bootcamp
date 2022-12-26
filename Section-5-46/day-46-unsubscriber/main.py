from selenium.common import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException, \
    ElementClickInterceptedException, TimeoutException
from urllib.error import ContentTooShortError
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


driver = uc.Chrome()
wait = WebDriverWait(driver, 20, ignored_exceptions=(TimeoutException, ContentTooShortError, ElementClickInterceptedException, NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException))


driver.get("https://www.youtube.com/@kurzgesagt/videos")

sing_in = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]'))
)
sing_in.click()

email = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'))
)
email.send_keys(os.environ["EMAIL"])

the_next = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))
)
the_next.click()

password = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input'))
)
password.send_keys(os.environ["PASSWORD"])

other_next = wait.until(
    EC.presence_of_element_located((By.XPATH,
                                    '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'))
)
other_next.click()


while True:
    options = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[1]/yt-icon-button[2]'))
    )
    options.click()

    channel = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item/yt-formatted-string'))
    )
    channel.click()

    un_sub_1 = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[5]/ytd-subscribe-button-renderer/div[2]/ytd-subscription-notification-toggle-button-renderer-next/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]'))
    )
    un_sub_1.click()

    un_sub_2 = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-menu-popup-renderer/tp-yt-paper-listbox/ytd-menu-service-item-renderer[4]/tp-yt-paper-item/yt-formatted-string'))
    )
    un_sub_2.click()

    un_sub_3 = wait.until(
        EC.presence_of_element_located((By.XPATH,
                                        '/html/body/ytd-app/ytd-popup-container/tp-yt-paper-dialog/yt-confirm-dialog-renderer/div[2]/div[2]/yt-button-renderer[3]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]'))
    )
    un_sub_3.click()

    driver.refresh()


