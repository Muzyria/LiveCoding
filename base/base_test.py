import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)

        request.cls.it_is_my_test = "ITS MY TEST NEW"




# class BaseTest:
#     data: Data
#
#     login_page: LoginPage
#     dashboard_page: DashboardPage
#     personal_page: PersonalPage
#
#     @pytest.fixture(autouse=True)
#     def setup(self, driver):
#         self.driver = driver
#
#     @property
#     def data(self):
#         return Data()
#
#     @property
#     def login_page(self):
#         return LoginPage(self.driver)
#
#     @property
#     def dashboard_page(self):
#         return DashboardPage(self.driver)
#
#     @property
#     def personal_page(self):
#         return PersonalPage(self.driver)

