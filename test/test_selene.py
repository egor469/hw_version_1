from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_github():
    browser.open('https://github.com')

    s('.header-search-button').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#pull-requests-tab').click()
    s(by.text('Fix pull request close test')).click()