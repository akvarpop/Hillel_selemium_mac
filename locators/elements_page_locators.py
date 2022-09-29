from selenium.webdriver.common.by import By


class LoginPage:
    LOGIN_FIELD = (By.ID, 'id_username')
    PASSWORD_FIELD = By.XPATH, '//*[@id="id_password"]'
    SUBMIT_BUTTON = By.XPATH, '//*[@id="login-form"]/div[3]/input'
    SUBMIT_RESULT = By.XPATH, '//*[@id="site-name"]/a'


class AdminPage:
    PAGE_HEADER = By.XPATH, '//*[@id="site-name"]/a'


class AddUsers:
    BUTTON_ADD_USERS = By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/td[1]/a'
    ADD_USERNAME = By.XPATH, '//*[@id="id_username"]'
    ADD_PASSWORD = By.XPATH, '//*[@id="id_password1"]'
    ADD_PASSWORD_CONFIRM = By.XPATH, '//*[@id="id_password2"]'
    BUTTON_SAVE = By.XPATH, '//*[@id="user_form"]/div/div/input[1]'
    BUTTON_SAVE_AND_CONTINUE = By.XPATH, '//*[@id="user_form"]/div/div/input[3]'
    BUTTON_SAVE_AND_ANOTHER = By.XPATH, '//*[@id="user_form"]/div/div/input[2]'
    ADDED_SUCCESSFULLY = By.XPATH, '//*[@id="main"]/div/ul/li'


class DeleteUser:
    BUTTON_PAGE_USERS = By.XPATH, '//*[@id="content-main"]/div/table/tbody/tr[2]/th/a'
    SEARCH_WINDOW_USERS = By.XPATH, '//*[@id="searchbar"]'
    BUTTON_SEARCH = By.XPATH, '//*[@id="changelist-search"]/div/input[2]'
    CHOOSE_USERNAME = By.XPATH, '//*[@id="action-toggle"]'
    CHOOSE_ACTION = By.XPATH, '//*[@id="changelist-form"]/div[1]/label/select'
    CHOOSE_ACTION_DELETE = By.XPATH, '//*[@id="changelist-form"]/div[1]/label/select/option[2]'
    BUTTON_GO = By.XPATH, '//*[@id="changelist-form"]/div[1]/button'
    BUTTON_YES_IM_SURE = By.XPATH, '//*[@id="content"]/form/div/input[4]'
    RESULT_TEXT = By.XPATH, '//*[@id="main"]/div/ul/li'