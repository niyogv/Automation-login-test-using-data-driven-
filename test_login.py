# This is a test automation script in python
# Application name:qamarket.moiverse.io
# Programmer name : Niyog v
# Date of programming : 2 feb 2022
#
# Test scenerioa : Login into moiverse

from selenium import webdriver
import pytest
import time
from utlities.utlis import Home


class Test_qamarket:

    # Test case1:Login with valid credentials
    @pytest.fixture(params=Home.readDataLogin('test1')) # the name of the test which is mentioned under the xl sheet
    def getdata(self,request):
        return request.param

# Test case2:Login with invalid credentials
    @pytest.fixture(params=Home.readDataLogin('test2')) # the name of the test which is mentioned under the xl sheet
    def getdata1(self,request):
        return request.param

# Test case3:Login with only username
    @pytest.fixture(params=Home.readDataLogin('test3')) # the name of the test which is mentioned under the xl sheet
    def getdata2(self,request):
        return request.param

# Test case4:Login with only password
    @pytest.fixture(params=Home.readDataLogin('test4')) # the name of the test which is mentioned under the xl sheet
    def getdata3(self,request):
        return request.param

    def test_1(self,getdata):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://qamarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        print(self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[1]/div[1]').text)
        user=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys(getdata['name'])
        password=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys(getdata['password'])
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(10)
        # Checks whether the title of page is matching, if it is matching it will assert true and pgm continues to execute next test case
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert True
            else:
                assert False
        finally:
            self.driver.quit()

    def test_2(self,getdata1):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://qamarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        user=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys(getdata1['name'])
        password=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys(getdata1['password'])
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(6)
        # Checks whether the title of page is matching, if it is matching it will assert false as it will show an error message and pgm continues to execute next test case
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert False,'Invalid credentials'
            else:
                assert True
        finally:
            self.driver.quit()

    def test_3(self,getdata2):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://qamarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        user=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[2]/div/div/input')
        user.send_keys(getdata2['name'])
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(6)
        # Checks whether the title of page is matching, if it is matching it will assert false as it will show an error message and pgm continues to execute next test case
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert False,'All fields are mandatory'
            else:
                assert True
        finally:
            self.driver.quit()

    def test_4(self,getdata3):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://qamarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        password=self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[10]/div/div[2]/div/div/div/div[3]/div/div/input')
        password.send_keys(getdata3['password'])
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(6)
        # Checks whether the title of page is matching, if it is matching it will assert false as it will show an error message and pgm continues to execute next test case
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert False,'All fields are mandatory'
            else:
                assert True
        finally:
            self.driver.quit()

    def test_5(self):
        self.driver=webdriver.Chrome(executable_path='/Applications/chromedriver')
        self.driver.get('https://qamarket.moiverse.io/')
        self.driver.maximize_window()
        self.driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[1]/div[2]/div').click()
        self.driver.find_element_by_xpath("//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained']").click()
        time.sleep(6)
        # Checks whether the title of page is matching, if it is matching it will assert false as it will show an error message and pgm continues to execute next test case
        try:
            if self.driver.title=='MoiVerse Marketplace':
                assert False,'All fields are mandatory'
            else:
                assert True
        finally:
            self.driver.quit()





