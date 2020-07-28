import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.firefox import GeckoDriverManager


"""
I had a similar issue where using ActionChains was not solving my error: WebDriverException: Message: unknown error: Element is not clickable at point (5 74, 892)

I found a nice solution if you dont want to use execute_script:

    from selenium.webdriver.common.keys import Keys #need to send keystrokes

    inputElement = self.driver.find_element_by_name('checkout')

    inputElement.send_keys("\n") #send enter for links, buttons
or

    inputElement.send_keys(Keys.SPACE) #for checkbox etc
"""
#
#browser = webdriver.Chrome(ChromeDriverManager().install())

#browser.get('http://127.0.0.1:8000/')
#time.sleep(3)
#assert 'Yahoo' in browser.title
#elem = browser.find_element_by_name('p')  # Find the search box
#elem.send_keys('seleniumhq' + Keys.RETURN)

#browser.quit()

class WannaEatUITester:
    jsScript = """
        function move_up(element) {
            element.scrollTop = element.scrollTop - 1000;
        }

        function move_down(element) {
            element.scrollTop = element.scrollTop + 1000;
        }

        move_down(arguments[0]);
        move_down(arguments[0]);
        """
    def get_engine(self, browser):
        engine = None
        if browser == "chrome" or browser == "yandex":
            engine = webdriver.Chrome(ChromeDriverManager().install())
        if browser == "opera":
            engine = webdriver.Opera(OperaDriverManager().install())
        if browser == "firefox":
            engine = webdriver.Firefox(executable_path='geckodriver.exe')
        #engine.set_window_size(1080, 720)
        return engine

    def test_ui(self):
        try:
            self.browser = self.get_engine(self.browser_type)
            self.browser.get(self.site)
            element = WebDriverWait(self.browser, 15).until(
                EC.element_to_be_clickable((By.ID, "UITestButton"))
            )
            element = self.browser.find_element_by_id("UITestButton")
            element.send_keys("\n")
            time.sleep(10)
            self.browser.quit()
        except EnvironmentError:
            print("ERROR")
            self.browser.quit()
        finally:
            self.browser.quit()

    def __init__(self, browser_type, site):
        """constructor of my UITester"""
        self.site = site
        self.browser_type = browser_type


uiTest = WannaEatUITester("chrome", "http://127.0.0.1:8000/").test_ui()