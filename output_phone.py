import find_phone as fph

def print_phone(data):
    phone=fph.find_data(data)
    print(f'Телефон {data} -')
    print(*phone)