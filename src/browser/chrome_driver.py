from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from utils.logger import Logger
from utils.utils import *

class ChromeDriver:
    def __init__(self, chrome_options = None, executable_path = None, mobile_emulation = None):
        self.logger = Logger("ChromeDriver")
        if chrome_options is None:
            chrome_options = Options()
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument('--ignore-ssl-errors')
            chrome_options.add_argument("--enable-unsafe-webgl")
            chrome_options.add_argument("--enable-unsafe-swiftshader")
            chrome_options.add_argument("--disable-software-rasterizer")
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_argument("--disable-web-security")
        if mobile_emulation is not None:
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        if executable_path is None:
            executable_path = "D:\\Tools\\anaconda3\\chromedriver.exe"
        service = Service(executable_path)
        self.driver = webdriver.Chrome(service = service, 
                                       options = chrome_options)
        self.logger.log_info("ChromeDriver initialized")
    def open_browser(self, url = "http://cn.bing.com"):
        try:
            self.driver.get(url)
            self.logger.log_info(f"Opened browser with url: {url}")
        except Exception as e:
            self.logger.log_error(f"An error occurred while opening browser: {str(e)}")

    def search(self, query, usr_config):
        try:
            sleep_random(usr_config["wait_time"])
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(query)
            sleep_random(usr_config["wait_time"])
            search_box.send_keys(Keys.RETURN)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "b_results"))
            )
            sleep_random(usr_config["wait_time"])
            self.logger.log_info(f"Searched query: {query}")
        except Exception as e:
            self.logger.log_error(f"An error occurred while searching: {str(e)}")

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.logger.log_info("Closed browser")
            
    def get_rewards(self):
        """获取积分"""
        pass
        
    def login(self, usr_config, login_url="http://login.live.com/"):
        username = usr_config["username"]
        password = usr_config["password"]
        self.driver.get(login_url)
        self.logger.log_info(f"Opened login page: {login_url}")
        try:
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "loginfmt"))
            )
            sleep_random(usr_config["wait_time"])
            username_field.send_keys(username)
            self.logger.log_info(f"Entered username: {username}")

            next_button = self.driver.find_element(By.ID, "idSIButton9")
            sleep_random(usr_config["wait_time"])
            next_button.click()
            self.logger.log_info("Clicked next button after entering username")

            self.driver.implicitly_wait(10)
            password_field = self.driver.find_element(By.NAME, "passwd")
            sleep_random(usr_config["wait_time"])
            password_field.send_keys(password)
            self.logger.log_info("Entered password")

            sign_in_button = self.driver.find_element(By.ID, "idSIButton9")
            sleep_random(usr_config["wait_time"])
            sign_in_button.click()
            self.logger.log_info("Clicked sign in button")

            stay_signed_in_button = self.driver.find_element(By.ID, "acceptButton")
            sleep_random(usr_config["wait_time"])
            stay_signed_in_button.click()
            self.logger.log_info("Clicked stay signed in button")
            
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self.logger.log_info("Login successful")
            sleep_random(usr_config["wait_time"])
        except Exception as e:
            self.logger.log_error(f"Login failed: {str(e)}")
            return None
        
    def random_roll(self):
        try:
            total_height = self.driver.execute_script("return document.body.scrollHeight")
            scroll_times = random.randint(5, 10)
            
            for _ in range(scroll_times):
                current_position = self.driver.execute_script("return window.pageYOffset;")
                screen_height = self.driver.execute_script("return window.innerHeight;")
                min_position = max(0, current_position - screen_height)
                max_position = min(total_height, current_position + screen_height)
                scroll_position = random.randint(int(min_position), 
                                                 int(max_position))
                
                self.driver.execute_script(f"window.scrollTo(0, {scroll_position});")
                time.sleep(random.uniform(0.5, 2.0))
        except Exception as e:
            self.logger.log_error(f"An error occurred while scrolling: {str(e)}")