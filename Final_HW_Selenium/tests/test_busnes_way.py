import datetime
import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium_stealth import stealth
from selenium.webdriver.common.by import By


from pages.fork import Fork
from pages.payment import Payment
from pages.select_filters import Select_filters
from pages.select_product import Select_product
from pages.start_page import Start_page

'''Бизнес путь покупки товаров'''


def test_select_product_1():
    a = 'C:\\Users\\Rail\\PycharmProjects\\python_Selenium'
    s = Service(a)
    driver = webdriver.Firefox(service=s)
    options = Options()
    options.page_load_strategy = 'eager'


    sp = Start_page(driver)
    sp.start()

    sf = Select_filters(driver)
    sf.select()

    select_product = Select_product(driver)
    select_product.products()

    f = Fork(driver)
    f.text_check()

    pm = Payment(driver)
    pm.pay()

