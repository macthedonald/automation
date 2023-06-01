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


class StreamApple():

    def __init__(self, url, email, password, repeat, minutes):
        threading.Thread.__init__(self)
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(
            options=options)
        self.wait = WebDriverWait(self.driver, 20)
        self.url = url
        self.chain = ActionChains(self.driver)
        self.email = email
        self.password = password
        self.repeat = repeat
        self.minutes = minutes

    def run(self, window):

        # It is switching to second tab now
        # self.driver.switch_to.new_window('tab')
        # self.driver.switch_to.window("secondtab")
        self.driver.delete_all_cookies()
        self.login(self.email, self.password)
        self.driver.get(self.url)
        # self.driver.implicitly_wait(5)
        # play button
        try:
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='click-action']"))).click()
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

            self.wait.until(EC.element_to_be_clickable(
                (By.CLASS_NAME, "play-button"))).click()

            time.sleep(5)
            self.driver.get(self.url)

            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[data-testid='click-action']"))).click()
        except:
            None
            #self.replay(h, m, s)
        else:
            print(self.email + " streaming.. "+self.url)

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

    def login(self, email, password):
        try:

            url = 'https://music.apple.com/login'
            # self.driver.maximize_window()
            self.driver.get(url)
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[src^='/includes/commerce/authenticate?product=music']")))
            self.wait.until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe[title^='Sign In with your Apple']")))
            self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input#account_name_text_field"))).send_keys(email)
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "button[id='sign-in']"))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.ID, "password_text_field"))).send_keys(password)
            self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, "button[id='sign-in']"))).click()
        except:
            print(self.email + " could not log in")
        else:
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
            #self.stop(window)
        else:
            print("stopped")
