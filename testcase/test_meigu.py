from time import sleep
from public.common import mytest
from public.pages import meiguPage

class TestMeigu(mytest.MyTest):
    def test_pankou(self):
        meigupage = meiguPage.MeiguPage(self.dr)
        meigupage.into_httptest_page()
        # meigupage.click_meigu_pankou_button()
        meigupage.compare_price()
