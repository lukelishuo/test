from Common_Function import search_products
from selenium import webdriver
import unittest
from time import sleep
from Common_Function import verify_item
import Config_para as CP
from Common_Function import choose_item
from Common_Function import select_num_cfm
from Common_Function import click_cart
from Common_Function import check_item_name
from Common_Function import check_item_number
from Common_Function import modify_item_number
from Common_Function import choose_second_item
from Common_Function import delete_item
from Common_Function import verify_total

#TestCase1 : Search "Scooter and check the first term is "Razor A Kick Scooter, Blue"

class TestCase1(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()

    def test_scenario(self):

        search_products(self.driver)
        sleep (2)
        result = verify_item(self.driver,CP.item_searched)
        self.assertEquals(result, "Razor A Kick Scooter, Blue")

    def doCleanups(self):
        self.driver.quit()

# Add in another scooter and verify it inside the shopping cart

class TestCase2(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"1",True)
        click_cart(self.driver)
        item_name = check_item_name(self.driver, 1)
        self.assertEquals(item_name, "Razor A Kick Scooter, Blue")


    def doCleanups(self):
        self.driver.quit()

#Check the numbers can be choose 1 - 9
class TestCase3(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver, "1",False)
        select_num_cfm(self.driver, "2",False)
        select_num_cfm(self.driver, "3",False)
        select_num_cfm(self.driver, "4",False)
        select_num_cfm(self.driver, "5",False)
        select_num_cfm(self.driver, "6",False)
        select_num_cfm(self.driver, "7",False)
        select_num_cfm(self.driver, "8",False)
        select_num_cfm(self.driver, "9",False)

    def doCleanups(self):
        self.driver.quit()


#Check the numbers you buy is the same in the shopping cart

class TestCase4(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"7",True)
        click_cart(self.driver)
        item_name = check_item_number(self.driver,1)
        self.assertEquals(item_name, "7")

    def doCleanups(self):
        self.driver.quit()

#Verify the number can also be change in shopping cart

class TestCase5(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"7",True)
        click_cart(self.driver)

        modify_item_number(self.driver,1,"4")
        item_name = check_item_number(self.driver,1)
        self.assertEquals(item_name, "4")

    def doCleanups(self):
        self.driver.quit()

#Add the second product and verify change in list

class TestCase6(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"1",True)
        click_cart(self.driver)
        choose_second_item(self.driver)
        select_num_cfm(self.driver, "1", True)
        click_cart(self.driver)
        item_name = check_item_name(self.driver, 1)
        self.assertEquals(item_name, "Razor A Kick Scooter, Red")

    def doCleanups(self):
        self.driver.quit()

class TestCase7(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"1",True)
        click_cart(self.driver)
        choose_second_item(self.driver)
        select_num_cfm(self.driver, "1", False)
        select_num_cfm(self.driver, "2", False)
        select_num_cfm(self.driver, "3", False)
        select_num_cfm(self.driver, "4", False)
        select_num_cfm(self.driver, "5", False)
        select_num_cfm(self.driver, "6", False)
        select_num_cfm(self.driver, "7", False)
        select_num_cfm(self.driver, "8", False)
        select_num_cfm(self.driver, "9", False)

    def doCleanups(self):
        self.driver.quit()

#Check the second product can also change buy quantity

class TestCase8(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"1",True)
        click_cart(self.driver)
        choose_second_item(self.driver)
        select_num_cfm(self.driver, "1", True)
        click_cart(self.driver)
        modify_item_number(self.driver,1,"2")
        item_name = check_item_number(self.driver,1)
        self.assertEquals(item_name, "2")

    def doCleanups(self):
        self.driver.quit()

#Check the sequence in the cart after choosing the second product

class TestCase9(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"1",True)
        click_cart(self.driver)
        choose_second_item(self.driver)
        select_num_cfm(self.driver, "1", True)
        click_cart(self.driver)
        item_name = check_item_name(self.driver, 1)
        self.assertEquals(item_name, "Razor A Kick Scooter, Pink")
        item_name = check_item_name(self.driver, 2)
        self.assertEquals(item_name, "Razor A Kick Scooter, Blue")

    def doCleanups(self):
        self.driver.quit()




#Check the item can be deleted from the table

class TestCase10(unittest.TestCase):

    def setUp(self):

        driverLocation = './chromedriver'
        self.driver=webdriver.Chrome(driverLocation)

    def test_scenario(self):

        choose_item(self.driver)
        sleep (2)
        select_num_cfm(self.driver,"1",True)
        click_cart(self.driver)
        choose_second_item(self.driver)
        select_num_cfm(self.driver, "1", True)
        click_cart(self.driver)
        item_name = check_item_name(self.driver, 1)
        before = verify_total(self.driver)
        delete_item(self.driver)
        sleep (3)
        after = verify_total(self.driver)
        self.assertFalse(before == after)

    def doCleanups(self):
        self.driver.quit()