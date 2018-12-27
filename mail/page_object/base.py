from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
# from ..model.driver import browser
class Bsae(object):
    yunke = 'http://www.yunkecn.com'
    def __init__(self,driver,url='/pc/home/login'):
        # self.driver = browser()
        self.driver = driver
        self.url = url

    def _open(self):
        yunke_url = self.yunke + self.url
        self.driver.get(yunke_url)
        sleep(2)
        assert self.driver.current_url == yunke_url, 'url错误：%s' %yunke_url


    def open(self):
        self._open()


    def find_element_(self,*loc):
        return self.driver.find_element(*loc)

    def iframe(self,*loc):

        return self.driver.switch_to.frame(*loc)
    def alert_(self):
        return self.driver.switch_to.alert.accept

    def alert_text(self):
        return self.driver.switch_to.alert.text
