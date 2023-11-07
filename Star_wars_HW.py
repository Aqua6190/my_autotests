import requests

'''Создание класса'''
class Star_wars():

    '''Поиск фильмов с участием Дарта Вейдера'''
    @staticmethod
    def dart_veider():
        veider_url = 'https://swapi.dev/api/people/4/' # URL Дарта Вейдера
        print(veider_url) # вывод URL Дарта Вейдера
        result = requests.get(veider_url) #запрос GET по URL Дарта Вейдера
        result.status_code #получение статус кода
        print(f'Статус код: {result.status_code}') #вывод статус кода
        assert result.status_code == 200 #проверка статус кода
        print('Запрос выполнен успешно!')
        print(result.text) #вывод текста запроса

        check = result.json() #вывод json запроса
        check_info = check.get('films') #поиск значения в списке films
        print(f'Список URL фильмов, в которых появлялся Дарт Вейдер: {check_info}') #вывод cписка фильмов с Дартом Вейдером
        return check_info #возвращение переменной для передачи ее в другую функцию

    '''Поиск персонажей, которые участвовали в фильмах с Дартом Вейдером'''
    @staticmethod
    def films_with_veider(check_info):
        list = [] #список, куда будут вноситься персонажи
        for f in check_info: #циклом проходимся по списку фильмов
            print(f) #вывод URL фильма
            result = requests.get(f) #выполнение запроса GET по фильму
            result.status_code #получение статус кода
            print(f'Статус код: {result.status_code}')#вывод статус кода
            assert result.status_code == 200 #проверка статус кода
            print('Запрос выполнен успешно!')
            print(result.text)#вывод текста запроса

            check = result.json() #получение json запроса
            check_info_1 = check.get('characters') #поиск значения в списке characters
            print(f'Список персонажей в фильме: {check_info_1}') #вывод списка персонажей в фильме

            for f_1 in check_info_1:

                print(f'URL Персонажа: {f_1}') #вывод URL персонажа
                result = requests.get(f_1) #запрос GET по URL персонажа
                result.status_code #получение статус кода
                print(f'Статус код: {result.status_code}') #вывод статус кода
                assert result.status_code == 200 #проверка статус кода
                print('Запрос выполнен успешно!')
                print(result.text) #вывод текста запроса
                check = result.json() #получение json запроса
                check_info_2 = check.get('name')#поиск значения в списке name
                print(f'Имя персонажа - {check_info_2}') #вывод имени персонажа
                if check_info_2 in list: #проверка: присутствует ли персонаж в списке
                   print('Персонаж уже присутствовал')
                else:
                    list.append(check_info_2)#добавление персонажа в список
        return list #возвращение переменной для передачи ее в другую функцию

    '''Добавление персонажей в текстовый файл'''
    @staticmethod
    def add_pers_in_fail(list):
        for f_2 in list:
            f = open('API_Homework/Персонажи.txt', 'a', encoding='utf-8')
            f.write(f'{f_2}\n')
            f.close()

per = Star_wars()
per.add_pers_in_fail(per.films_with_veider(per.dart_veider()))