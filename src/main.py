from browser.chrome_driver import ChromeDriver
from utils.utils import read_config, read_random_lines

def main():
    driver = None
    try:
        usr_config = read_config('.\\config\\user_config.json')
        mobile_emulation = {
            "deviceName": "Nexus 5"
        }
        driver = ChromeDriver(executable_path=usr_config['chromedriver_path'], 
                              mobile_emulation=mobile_emulation)
        driver.login(usr_config)
        driver.open_browser(url="http://cn.bing.com")
        random_lines = read_random_lines('.\\data\\queries.txt', num_lines=20)
        
        for line in random_lines:
            driver.search(line, usr_config)
            driver.random_roll()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if driver:
            driver.close_browser()

if __name__ == "__main__":
    main()