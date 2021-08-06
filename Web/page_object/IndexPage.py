from Web.page_object.BasePage import BasePage


class IndexPage(BasePage):

    # 素材管理
    def scgl(self):
        BasePage(self.driver).login()
        self.driver.find_element_by_xpath('//*[contains(text(), "素材管理")]/../..//*[@class="el-submenu__title"]').click()

    # 视频管理
    def spgl(self):
        BasePage(self.driver).login()
        self.driver.find_element_by_xpath('//*[contains(text(), "视频管理")]/../..//*[@class="el-submenu__title"]').click()

    # 互动管理
    def hdgl(self):
        BasePage(self.driver).login()
        self.driver.find_element_by_xpath('//*[contains(text(), "互动管理")]/../..//*[@class="el-submenu__title"]').click()

    # 统计管理
    def tjgl(self):
        BasePage(self.driver).login()
        self.driver.find_element_by_xpath('//*[contains(text(), "统计管理")]/../..//*[@class="el-submenu__title"]').click()

    #系统管理
    def xtgl(self):
        BasePage(self.driver).login()
        self.driver.find_element_by_xpath('//*[contains(text(), "系统管理")]/../..//*[@class="el-submenu__title"]').click()