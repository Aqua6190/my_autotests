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
class Placing_an_order_v_2(Base):




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    """ВЕРСИЯ ПОД ДРУГУЮ ВЕРСТКУ"""
    # Locators
    next = '//div[@class="checkout-miniature-slider__nav-button checkout-miniature-slider__nav-button--next"]'#локатор стрелки
    choise_post = '//button[contains(text(),"Выбрать")] '#локатор выбора способа доставки
    post_window = '//div[@class="checkout-delivery__content"]'
    courier = '//div[@class="checkout-delivery__tab"]/span[text()= "курьером"]'#локатор курьера
    adress = '//textarea[@placeholder="улица, дом, квартира"]'#локатор поля ввода адреса
    adress_2 = '//span[@class="dadata-suggestions__item"]'#локатор адреса из дроп-даун меню
    add_this_adress = '//button[@class="button button--default button--full-width checkout__button"]'#локатор кноки доставить на этот адрес
    name = '//input[@name="name"]'#локатор ввода имени
    e_mail = '//input[@name="email"]'#локатор ввода e-mail
    phone_number = '//input[@name="phone"]'#локатор ввода телефона
    continue_ = '//button[@class="button button--default button--full-width checkout-client__button"]'#локатор ввода телефона
    pay_button = '//button[text()="Оплатить заказ"]'#локатор кнопки оплатить заказ


    #Getters

    def get_next(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.next)))

    def get_choise_post(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.choise_post)))

    def get_post_window(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.post_window)))

    def get_courier(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.courier)))
    def get_adress(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.adress)))

    def get_adress_2(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.adress_2)))

    def get_add_this_adress(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.add_this_adress)))

    def get_name(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_continue_(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.continue_)))

    def get_e_mail(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail)))

    def get_phone_number(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_pay_button(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.pay_button)))

    #Actions

    def choise_post_(self):
        self.get_choise_post().click() #нажать на кнопку выбрать способ доставки
        print('Нажали кнопку ВЫБРАТЬ СПОСОБ ДОСТАВКИ')
        time.sleep(3)

    def choise_courier(self):
        self.get_next().click()#нажать на стрелочку, чтобы прокрутить слайдер
        time.sleep(1)
        self.get_next().click()#нажать на стрелочку, чтобы прокрутить слайдер
        self.get_courier().click()#выбрать курьером
        print('Выбрали курьером')


    def input_adress(self):
        self.get_adress().send_keys('г Астрахань, ул Ленина, д 1')#ввести адрес
        self.get_adress_2().click()#выбрать адрес из дроп даун меню
        print('Ввели адрес')

    def sroll(self):
        self.driver.execute_script('window.scrollTo(0, 400)')#скролл
        print('Скролл')
        time.sleep(2)

    def click_add_this_adress(self):
        self.get_add_this_adress().click()#нажать на кнопку Доставить на этот адрес
        print('Нажали на кнопку "Доставить на этот адрес"')

    def input_personal_data(self):
        self.get_name().send_keys('Рикардо Милос')#ввести имя и фамилию
        print('Ввели имя')
        self.get_e_mail().send_keys('Name_lastname@meil.com')#ввести e-mail
        print('Ввели e-mail')
        self.get_phone_number().send_keys('99900000000')#ввести телефон
        print('Ввели телефон')

    def click_order_button(self):
        self.get_continue_().click()#нажать продолжить
        time.sleep(3)
        print('Нажали на кнопку ПРОДОЛЖИТЬ')
        self.get_pay_button().click()#нажать оплатить
        print('Нажали на кнопку ОПЛАТИТЬ')

    def order(self):
        self.get_current_url()#получить текущий URL
        self.choise_post_()#выбрать способ доставки
        self.choise_courier()#выбрать курьера
        self.input_adress()#ввести адрес
        self.sroll()#скролл
        self.click_add_this_adress()#доставить на этот адрес
        self.input_personal_data()#ввести ерсональные данные
        self.click_order_button()#оформить заказ

