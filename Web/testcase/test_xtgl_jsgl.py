from time import sleep
from selenium import webdriver
from Web.page_object.SearchPage import SearchPage


class Test_JSGL(object):

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("http://10.23.190.107/multiscreen/")
        self.driver.maximize_window()

    def test_search_name(self):
        SearchPage(self.driver).xt_jsgl("权限")

    def teardown(self):
        sleep(10)
        self.driver.quit()