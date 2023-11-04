import time
from telnetlib import EC

from selenium.common import TimeoutException, MoveTargetOutOfBoundsException, ElementNotInteractableException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
class Select_product(Base):




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    product = '//img[@alt="Свитшот оверсайз с принтом медведя"]'#локатор выбираемого товара
    button_cart = '//button[@class="button button--default product-detail__to-cart text-b5"]'#локатор кнопки
    text = '//h1[@class="product-detail__title"]'#локатор названия выбранного товара


    #Getters
    def get_product(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.product)))

    def get_button_cart(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_cart)))

    def get_text(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.text)))

    #Actions

    def click_product(self):
        try:
            self.get_product().click()#выбрали товар
            print('Выбрали товар')
        except ElementNotInteractableException:
            self.driver.execute_script('window.scrollTo(0, 750)')  # скрол вниз
            print('Скролл')
            time.sleep(2)
            self.get_product().click()  # выбрали товар
            print('Выбрали товар')
    def sroll(self):
        self.driver.execute_script('window.scrollTo(0, 400)')#скрол вниз
        print('Скролл')
        time.sleep(2)


    def click_button_cart(self):
        self.get_button_cart().click()#положили в корзину
        print('Нажали добавить в корзину')
        self.get_button_cart().click()
        print('Нажали оформить заказ')#нажали на кнопку оформления заказа

    def products(self):
        self.get_current_url()#получение текущего URL
        self.click_product()#выбор товара
        self.get_current_url()#получение текущего URL
        self.assert_url('https://tvoe.ru/product/tolstovka-s-kapyushonom-belyy-96886/#1064304')#действие для assert URL
        self.assert_text(self.get_text(),"СВИТШОТ ОВЕРСАЙЗ С ПРИНТОМ МЕДВЕДЯ")#действие для assert названия
        self.sroll()#скролл
        self.click_button_cart()#нажать на кнопка в корзину/оформить заказ

