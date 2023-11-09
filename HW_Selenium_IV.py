import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

from login_page import Login_page

'''Создание класса'''
class Login():


    def test(self):
        a = 'C:\\Users\\Rail\\PycharmProjects\\python_Selenium'
        s = Service(a)
        driver = webdriver.Firefox(service=s)
        url = 'https://www.saucedemo.com/'  # базовый url
        url_inv = 'https://www.saucedemo.com/inventory.html'
        un = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']  # логин
        pw = 'secret_sauce'  # пароль
        problem_users = [] #список проблемных юзеров
        driver.get(url)  # вход на сайт по базовому url
        driver.maximize_window()  # открытие окна на максимальный размер
        print('Вход на сайт')
        for f in un:
            print(f'Тест юзера {f}')
            username = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # поиск поля user name
            username.send_keys(f)  # заполнение поля user name
            print('Логин введен')
            password = driver.find_element(By.XPATH, '//*[@id="password"]')  # поиск поля password
            password.send_keys(pw)  # заполнение поля password
            print('Пароль введен')
            username.send_keys(Keys.ENTER)  # нажимаем кноку Enter
            time.sleep(5) #ожидание на странице
            current_url = driver.current_url # проверка перехода на другую страницу
            if current_url != url_inv:
                problem_users.append(f) # добавление юзеров в список
                print(f'Проблемный юзер: {f}!!!')
                driver.refresh()
            driver.back()  # вернуться назад
            print(f'Тест юзера {f} завершен')
        print('Тест на авторизацию окончен')
        print(f'Пофиксить указанных юзеров {problem_users}')

client = Login()
client.test()
