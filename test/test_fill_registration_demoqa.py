

from selene import browser
import os.path

def date_generator(day: int, month: int, year: int):
    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__month-select option[value="{month - 1}"]').click()
    browser.element(f'.react-datepicker__year-select option[value="{year}"]').click()
    if day >= 10:
        browser.element(f'.react-datepicker__day.react-datepicker__day--0{day}').click()
    else:
        browser.element(f'.react-datepicker__day.react-datepicker__day--00{day}').click()

def test_fill_registration_demoqa(window_browser):
    browser.open('https://demoqa.com/automation-practice-form') # Открытие страницы для заполнения формы

    # Заполнение регистрационной формы

    # Персональные данные
    browser.element('#firstName').type('Виталий')  # Имя
    browser.element('#lastName').type('Ерёмин') # Фамилия
    browser.element('#userEmail').type('Eryomin@bk.ru') # Адрес электронной почты
    browser.element('[for="gender-radio-1"]').click() # Пол
    browser.element('#userNumber').type('9109176995') # Контактный номер

    # Выбор даты рождения
    browser.element('#dateOfBirthInput').click()
    date_generator(22, 1, 1978)

    # Увлечения, интересы
    browser.element('#subjectsInput').type('Book').press_tab()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()

    # Картинка
    browser.element('#uploadPicture').send_keys(os.path.abspath('img.png'))

    # Адрес проживания
    browser.element('#currentAddress').set_value('Obninsk, Blohinceva street, 11')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()

    # Подтверждение отправки заполненной формы
    browser.element('#submit').click()

