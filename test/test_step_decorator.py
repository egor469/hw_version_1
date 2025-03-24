import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_rep('eroshenkoam/allure-example')
    go_to_rep('eroshenkoam/allure-example')
    search_pull()

@allure.step('открываем')
def open_main_page():
    browser.open('https://github.com')

@allure.step('ищем {repo}')
def search_for_rep(repo):
    s('.header-search-button').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()

@allure.step('открываем {repo}')
def go_to_rep(repo):
    s(by.link_text(repo)).click()

@allure.step('ищем')
def search_pull():
    s('#pull-requests-tab').click()
    s(by.text('Fix pull request close test')).click()