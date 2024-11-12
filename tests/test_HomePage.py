import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from ..TestData.HomePageData import HomePageData
from ..pageObjects.HomePage import HomePage
from ..utilities.BaseClass import BaseClass


class Test(BaseClass):

    def test_submission(self, getData):

        log = self.getLogger()

        homepage = HomePage(self.driver)

        # homepage.getName().click()
        input_field = self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]")
        # input_field.clear()
        log.info("input value first name is" + getData["firstname"])
        input_field.send_keys(getData["firstname"])

        # self.driver.find_element(By.XPATH, "(//input[@name='name'])[1]").send_keys(getData)

        email_field = homepage.getEmail()
        # email_field.clear()
        log.info("input value email name is" + getData["email"])
        email_field.send_keys(getData["email"])

        # time.sleep(2)

        homepage.getAlertBtn().click()
        # self.driver.find_element(By.ID, "alertbtn").click()

        self.verifySuccess()

        alertText = homepage.successText().text
        print(alertText)
        assert "Success" in alertText

        self.driver.refresh()



    @pytest.fixture(params=HomePageData.getTestData("TestCase1"))
    def getData(self, request):
        return request.param
