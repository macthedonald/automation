from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Applemusic:


    def __init__(self, username):

        driver = webdriver.Chrome()

        driver.get("https://music.apple.com/login")
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[src^='/includes/commerce/authenticate?product=music']")))
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR,"iframe[title^='Sign In with your Apple']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#account_name_text_field"))).send_keys("pachanmorgan@gmail.com")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[id='sign-in']"))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                    (By.ID, "password_text_field"))).send_keys('671@Bonny')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "button[id='sign-in']"))).click()

Applemusic('example@gmail.com')
