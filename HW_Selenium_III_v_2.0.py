import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

'''Создание класса'''
class Product():

       ''' Выбор товаров покупателем'''
       @staticmethod
       def Choice():
              print('Приветствуем Вас в нашем магазине \n"У Чака Норриса",\n' #приветствие
                    'пожалуйста, выберете товар(ы)')
              print(f'1- Sauce Labs Backpackn\n' #показ ассортимента товаров
                    f'2- Sauce Labs Bike Light\n'
                    f'3- Sauce Labs Bolt T-Shirt\n'
                    f'4- Sauce Labs Fleece Jacket\n'
                    f'5- Sauce Labs Onesie\n'
                    f'6- Test.allTheThings() T-Shirt (Red)')
              product = () #выбранный товар
              list_choice = []#список выбранных товаров
              list_1 = ['1', '2', '3', '4', '5', '6','ok']#список для сверки с выбором покупателя
              while product != 'ok':#цикл на выбор товаров
                product = (input('Введите цифру вашего товара или введите "ok":'))#ввод цифры товара
                if product in list_choice:#сверка на недопущение дубликатов
                    print('Товар уже выбран')
                if product in list_1:#сверка со списком товаров
                    list_choice.append(product)#добавление товара в список выборов покупателя
                else:#если введено значение, которое не присутствует в списке
                    print('Такого товара нет')
              list_choice.pop()#удаление из списка покупателя значения 'ok'
              list_choice_f =list(set(list_choice))#удаление дубликатов выбора

              product_range = ['', 'Sauce Labs Backpack', 'Sauce Labs Bike Light',
                               'Sauce Labs Bolt T-Shirt', 'Sauce Labs Fleece Jacket', 'Sauce Labs Onesie',
                               'Test.allTheThings() T-Shirt (Red)']#список названий товаров
              for f in list_choice_f:#цикл на вывод списка выбранного товара
                pr = product_range[int(f)]#получение значения по индексу в списке
                print(f'Вы выбрали: {pr}')
              return list_choice_f#передача переменной в функцию Sell

       '''Бизнес путь покупки товаров'''
       @staticmethod
       def Sell(list_choice_f):
           a = 'C:\\Users\\Rail\\PycharmProjects\\python_Selenium'
           s = Service(a)
           driver = webdriver.Firefox(service=s)

           list_product_xpath = ['',
                                 '//*[@id="add-to-cart-sauce-labs-backpack"]',
                                 '//*[@id="add-to-cart-sauce-labs-bike-light"]',
                                 '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]',
                                 '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]',
                                 '//*[@id="add-to-cart-sauce-labs-onesie"]',
                                 '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]']#список локаторов всех товаров
           url = 'https://www.saucedemo.com/'  # базовый url
           un = 'standard_user'  # логин
           pw = 'secret_sauce'  # пароль
           first_name = 'Chuck'  # имя покупателя
           last_name = 'Norris'  # фамилия покупателя
           zip = 777  # zip покупателя
           driver.get(url)  # вход на сайт по базовому url
           driver.maximize_window()  # открытие окна на максимальный размер
           print('Вход на сайт')
           username = driver.find_element(By.XPATH, '//*[@id="user-name"]')  # поиск поля user name
           username.send_keys(un)  # заполнение поля user name
           print('Логин введен')
           password = driver.find_element(By.XPATH, '//*[@id="password"]')  # поиск поля password
           password.send_keys(pw)  # заполнение поля password
           print('Пароль введен')
           username.send_keys(Keys.ENTER)  # нажимаем кноку Enter

           for f1 in list_choice_f:#цикл на выбор локаторов товаров из списка покупок покупателя
               xp = list_product_xpath[int(f1)]#получение значения по индексу в списке
               button_1 = driver.find_element(By.XPATH, xp)  # поиск кнопки заказа товара
               button_1.click()  # нажать на кнопку заказа товара

           '''Переходим в корзину'''
           basket = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')  # поиск кнопки перехода в корзину
           basket.click()  # нажать на кнопку перехода в корзину
           time.sleep(5)
           print('Переход в корзину')

           '''Ввод данных покупателя'''
           checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')  # поиск кнопки checkout
           checkout.click()  # нажатие кнопки checkout
           print('Переход к заполнению данных пользователя')

           first_field = driver.find_element(By.XPATH, '//*[@id="first-name"]')  # поиск первого поля
           first_field.send_keys(first_name)  # ввод данных
           print('Имя введено')
           second_field = driver.find_element(By.XPATH, '//*[@id="last-name"]')  # поиск второго поля
           second_field.send_keys(last_name)  # ввод данных
           print('Фамилия введена')
           third_field = driver.find_element(By.XPATH, '//*[@id="postal-code"]')  # поиск третьего поля
           third_field.send_keys(zip)  # ввод данных
           print('Zip введен')
           time.sleep(2)
           continu = driver.find_element(By.XPATH, '//*[@id="continue"]')  # поиск кнопки continue
           continu.click()  # нажатие кнопки continue

           '''Завершающий этап'''

           finish = driver.find_element(By.XPATH, '//*[@id="finish"]')  # поиск кнопки finish
           finish.click()  # нажатие кнопки finish
           print('Покупка завершена!')


buy = Product()
buy.Sell(buy.Choice())