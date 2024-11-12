from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    card = (By.XPATH, "//div[@class='card h-100']")

    button_loca = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    button_loca2 = (By.XPATH, "//button[@class='btn btn-success']")

    def cards(self):
        return self.driver.find_elements(*CheckoutPage.card)

    def butt_click(self):
        return self.driver.find_element(*CheckoutPage.button_loca)

    def butt_2(self):
        return self.driver.find_element(*CheckoutPage.button_loca2)


class Products:

    prod = (By.XPATH, "div/h4/a")

    checkout_loca = (By.XPATH, "div/button")

    def __init__(self, product):
        self.product = product

    def prod_name(self):
        return self.product.find_element(*Products.prod)

    def checkout(self):
        return self.product.find_element(*Products.checkout_loca)