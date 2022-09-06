import re
from playwright.sync_api import Page, expect
import time
"""
python3 -m pytest tests --headed --slowmo 1000
headed mode shows browser
slowmo adds sleep in micro secs
"""
task_id = 159
matched_number_xpath = '//html/body/div/div/main/div/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/strong'



def test_scrapy_daraz(page: Page) -> None:
    page.goto('https://spyder.daraz.com/scrapy-ui/login')
    page.locator('#email').fill('rukeshd')
    page.locator('#password').fill('12345')
    page.locator('.btn-secondary').click()
    # page.goto('https://spyder.daraz.com/scrapy-ui/skumatching?page=1&pageSize=10')
    # takes to page
    page.goto(f'https://spyder.daraz.com/scrapy-ui/skumatching-details?id={task_id}&page=1&pageSize=50')
    # need to run a for loop here:
    # fix this later:
    mn = page.locator(matched_number_xpath).inner_text()
    print(mn)
    

    # page.locator('.btn-secondary').nth(0).click()
    """/html/body/div/div/main/div/div[2]/div/div/div/div[2]/table/tbody/tr[1]/td[7]/button[1]
    /html/body/div/div/main/div/div[2]/div/div/div/div[2]/table/tbody/tr[2]/td[7]/button[1]"""
    

