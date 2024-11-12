from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# from pageObjects.CheckoutPage import CheckoutPage, Products
from ..pageObjects.CheckoutPage import CheckoutPage
from ..pageObjects.CheckoutPage import Products
from ..pageObjects.ConfirmPage import ConfirmPage
from ..pageObjects.HomePage import HomePage
from ..utilities.BaseClass import BaseClass


class TestOne(BaseClass):
    def test_e2e(self):

        log = self.getLogger()

        #  //a[contains(@href,'shop')]    a[href*='shop']

        homepage = HomePage(self.driver)
        homepage.shopItems().click()
        # self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()

        checkout = CheckoutPage(self.driver)
        products = checkout.cards()

        log.info("getting all products")

        for product in products:
            p = Products(product)  #create a constructor with product sending as intsance variable
            productName = p.prod_name().text
            log.info(productName)
            # productName = product.find_element(By.XPATH, "div/h4/a").text

            if productName == "Blackberry":
                check_click = p.checkout().click()
                # product.find_element(By.XPATH, "div/button").click()

        checkout.butt_click().click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

        checkout.butt_2().click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

        log.info("Entering COuntry name as ind")
        confirmpage = ConfirmPage(self.driver)
        confirmpage.input_val().send_keys("ind")
        # self.driver.find_element(By.ID, "country").send_keys("ind")

        self.verifyinglink("India")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))


        confirmpage.country_ele().click()
        # self.driver.find_element(By.LINK_TEXT, "India").click()

        confirmpage.tick_checkbox().click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

        confirmpage.submit_button().click()
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("text recieved from application is "+ successText)

        assert "Success! Thank you!" in successText