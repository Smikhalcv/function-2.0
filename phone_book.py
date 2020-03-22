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

    def del_contact(self, *contact): #Удаляет контакт если он записан в переменную
        if contact:
            for man in contact:
                for k, v in self.phone_book.items():
                    if man == v:
                        key_del = k
                if key_del:
                    del self.phone_book[key_del]
                else:
                    print('Нет такого контакта.')

    def del_name_contact(self, name): # Удаляет контакт по имени и фамилии контакта
        while True:
            key_del = [] # list key for delete
            if len(name.split()) == 2: # must input name and last name for to delete
                first_name, last_name = name.split()
                for k, v in self.phone_book.items(): # перебирает телефонную книгу и имя и фамилия есть в ней, записывает Id для удаления
                    if last_name == v.last_name and first_name == v.name:
                        key_del.append(k)
                if key_del:
                    if len(key_del) > 1: # Если есть несколько контактов с одинаковыми именами и фамилиями спрашивает что удалять
                        print(f'Контактов с именем {first_name} {last_name} больше одного, укажите id {key_del}'
                              f'или введите all, если '
                              f'хотите все контакты с таким именем')
                        id = input('- ')
                        if id.lower() == 'all':
                            for key in key_del:
                                del self.phone_book[key]
                            break
                        if id in self.phone_book.keys():
                            del self.phone_book[id]
                            break
                        else:
                            print('Неверно указан id')
                    if len(key_del) == 1: # удаляет если нет повторений
                        del self.phone_book[key_del]
                        break
                    else:
                        print(f'Contact {first_name} {last_name} не существует в телефоннной книге')
                break
            if len(name.split()) != 2:
                print('Введите Имя и Фимилию контакта')
                name = input()

    def show_contacts(self):
        for contact in self.phone_book.values():
            print(contact)

