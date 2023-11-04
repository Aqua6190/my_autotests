import time
from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
class Placing_an_order(Base):




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    courier = '//div[@class="checkout-delivery__tab-link"]'#локатор выбора курьера
    adress = '//textarea[@placeholder="город, улица, дом, квартира"]'#локатор поля ввода адреса
    adress_2 = '//span[@class="dadata-suggestions__item"]'#локатор выбора адреса из дроп-даун меню
    name = '//input[@placeholder="Имя"]'#локатор поля ввода имени
    last_name = '//input[@placeholder="Фамилия"]'#локатор поля ввода фамилии
    e_mail = '//input[@placeholder="E-mail"]'#локатор поля ввода e-mail
    phone_number = '//input[@placeholder="Телефон"]'#локатор поля ввода телефона
    placing_an_order = '//button[@class="total-sum__btn button button--accent button--large button--full-width"]'#локатор кнопки оформления заказа


    #Getters

    def get_courier(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.courier)))

    def get_adress(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.adress)))

    def get_adress_2(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.adress_2)))
    def get_name(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_last_name(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_e_mail(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail)))

    def get_phone_number(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_placing_an_order(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.placing_an_order)))


    #Actions

    def click_courier(self):
        self.get_courier().click()#нажали выбрать курьера
        print('Выбрали курьера')


    def sroll(self):
        self.driver.execute_script('window.scrollTo(0, 400)')#сделали скролл
        print('Скролл')
        time.sleep(2)

    def input_adress(self):
        self.get_adress().send_keys('г Астрахань, ул Ленина, д 1')#ввели адрес доставки
        self.get_adress_2().click()#выбрали адрес из дроп-даун меню
        print('Ввели адрес')


    def input_personal_data(self):
        self.get_name().send_keys('Рикардо')#ввели имя
        print('Ввели имя')
        self.get_last_name().send_keys('Милос')#ввели фамилию
        print('Ввели Фамилию')
        self.get_e_mail().send_keys('Name_lastname@meil.com')#ввели e-mail
        print('Ввели e-mail')
        self.get_phone_number().send_keys('9990000000')#ввели телефон
        print('Ввели телефон')

    def click_order_button(self):
        self.get_placing_an_order().click()#нажали на кнопку оформить заказ
        print('Нажали на кнопку оформить заказ')

    def order(self):
        self.get_current_url()#Получили текущий URL
        self.sroll()#скрол
        self.click_courier()#выбрать курьера
        self.input_adress()#ввести адрес
        self.input_personal_data()#ввели персональные данные
        self.click_order_button()#нажали оформить заказ

