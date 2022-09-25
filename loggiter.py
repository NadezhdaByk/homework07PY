import input_data as inp
import menu

def log_data():
    name=inp.input_name()
    phone=inp.input_phone()
    with open('phone.txt', 'a+', encoding='UTF-8') as file:
        file.write(f'{name}: телефон {phone}\n')

