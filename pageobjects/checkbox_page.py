from selenium.webdriver.common.by import By


class CheckboxPage(object):

    def __init__(self, driver):
        self.checkbox_1 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(1)")
        self.checkbox_2 = lambda: driver.find_element(By.CSS_SELECTOR, "#checkboxes > input[type=checkbox]:nth-child(3)")