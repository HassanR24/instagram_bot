from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class InstaFollower:

    def __init__(self):
        exe_path = "/Users/macintosh/Development/chromedriver"
        #replace the above path with your own
        ser = Service(executable_path=exe_path)
        self.driver = webdriver.Chrome(service=ser)
        self.insta_url = "https://www.instagram.com/accounts/login/"
        self.driver.maximize_window()

    def login(self, username, password):
        self.driver.get(self.insta_url)
        time.sleep(5)
        username_field = self.driver.find_element(By.NAME, "username")
        username_field.send_keys(username)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(password, Keys.ENTER)
        time.sleep(5)
        save_info_button = self.driver.find_element(By.XPATH,
                                                    '//button[@type="button"][contains(text(),"Save information")]')
        save_info_button.click()
        time.sleep(3)
        not_now_button = self.driver.find_element(By.XPATH, '//button[contains(text(),"Not Now")]')
        not_now_button.click()
        time.sleep(3)

    def find_followers(self):
        search_button = self.driver.find_element(By.XPATH, "//div[contains(@class,'_aacl')] [text()='Search']")
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(search_button)
        actions.click()
        actions.perform()
        time.sleep(3)
        search_field = self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        search_field.send_keys("Tasty")
        time.sleep(2)
        search_field.send_keys(Keys.ENTER)
        time.sleep(1)
        search_field.send_keys(Keys.ENTER)
        time.sleep(5)

    def follow_people(self):
        followers_button = self.driver.find_element(By.XPATH, '//span[contains(text()," followers")]')
        followers_button.click()
        time.sleep(5)
        follow_list = self.driver.find_elements(By.XPATH, '//div[contains(@class,"_aacl _aaco")][text()="Follow"]')
        for follow in follow_list:
            try:
                follow.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                pass
