import time
from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
class Payment(Base):




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    frame = '//iframe[@class=" with-appled"]'
    card_number = '//input[@id="card"]'
    date = '//input[@id="date"]'
    cvv = '//input[@id="cvv"]'
    pay_button = '//span[@class="currency"]'
    text = '//div[contains(text(),"Операция")]'



    #Getters
    def get_card_number(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.card_number)))

    def get_frame(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.frame)))

    def get_date(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.date)))
    def get_cvv(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.cvv)))
    def get_pay_button(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.pay_button)))

    def get_text(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.text)))

    #Actions

    def payment(self):
        self.driver.switch_to.frame(self.get_frame())#переключиться на фрейм
        print('Переключились на фрейм')
        self.get_card_number().send_keys('4242424242424242')#ввести номер карты
        print('Ввели номер карты')
        self.get_date().send_keys('1225')#ввести дату
        print('Ввели дату')
        self.get_cvv().send_keys('000')#ввести CVV
        print('Ввели cvv')
        self.get_pay_button().click()#нажать оплатить
        print('Нажали на кнопку оплатить')





    def pay(self):
        self.get_current_url()#получить текущий URL
        self.payment()#ввести данные карты
        self.quit()# выход из тестирования