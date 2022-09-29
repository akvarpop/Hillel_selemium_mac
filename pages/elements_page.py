import time
import pytest
from locators.elements_page_locators import LoginPage, AddUsers, DeleteUser
from pages.base_page import BasePage
from resources.data_json_on_python import NAME_ADMIN, PASSWORD_ADMIN


class TextBoxPage(BasePage):

    def fill_all_fields(self):
        self.element_is_visible(LoginPage.LOGIN_FIELD).send_keys(NAME_ADMIN)
        self.element_is_visible(LoginPage.PASSWORD_FIELD).send_keys(PASSWORD_ADMIN)
        self.element_is_visible(LoginPage.SUBMIT_BUTTON).click()
        time.sleep(1)

    def check_field(self):
        result = self.element_is_visible(LoginPage.SUBMIT_RESULT).text
        return result

    def create_new_user(self):
        self.element_is_visible(AddUsers.BUTTON_ADD_USERS).click()
        self.element_is_visible(AddUsers.ADD_USERNAME).send_keys('Popravka')
        self.element_is_visible(AddUsers.ADD_PASSWORD).send_keys('test12345')
        self.element_is_visible(AddUsers.ADD_PASSWORD_CONFIRM).send_keys('test12345')
        self.element_is_visible(AddUsers.BUTTON_SAVE).click()
        time.sleep(1)

    def check_new_user(self):
        result = self.element_is_visible(AddUsers.ADDED_SUCCESSFULLY).text
        return result

    def delete_user(self):
        self.element_is_visible(DeleteUser.BUTTON_PAGE_USERS).click()
        self.element_is_visible(DeleteUser.SEARCH_WINDOW_USERS).send_keys('Popravka')
        self.element_is_visible(DeleteUser.BUTTON_SEARCH).click()
        self.element_is_visible(DeleteUser.CHOOSE_USERNAME).click()
        self.element_is_visible(DeleteUser.CHOOSE_ACTION).click()
        self.element_is_visible(DeleteUser.CHOOSE_ACTION_DELETE).click()
        self.element_is_visible(DeleteUser.BUTTON_GO).click()
        self.element_is_visible(DeleteUser.BUTTON_YES_IM_SURE).click()
        time.sleep(2)

    def check_delete_user(self):
        result = self.element_is_visible(DeleteUser.RESULT_TEXT).text
        return result
