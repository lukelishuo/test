# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

class Page(object):
    """基础类，用于所以页面对象类继承"""
    login_url = 'https://www.amazon.com/'

    def __init__(self, selenium_driver, base_url=login_url):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 10

    def on_page(self):
        #return self.driver.current_url == (self.base_url + self.url)
        return self.driver.current_url == self.url

    def _open(self, url):
        #url = self.base_url + url # Changed this as the login page has total different address as click login
        self.driver.get(url)
        #assert self.on_page(), 'did not land on %s' % url

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)


class Mainpage(Page):

     # get the mainpage url
    url = "https://www.amazon.com/"
    searchbox_loc = (By.ID,"twotabsearchtextbox")
    searchbut_loc = (By.CSS_SELECTOR,"#nav-search > form > div.nav-right > div > input")


    def search_input(self):
        self.find_element(*self.searchbox_loc).send_keys("Razor A Kick Scooter, Blue")
    def search_press(self):
        self.find_element(*self.searchbut_loc).click()


class Result(Page):
    # get the mainpage url
    url = "https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=Razor+A+Kick+Scooter%2C+Blue"
    item_loc = (By.ID, "pdagDesktopSparkleDescription1")

    def check_first_result(self):
        response = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "pdagDesktopSparkleDescription1")))
        return self.find_element(*self.item_loc).text

    def click_first_result(self):
        response = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "pdagDesktopSparkleDescription1")))
        self.find_element(*self.item_loc).click()

class Razer(Page):
    # get the mainpage url
    url = "https://www.amazon.com/Razor-A-Kick-Scooter-Blue/dp/B01EN6LTAQ/ref=sr_1_1_sspa?s=outdoor-recreation&ie=UTF8&qid=1547803054&sr=1-1-spons&keywords=scooter&psc=1"
    addbutton_loc = (By.ID, "add-to-cart-button")
    numbertable_loc = (By.ID, "quantity")

    def select_number(self,number):
        sleep (2)
        depart = self.find_element(*self.numbertable_loc)
        select_depart = Select(depart)
        select_depart.select_by_visible_text(number)

    def add_to_cart(self):
        self.find_element(*self.addbutton_loc).click

class Confirmation(Page):
    # get the mainpage url
    url = "https://www.amazon.com/gp/huc/view.html?ie=UTF8&newItems=Cb8d04367-c9bb-4aea-baea-9caba822997b%2C1"
    cartbutton_loc = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        self.find_element(*self.cartbutton_loc).click

class ShopCart(Page):
    # get the mainpage url
    url = "https://www.amazon.com/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance"
    firstname_loc = (By.CSS_SELECTOR, "#result_0 > div > div:nth-child(5) > div:nth-child(1) > a > h2")

    def check_first_result(self):
        return self.find_element(*self.firstname_loc).text

    def click_first_result(self):
        self.find_element(*self.firstname_loc).click


