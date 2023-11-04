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

from pages.placing_an_order import Placing_an_order
from pages.placing_an_order_v_2 import Placing_an_order_v_2


class Fork(Base):

#ПО НЕВЫЯСНЕННЫМ ПРИЧИНАМ ПРИ ОФОРМЛЕНИИ ЗАКАЗА ВЫХОДЯТ ДВЕ РАЗЛИЧНЫЕ ВЕРСТКИ СТРАНИЦЫ
#С ЧЕМ ЭТО СВЯЗАННО НЕИЗВЕСТНО, ПРЕДУГАДАТЬ ЭТО НЕВОЗМОЖНО, ПОЭТОМУ ЗДЕСЬ ПРИСУТСТВУЕТ "ВИЛКА"
#ЕСЛИ ПРОВЕРКА ПО ТЕКСТУ ПРОШЛА УСПЕШНО ЗАПУСКАЕТСЯ ТЕСТ PLACING AN ORDER, В ИНОМ СЛУЧАЕ ТЕСТ PLACING AN ORDER V.2

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    check = '//h1[@class="title title--h1"]'# локатор фразы "Оформление заказа"

    #Getters

    def get_check(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.check)))

    #Actions
    def text_check(self):
        try:
            self.assert_text(self.get_check(), 'Оформление заказа')# проверка наличия фразы
            print('верстка №1')
            po = Placing_an_order(self.driver)# запуск теста с первой версткой
            po.order()
        except TimeoutException:
            print('верстка №2')
            po_v_2 = Placing_an_order_v_2(self.driver)#запуск теста со второй версткой
            po_v_2.order()















        # print('ошибка')
        # self.get_check().text()
        # print('ошибка-1')
        # print(self.get_check().text())
        # print('ошибка-2')
        # if self.get_check().text() == 'ОФОРМЛЕНИЕ ЗАКАЗА':
        #     print('верстка №1')
        #     po = Placing_an_order(self.driver)
        #     po.order()
        # else:
        #     print('верстка №2')
        #     po_v_2 = Placing_an_order_v_2(self.driver)
        #     po_v_2.order()



