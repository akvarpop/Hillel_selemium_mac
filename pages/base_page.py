from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    # Поиск элемента который виден на странице
    def element_is_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    # Поиск видимых элементов
    def element_are_visible(self, locator, timeout = 5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    # Поиск элемента которого не видно в открывшемся окне
    def element_is_presents(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # Поиск элементов которых не видно в открывшемся окне.
    def element_are_presents(self, locator, timeout= 5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    # Поиск невидимого элемента.
    def element_is_not_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    # Поиск кликабельного элемента.

    def element_is_clickabel(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element):
        self.driver.execute_script("argument[0].scrollIntoView();", element)

    def send_pdf(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
