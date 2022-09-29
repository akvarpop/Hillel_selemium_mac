import time
import pytest
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage
from resources.data_json_on_python import URL_ENDPOINT
from locators.elements_page_locators import LoginPage, AddUsers, DeleteUser


class TestElements:
    class TestTextBox:

        def test_login_to_admin_panel(self, driver):
            """Fill in the fields to enter the admin panel"""
            text_box_page = TextBoxPage(driver, URL_ENDPOINT)
            text_box_page.open()
            text_box_page.fill_all_fields()
            driver.get_screenshot_as_file("WELCOME, ADMIN.png")
            assert text_box_page.check_field() == 'Django administration', print('Administrator logged in not '
                                                                                 'successfully')

        def test_create_new_user(self, driver):
            """Create new user in admin panel """
            text_box_page = TextBoxPage(driver, URL_ENDPOINT)
            text_box_page.open()
            text_box_page.create_new_user()
            driver.get_screenshot_as_file("NEW_USER.png")
            assert text_box_page.check_new_user() == 'The user “Popravka” was added successfully. You may edit it ' \
                                                     'again below.', print('New user is not create')

        def test_delete_user(self, driver):
            """Find and delete the user you created"""
            text_box_page = TextBoxPage(driver, URL_ENDPOINT)
            text_box_page.open()
            text_box_page.delete_user()
            driver.get_screenshot_as_file("DELETE_USER.png")
            assert text_box_page.check_delete_user() == 'Successfully deleted 1 user.', print('New user is not delete')
