from selenium.webdriver.common.by import By
from .base import Bsae
import time

class LoginPage(Bsae):
    login_username_loc = (By.ID, 'uid')
    login_pwd_loc = (By.ID, 'pwd')
    login_button_loc = (By.ID, 'login_button')

    def login_username(self, text):
        return self.find_element_(*self.login_username_loc).send_keys(text)

    def login_pwd(self, text):
        return self.find_element_(*self.login_pwd_loc).send_keys(text)

    def login_button(self):
        return self.find_element_(*self.login_button_loc).click()


    def login_action(self,username='13146866232',password='111111'):
        self.open()
        self.login_username(username)
        self.login_pwd(password)
        self.login_button()


