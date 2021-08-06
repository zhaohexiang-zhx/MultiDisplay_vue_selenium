# 各个页面的筛选条件
from Web.page_object.BasePage import BasePage
from Web.page_object.SysmanagePage import SysmanagePage


class SearchPage(BasePage):

    # 系统管理-账号管理
    def xt_zhgl(self, name):
        SysmanagePage(self.driver).zhgl()
        self.driver.find_element_by_css_selector('.el-input__inner[placeholder=请输入姓名或账号]').send_keys('%s' % name)
        self.driver.find_element_by_css_selector('.filter-aloneLine .filter-moreBtnBox .hk-btnNormal').click()

     # 系统管理-角色管理
    def xt_jsgl(self, roleName):
        SysmanagePage(self.driver).jsgl()
        self.driver.find_element_by_css_selector('.el-input__inner[placeholder=请输入角色名称]').send_keys('%s' % roleName)
        self.driver.find_element_by_css_selector('.filter-aloneLine .filter-moreBtnBox .hk-btnNormal').click()

    # 系统管理-版本管理
    def xt_bbgl(self, versionNum):
        SysmanagePage(self.driver).bbgl()
        self.driver.find_element_by_css_selector('.el-input__inner[placeholder=请输入版本号]').send_keys('%s' % versionNum)
        self.driver.find_element_by_css_selector('.filter-aloneLine .filter-moreBtnBox .hk-btnNormal').click()