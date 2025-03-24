import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_github():
    with allure.step("Открываем гланвую страницу github"):
        browser.open('https://github.com')

    with allure.step("Ищем репозиторий eroshenkoam"):
        s('.header-search-button').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step("Ищем тестовый пример"):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("ищем тестовый запрос"):
        s('#pull-requests-tab').click()
        s(by.text('Fix pull request close test')).click()