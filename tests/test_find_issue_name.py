import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


"""
просто тест
"""


def test_github():
    browser.open('https://github.com/')
    s('.header-search-input').send_keys('eroshenkoam/allure-example')
    s('.header-search-input').submit()
    s(by.link_text('eroshenkoam/allure-example')).click()
    s('#issues-tab').click()
    s(by.partial_text('#76')).should(be.visible)

"""
лямбда
"""

def test_dymamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()


    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)


"""
декораторы
"""


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий')
def search_for_repository(repo):
    browser.element('.header-search-input').send_keys(repo)
    browser.element('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Открываем таб Issues')
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверяем наличие issue с номером 76')
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).click()


"""
аннотации
"""


def test_dymamyc_label():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.label('owner', 'kukushkina')
    allure.dynamic.feature('Задачи и репозитори')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу')
    allure.dynamic.link('https://github.com/', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner' , 'kukushkina')
@allure.feature('Задачи и репозитори')
@allure.story('Пользователь может создать задачу')
@allure.link('https://github.com/', name='Testing')
def test_decorator_label():
    pass