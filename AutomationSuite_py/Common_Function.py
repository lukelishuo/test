from time import sleep
import Page_Class as page
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import Config_para as CP



def search_products(driver):

    main_page = page.Mainpage(driver)
    main_page.open()
    main_page.search_input()
    sleep (0.5)
    main_page.search_press()

def get_item(driver):
    main_page = page.Result(driver)
    main_page.open()
    text = main_page.check_first_result()
    return text

def choose_item(driver):
    main_page = page.Result(driver)
    main_page.open()
    main_page.click_first_result()

def choose_number(driver,number):
    main_page = page.Razer(driver)
    main_page.open()
    main_page.select_number(number)
    sleep (1)
    main_page.add_to_cart()

def go_shopcart(driver):
    main_page = page.Confirmation(driver)
    main_page.open()
    main_page.add_to_cart()

def verify_item(driver,text):
    response = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, text)))
    return response.text

def verify_total(driver):
    response = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, CP.check_total)))
    return response.text

def select_num_cfm(driver,number,click):
    response = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, CP.numbertable)))
    select_num = Select(response)
    select_num.select_by_visible_text(number)
    if click == True:
        sleep(1)
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, CP.addbutton))).click()

def click_cart(driver):
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.ID, CP.go_cart))).click()

def choose_second_item(driver):
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, CP.second_scooter))).click()

def delete_item(driver):
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, CP.delete_item))).click()




def check_item_name(driver,number):
    if number == 1:
        selector = CP.first_item
    if number == 2:
        selector = CP.second_item
    if number == 3:
        selector = CP.third_item
    item =  WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    return item.text

def check_item_number(driver,number):
    if number == 1:
        selector = CP.first_number
    if number == 2:
        selector = CP.second_number
    if number == 3:
        selector = CP.third_number
    item =  WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    return item.text

def modify_item_number(driver,item,quantity):
    if item == 1:
        selector = CP.first_number_select
    if item == 2:
        selector = CP.second_number
    if item == 3:
        selector = CP.third_number

    response = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
    select_num = Select(response)
    select_num.select_by_visible_text(quantity)
