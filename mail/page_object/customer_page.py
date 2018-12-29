from selenium.webdriver.common.by import By
from .login_page import LoginPage

class CustomerPage(LoginPage):
    head_customer_loc = (By.XPATH, '//*[@class="nav"]/li[2]/a')
    add_customer_loc = (By.ID, 'add_customer')
    customer_name_loc = (By.ID, 'custom-field-customerName')
    cellphone_loc = (By.ID, 'custom-field-cellPhone')
    customer_button_loc = (By.XPATH, '//*[@id="applyBox-2"]/input')

    def head_customer(self):
        return self.find_element_(*self.head_customer_loc).click()

    def add_customer(self):
        return self.find_element_(*self.add_customer_loc).clcik()

    def customer_name(self, text):
        return self.find_element_(*self.customer_name_loc).send_keys(text)

    def cellphone(self, text):
        return self.find_element_(*self.cellphone_loc).send_keys(text)
    def customer_button(self):
        return self.find_element_(*self.customer_button_loc).clcik()

    def add_customer_action(self, name, phone):
        self.open()
        self.login_action()
        self.head_customer()
        self.add_customer()
        self.customer_name(name)
        self.cellphone(phone)
        self.customer_button()

