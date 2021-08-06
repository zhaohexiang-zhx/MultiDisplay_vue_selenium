# 系统管理下各个菜单入口
from Web.page_object.BasePage import BasePage
from Web.page_object.IndexPage import IndexPage


class SysmanagePage(BasePage):

    # 账号管理
    def zhgl(self):
        IndexPage(self.driver).xtgl()
        self.driver.find_element_by_xpath('//*[@class="el-menu el-menu--inline"]//li[contains(text(), "账号管理")]').click()

    # 角色管理
    def jsgl(self):
        IndexPage(self.driver).xtgl()
        self.driver.find_element_by_xpath('//*[@class="el-menu el-menu--inline"]//li[contains(text(), "角色管理")]').click()

    # 版本管理
    def bbgl(self):
        IndexPage(self.driver).xtgl()
        self.driver.find_element_by_xpath('//*[@class="el-menu el-menu--inline"]//li[contains(text(), "版本管理")]').click()

    # 一键置灰
    def yjzh(self):
        IndexPage(self.driver).xtgl()
        self.driver.find_element_by_xpath('//*[@class="el-menu el-menu--inline"]//li[contains(text(), "一键置灰")]').click()

    # 应用信息
    def yyxx(self):
        IndexPage(self.driver).xtgl()
        self.driver.find_element_by_xpath('//*[@class="el-menu el-menu--inline"]//li[contains(text(), "应用信息")]').click()


