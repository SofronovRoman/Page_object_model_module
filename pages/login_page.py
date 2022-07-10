from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        try:
           WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
           return True
           assert True

    def should_be_login_form(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \       "Success message is presented, but should not be"

    def should_be_register_form(self):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False