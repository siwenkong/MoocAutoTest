# -*- coding:utf-8 -*-
import time
from public.common import basepage
from public.pages import moocIndexPage

class MoocSettingPage(basepage.Page):

    def into_mooc_page(self):
        self.dr.open("http://www.imooc.com/")

    def click_login_button(self):
        """"点击页面右上角的登陆按钮"""
        self.dr.click('id->js-signin-btn')

    def input_username(self, values):
        """"输入用户名"""
        self.dr.clear_type('name->email', values)

    def input_password(self, values):
        """"输入密码"""
        self.dr.clear_type('name->password', values)

    def click_login(self):
        """"点击登陆按钮"""
        self.dr.click('css->input.btn-red.btn-full.xa-login')
        # self.dr.click('class->btn-red')
        time.sleep(3)

    def move_to_user(self):
        """"移动到右上角的用户头像上"""
        self.dr.move_to_element('id->header-avator')

    def click_setting(self):
        """"点击个人设置按钮"""
        self.dr.click('link_text->个人设置')
        self.dr.into_new_window()

    def click_change_img(self):
        """"更换头像"""
        self.dr.move_to_element('class->avator-img')
        self.dr.click('class->js-avator-link')
        filePath = "F:/workspace/MoocAutoTesting/data/xiongbenxiogn1.jpg"
        self.dr.type('id->upload', filePath)
        self.dr.click('link_text->确定')
