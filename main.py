from time import sleep

import yaml
from selenium import webdriver


# profile = webdriver.FirefoxProfile()
# profile.set_preference("network.cookie.cookieBehavior", 2)
# profile.update_preferences()

class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        self.browser.get('https://www.instagram.com/')

        self.browser.find_element_by_xpath("//button[text()='Accept All']").click()

        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(username)
        password_input.send_keys(password)

        self.browser.find_element_by_xpath("//div[text()='Log In']").submit()


class MainPage:  # entry screen
    def __init__(self, browser):
        self.browser = browser

    def DiscardSaveLoginInformation(self):
        self.browser.find_element_by_xpath("//button[text()='Not Now']").click()

    def DiscardNotfication(self):
        self.browser.find_element_by_xpath("//button[text()='Not Now']").click()


cfg = "config.yaml"
with open(cfg, "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

my_username = cfg['username']
my_secret_password = cfg['password']

browser = webdriver.Firefox()
browser.implicitly_wait(10)

loginPage = LoginPage(browser)
loginPage.login(my_username, my_secret_password)

mainPage = MainPage(browser)
mainPage.DiscardSaveLoginInformation() # save login information discard
mainPage.DiscardNotfication()

sleep(5)

browser.close()
