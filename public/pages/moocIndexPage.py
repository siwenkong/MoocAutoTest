# -*- coding:utf-8 -*-
import time
from public.common import basepage


class MoocIndexPage(basepage.Page):

    def into_mooc_page(self):
        """打开慕课网首页"""
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

    # def return_title(self):
    #     """"返回该页面的title"""
    #     return self.dr.get_title()

    def click_shizhan(self):
        """"点击实战按钮"""
        self.dr.click('link_text->实战')

    def click_second(self):
        """"点击实战页面上方最右边一个按钮"""
        self.dr.click_element('css->a.banner-item.l', 1)
        self.dr.into_new_window()

    def click_flash(self):
        """"点击实战列表的第二项"""
        self.dr.click_element('css->a.r.study-btn', 1)
        self.dr.into_new_window()  #移动到新打开的窗口

    def click_addCart(self):
        """"点击添加购物车"""
        self.dr.click('class->sz-add-shopping-cart')

    def move_cart(self):
        """"将鼠标移动到购物车按钮上"""
        self.dr.move_to_element('class->shop-cart-icon')
    def click_sum(self):
        """"点击去购物车按钮"""
        self.dr.click('link_text->去购物车')
        self.dr.into_new_window()




















