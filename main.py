import selenium
import webbrowser
from time import time, sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = TWITTER_EMAIL
TWITTER_PASSWORD = TWITTER_PASSWORD

class InternetSpeedTwitterBot():
    def __init__(self):
        self.chrome_driver_path = "C:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome()
        # self.driver.get('https://twitter.com/')
        self.UP = 0
        self.DOWN = 0
    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        ## Starts internet speed test
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        ## Gets Upload Speed (UP)
        time.sleep(60)
        self.UP = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        ## Gets Download Speed (DOWN)
        self.DOWN = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # print(UP)
        # print(DOWN)
    def twitter_post(self):
        self.driver.get("https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D")
        time.sleep(2)
        self.driver.find_element(By.NAME, 'text').send_keys(TWITTER_EMAIL)
        self.driver.find_element(By.NAME, 'text').send_keys(Keys.ENTER)
        time.sleep(4)
        self.driver.find_element(By.NAME, "password").send_keys(TWITTER_PASSWORD)
        self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(8)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys(
            f"@Spectrum, why is my upload speed {self.UP}Mbps and my download speed {self.DOWN}Mbps "
            f"when I am promised a {PROMISED_UP} Mbps upload speed "
            f"and a {PROMISED_DOWN} Mbps download speed? Please advise"
        )





Speed_Bot = InternetSpeedTwitterBot()
# Speed_Bot.get_internet_speed()
Speed_Bot.get_internet_speed()
time.sleep(5)
if Speed_Bot.UP < PROMISED_UP and Speed_Bot.DOWN < PROMISED_DOWN:
    Speed_Bot.twitter_post()









