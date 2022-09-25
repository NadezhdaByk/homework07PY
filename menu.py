import loggiter as log
import find_phone as fph
import output_phone as oph

def start():
    var = input('Добро пожаловать! Если Вы хотите ВВЕСТИ номер телефона в стправочник нажмите 1. Если Вы хотите НАЙТИ телефон в справочнике нажмите 2: ')

    if var == '1':
        log.log_data()
    if var == '2':
        data=input('Номер какого человека найти? ')
        # fph.find_data(data)
        oph.print_phone(data)
