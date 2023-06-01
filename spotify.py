import threading
import datetime
import time
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StreamSpotify():

    def __init__(self, url, email, password, repeat, minutes):
        threading.Thread.__init__(self)
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=options)
        self.wait = WebDriverWait(self.driver, 15)
        # self.driver.maximize_window()
        self.url = url
        self.chain = ActionChains(self.driver)
        self.email = email
        self.password = password
        self.repeat = repeat
        self.minutes = minutes

    def run(self, window):
        try:
            self.driver.delete_all_cookies()
            self.login(self.email, self.password)
            self.driver.get(self.url)
            # self.driver.implicitly_wait(5)
            nextbtn = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "html > body > div:nth-of-type(4) > div > div:nth-of-type(2) > div:nth-of-type(2) > footer > div > div:nth-of-type(2) > div > div:first-of-type > div:nth-of-type(2) > button:first-of-type > svg > path")))
            nextbtn.click()
            # play button
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button"))).click()
            
            # policy button
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[id='onetrust-close-btn-container'] > button"))).click()

            # self.wait.until(EC.presence_of_element_located(
            # (By.CSS_SELECTOR, "button[data-testid='control-button-repeat']"))).click()
        except:
            None
            #self.run(window)
        else:
            print("\nᴺᴼᵂ ᴾᴸᴬᵞᴵᴺᴳ♫♬♪.. "+self.url)
            self.countdown(0, self.minutes, 0, window)

    def start_thread(self, window):
        threading.Thread(target=self.run, args=(window,), daemon=True).start()

    def replay(self, h, m, s):
        try:
            play_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button")))
            play_button.click()
            time.sleep(5)
            self.driver.get(self.url)

            nextbtn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "html > body > div:nth-of-type(4) > div > div:nth-of-type(2) > div:nth-of-type(2) > footer > div > div:nth-of-type(2) > div > div:first-of-type > div:nth-of-type(2) > button:first-of-type > svg > path")))
            nextbtn.click()
            
            # play again
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button"))).click()

            
        except:
            None
            None
            #self.replay(h, m, s)
        else:
            print("replaying\n")
            total_seconds = (int(h) * 3600 + int(m) * 60 + int(s))/2

            # While loop that checks if total_seconds reaches zero
            # If not zero, decrement total time by one second
            while total_seconds > 0:

                # Timer represents time left on countdown
                timer = datetime.timedelta(seconds=total_seconds)

                # Prints the time left on the timer
                print("～(■_■)～♪", end="\t\t")

                # Delays the program one second
                time.sleep(1)

                # Reduces total time by one second
                total_seconds -= 1

    def login(self, Email, Password):

        url = 'https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2F'
        # self.driver.maximize_window()
        try:
            self.driver.get(url)
            # self.driver.implicitly_wait(3)
            self.driver.find_element(
                By.CSS_SELECTOR, "#login-username").send_keys(Email)
            self.driver.find_element(
                By.CSS_SELECTOR, "#login-password").send_keys(Password)
            # self.driver.implicitly_wait(3)
            print(self.email + " logging in..")
            self.driver.find_element(
                By.CSS_SELECTOR, "button[id='login-button']").click()
        except:
            None
            print(self.email + " failed to login")

        else:
            sleep(2)
            print(self.email + " logged in")

    # Create class that acts as a countdown

    def countdown(self, h, m, s, window):

        # Calculate the total number of seconds
        total_seconds = (int(h) * 3600 + int(m) * 60 + int(s))/2

        # While loop that checks if total_seconds reaches zero
        # If not zero, decrement total time by one second
        while total_seconds > 0:

            # Timer represents time left on countdown
            timer = datetime.timedelta(seconds=total_seconds)

            # Prints the time left on the timer
            print("～(■_■)～♪", end="\t\t")

            # Delays the program one second
            time.sleep(1)

            # Reduces total time by one second
            total_seconds -= 1
        # print(self.email + " stopped streaming")
        # time.sleep(37)
        for i in range(self.repeat):
            print("\nreplay count: " + str(i+1))
            self.replay(0, self.minutes, 0)

        self.stop(window)

    def stop(self, window):
        try:
            print("stopping...")
            self.driver.quit()
        except:
            None
            self.stop(window)
        else:
            print("stopped")
