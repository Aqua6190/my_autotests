import datetime
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
class Select_filters(Base):




    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    popup_2 = '//div[@class="popmechanic-close"]'#локатор второго попапа
    filters = '//span[@class="filters__show-text"]'#локатор вкладки фильтры
    price_range_1 = '//input[@class="input price-range__value text-b7"]'#локатор поля цены от
    price_range_2 = '(//div[contains(@class, "price-range__values")]//input)[2]'#локатор поля цены до
    check_box_size = '//label[text()= "L"]'#локатор размера
    color = '//label[@for="chk-49-2229"]'#локатор цвета
    post = '//label[@for="chk3"]'#локатор возможности доставки
    main_filters = "//div[@class='filters__main']"#локатор меню фильтров
    button_show = "//button[@class='button button--default filters__button filters__button--apply text-b5']"#локатор кнопки показать


    #Getters
    def get_popup_2(self):
      return WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH, self.popup_2)))

    def get_filters(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.filters)))

    def get_price_range_1(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.price_range_1)))

    def get_price_range_2(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.price_range_2)))

    def get_check_box_size(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.check_box_size)))

    def get_color(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.color)))

    def get_post(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.post)))

    def get_main_filters(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.main_filters)))

    def get_button_show(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))

    #Actions

    def click_popup_2(self):
        try:
            self.get_popup_2().click()#закрытие второго попапа, если появился
            print('Закрыли второй попап')
        except TimeoutException:
            print('Попап не появился')

    def click_filters(self):
        self.get_filters().click()#открыть фильтры
        print('Открыли фильтры')

    def input_price_range(self, value_1, value_2):
        self.get_price_range_1().send_keys(value_1)#ввели цену от
        self.get_price_range_2().send_keys(value_2)#ввели цену до
        print('Указали диапазон')

    def click_check_box_size(self):
        self.get_check_box_size().click()#выбрали размер
        print('Выбрали размер')

    def click_color(self):
        self.get_color().click()#выбрали цвет
        print('Выбрали цвет')

    def move(self):
        self.get_main_filters().click()#кликнули на поле меню фильтров
        self.get_main_filters().send_keys(Keys.SPACE)#пролистнули

    def click_post(self):
        time.sleep(5)
        self.get_post().click()#выбрали доставку
        print('Выбрали возможность доставки')

    def click_button_show(self):
        self.get_button_show().click()#нажали на кнопку
        print('Нажали на кнопку "Показать товар"')
    def select(self):
        self.click_popup_2()#действие для закрытие поапа
        self.click_filters()#действие для открытия фильтров
        self.input_price_range(500, 3000)#действие для задания диапазона цены
        self.click_check_box_size()#действие для выбора размера
        self.click_color()#действие для выбора цвета
        self.move()#действие для прокрутки меню
        self.click_post()#действие для выбора доставки
        self.click_button_show()#действие для нажатия кнопки