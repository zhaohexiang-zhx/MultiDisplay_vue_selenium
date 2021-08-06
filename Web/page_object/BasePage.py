from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(object):

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def login(self):
        self.driver.get_cookies()
        self.driver.add_cookie({'name': 'access_token',
                                'value': 'd9bd5ef3a3ce488053d264ddc383f7d4a16e927a886b61468c536a8a7580f0e4d87c439ee5952a6d3fb736b0cc47ed348dcf7d7ecdeb58d3c6965a91b1bace5d7c9d275edcd5e6a488238f5cdba5f3fa59df2a5a0e78fc7e737750f2cbf9ffab375513c288ed3e2d7404b2e1f1ca5682bdb7a29008f38aef37703d91d088c04b265276b2880ed5d1b5b35b84d8761930'})
        self.driver.add_cookie({'name': 'multiscreen_access_token',
                                'value': '19f1a06e394c9bfcdbb96b77145dfc9fce448438a5d25be11b52f65d260300da02a49bdf48e2d8a47c209581c570ad779b29da0d8bd4717541e10440d0c12c6d0dcecba9dafd59201776ea841303c115e84117162a611b2fa059e814aae4e61b66fd933481487f2d13ceb8285c28c1bd6f39c5206fcb77ae'})
        self.driver.refresh()
        self.driver.find_element_by_css_selector('.btn').click()
        self.driver.refresh()
