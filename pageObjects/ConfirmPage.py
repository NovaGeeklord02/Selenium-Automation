from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    input_loca = (By.ID, "country")

    input_country = (By.LINK_TEXT, "India")

    check_loca = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    submit_location = (By.CSS_SELECTOR, "[type='submit']")

    def input_val(self):
        return  self.driver.find_element(*ConfirmPage.input_loca)

    def country_ele(self):
        return self.driver.find_element(*ConfirmPage.input_country)

    def tick_checkbox(self):
        return self.driver.find_element(*ConfirmPage.check_loca)

    def submit_button(self):
        return self.driver.find_element(*ConfirmPage.submit_location)
