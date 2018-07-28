from time import sleep
from public.common import mytest
from public.pages import moocIndexPage
from public.common import datainfo

class TestMoocIndex(mytest.MyTest):
    def test_login(self):
        moocpage = moocIndexPage.MoocIndexPage(self.dr)
        moocpage.into_mooc_page()
        moocpage.click_login_button()
        moocpage.input_username('kongsiwen0818@163.com')
        moocpage.input_password('lkp11104077ksw')
        moocpage.click_login()
        moocpage.click_shizhan()
        moocpage.click_second()
        moocpage.click_flash()
        moocpage.click_addCart()
        moocpage.move_cart()
        moocpage.click_sum()
        sleep(2)
        # title = moocpage.return_title()
        # print title