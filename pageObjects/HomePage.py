from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, " a[href*='shop']")

    name = (By.CSS_SELECTOR, "#name")

    alert_btn = (By.XPATH, "//input[@type='submit']")

    verify_success = (By.XPATH, "//div/strong")

    email = (By.XPATH, "//input[@name='email']")

    def shopItems(self):
       return self.driver.find_element(*HomePage.shop)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getAlertBtn(self):
        return self.driver.find_element(*HomePage.alert_btn)

    def successText(self):
        return self.driver.find_element(*HomePage.verify_success)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
