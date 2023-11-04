import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url #получить текущий URL
        print(f'Текущий URL {get_url}')

    def assert_text(self, word, result):
        value_word = word.text #получить текст по локатору
        print(value_word)
        assert value_word == result #сравнение текста по локатору с заданным текстом
        print('OK')

    def assert_url(self, result):
        get_url = self.driver.current_url #получить текущий URL
        print(f'Полученный URL {get_url}')
        assert get_url == result #сравнение текущего URL с заданным URL
        print('OK URL')

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime('%Y.%m.%d.%H.%M.%S') #получение сегодняшней даты
        name_screenshot = 'screenshot' + now_date + '.png' #название скриншота и расширение
        self.driver.save_screenshot('C:\\Users\\Rail\\PycharmProjects\\Final_HW_Selenium\\screen\\' + name_screenshot) #путь сохранения скриншота


    def quit(self):
        self.driver.quit() #выйти из браузера
        print('Вышли из браузера')
        print('Тестирование окончено')