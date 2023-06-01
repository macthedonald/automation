import threading
from localStoragePy import localStoragePy
import datetime
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class StreamAudiomack():

    def __init__(self, url, minutes, repeat):
        threading.Thread.__init__(self)
        self.ls = localStoragePy("playlist", "json")
        options = webdriver.ChromeOptions()
        options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=options)


        self.wait = WebDriverWait(self.driver, 15)
        self.driver.maximize_window()
        self.url = url
        self.chain = ActionChains(self.driver)
        self.repeat = repeat
        self.minutes = minutes

    def run(self, window):

        # self.driver.switch_to.window("secondtab")
        try:
            self.driver.delete_all_cookies()
            self.driver.get(self.url)
        
            # play button
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-testid='playButton']"))).click()
        except:
            None
        else:
            print("\nᴺᴼᵂ ᴾᴸᴬᵞᴵᴺᴳ♫♬♪.. "+self.url)
            self.countdown(0, self.minutes, 0, window)

    def start_thread(self, window):
        threading.Thread(target=self.run, args=(window,), daemon=True).start()

    def replay(self, h, m, s):
        try:
            # pause
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-testid='playButton']"))).click()

            time.sleep(5)
            self.driver.get(self.url)

            # play button
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button[data-testid='playButton']"))).click()
        except:
            None
            # self.replay(h, m, s)
        else:
            time.sleep(5)
            print("\nreplaying\n")
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

        # Create class that acts as a countdown

    def countdown(self, h, m, s, window):

        # Calculate the total number of seconds
        total_seconds = (int(h) * 3600 + int(m) * 60 + int(s)) / 2

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
            print("\nreplay count: " + str(i + 1))
            self.replay(0, self.minutes, 0)

        self.stop(window)

    def stop(self, window):
        try:
            print("stopping...")
            self.driver.quit()
        except:
            None
            # self.stop(window)
        else:
            print("stopped")
