from telnetlib import EC

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Start_page(Base):

    url = 'https://tvoe.ru/#'#URL сайта ТВОЁ


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    popup = '//button[@class="popup__close"]' #локатор попапа
    catalog = '//a[@href="/catalog/mujchinam/"]' #локатор каталога
    value = '//h1[@class="top-block__page-title"]' #надпись для assert
    odejda = '/html/body/div[4]/div/header/div[2]/div[1]/div/ul/li[2]/div/ul/li[1]/div[1]/a'
    t_shirt = '//a[@href="/catalog/mujchinam/odejda/tolstovka/"]' #локатор толстовок, свитшотов и худи
    close_cookie_message = '//div[@class="popmechanic-close"]' #локатор попапа о кукки


    #Getters
    def get_catalog(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_popap(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.popap)))

    def get_popup(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.popup)))

    def get_close_cookie_message(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.close_cookie_message)))

    def get_odejda(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.odejda)))

    def get_t_shirt(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.t_shirt)))

    def get_value(self):
      return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.value)))


    #Actions

    def get_actions(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_catalog()).perform() #навели указатель на вкладку "Мужчинам"
        print('Выбрали "Мужчинам"')
        action_2 = ActionChains(self.driver)
        action_2.move_to_element(self.get_odejda()).perform()#навели указатель на вкладку "Одежда"
        print('Выбрали "Одежда"')
        action_3 = ActionChains(self.driver)
        action_3.move_to_element(self.get_odejda()).perform()#навели указатель на вкладку "Толствоки, худи свитшоты"
        print('Выбрали "Толстовки, свитшоты,худи"')

    def click_popup(self):
        self.get_popup().click() #закрыли всплывающий поп с выбором города
        print('Закрыли попап')

    def click_close_cookie_message(self):
        self.get_close_cookie_message().click() #закрыли сообщение о cookie
        print('Закрыли cообщение о cookie')
    def get_click_t_shirt(self):
        self.get_t_shirt().click()
        print('Выбрали толстовку')

    def start(self):
        self.driver.get(self.url) #открыть сайт
        self.driver.maximize_window() #открыть окно на максимальный размер
        self.get_current_url()#получение текущего URL
        self.click_popup()#действие для закрытие попапа
        self.click_close_cookie_message()#действие для закрытие попапа о кукки
        self.get_actions()#действие для наведения указателя мыши
        self.get_click_t_shirt()#кликнуть по выбору каталога
        self.assert_url('https://tvoe.ru/catalog/mujchinam/odejda/tolstovka/')#проверка URL
        self.assert_text(self.get_value(), 'ТОЛСТОВКИ, СВИТШОТЫ, ХУДИ ДЛЯ МУЖЧИН')#проверка что зашли на нужную страницу


