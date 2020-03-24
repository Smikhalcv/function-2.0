import json

class Contact:
    def __init__(self, name, last_name, phone_number, chosen=False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.chosen = chosen
        self.kwargs = kwargs

    def __str__(self):
        if self.chosen == False:
            represent_chosen = 'Нет'
        else:
            represent_chosen = 'Да'
        represent_kwargs = ''
        if self.kwargs:
            for k, v in self.kwargs.items():
                represent_kwargs += f'\t {k} : {v} \n'
            response = (f'''Имя: {self.name}
Фамилия: {self.last_name}
Телефон: {self.phone_number}
В избраных: {represent_chosen}
Дополнительная информация:
{represent_kwargs}''')
        else:
            response = (f'''Имя: {self.name}
Фамилия: {self.last_name}
Телефон: {self.phone_number}
В избраных: {represent_chosen}
''')
        return response

class Phone_Book():

    phone_book = {}

    def __init__(self, name):
        self.name = name


    def add_contact(self, *contact):
        if contact:
            for man in contact:
                if type(man) == Contact:
                    self.phone_book[f'id {str(len(self.phone_book))} {man.name} {man.last_name}'] = man
                if type(man) != Contact:
                    print(f'Констакт {man} не принадлежит к классу Contact')
        else:
            print('Укажите контакт, который необходимо добавить')

    def del_tel_contact(self, tel): # Показывает контакт по номеру телефона
        if tel:
            for k, v in self.phone_book.items():
                if tel == v.phone_number:
                    del_key = k
            del self.phone_book[del_key]
        else:
            print('Нет такого контакта.')

    def show_chosen_contact(self): # Показывает избранные контакты
        chosen_id = []
        for k, v in self.phone_book.items():
            if v.chosen == True:
                chosen_id.append(k)
        for id in chosen_id:
            print(self.phone_book[id])

    def show_name_contact(self, name): # показывает контакт по имени и фамилии контакта
        while True:
            key_show = [] # list key for delete
            if len(name.split()) == 2: # must input name and last name
                first_name, last_name = name.split()
                for k, v in self.phone_book.items(): # перебирает телефонную книгу и имя и фамилия есть в ней, записывает Id
                    if last_name == v.last_name and first_name == v.name:
                        key_show.append(k)
                if key_show:
                    for id in key_show:
                        print(self.phone_book[id])
                    break
            if len(name.split()) != 2:
                print('Введите Имя и Фимилию контакта')
                name = input()

    def show_contacts(self):
        for contact in self.phone_book.values():
            print(contact)

def adv_print(text, start='', max_line=None, in_file=None):
    if max_line:
        text = str(text)
        data = []
        for i in range((len(text) // max_line) + 1):
            for e in range(len(text) + max_line):
                if e == max_line * (i + 1):
                    data.append(text[max_line * (i):max_line * (i + 1)])
        text = '\n'.join(data)

    if start:
        text = str(text)
        start = str(start + '\n')
        text = start + text
    print(text)
    if in_file:
        in_file = str(in_file)
        text = text.split('\n')
        with open((in_file + '.json'), 'w', encoding='utf-8') as file:
            json.dump(text, file, ensure_ascii=False, indent=2)
        print(f'Файл {in_file}.json создан.')