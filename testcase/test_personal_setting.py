from time import sleep
from public.common import mytest
from public.pages import moocSettingPage

class TestPersonalSetting(mytest.MyTest):
    def test_setting(self):
        settingPage = moocSettingPage.MoocSettingPage(self.dr)
        settingPage.into_mooc_page()
        settingPage.click_login_button()
        settingPage.input_username('kongsiwen0818@163.com')
        settingPage.input_password('lkp11104077ksw')
        settingPage.click_login()
        settingPage.move_to_user()
        settingPage.click_setting()
        settingPage.click_change_img()