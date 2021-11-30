import os


class Customer:
    def __init__(self, customer_file=None, customer_data=None):
        self.customer_data = {}
        self.customer_file = ''
        self.person_file = ''

    def input_surname(self):
        surname = input('Фамилия: ').capitalize()
        if not surname.isalpha():
            print('Внимание! Фамилия должна содержать только буквенные символы. Попробуйте еще раз')
            return self.input_surname()
        return surname

    def input_name(self):
        name = input('Имя: ').capitalize()
        if not name.isalpha():
            print('Внимание! Имя должно содержать только буквенные символы. Попробуйте еще раз')
            return self.input_name()
        return name

    def input_patronymic(self):
        patronymic = input('Отчество: ').capitalize()
        if not patronymic.isalpha():
            print('Внимание! Отчество должно содержать только буквенные символы. Попробуйте еще раз')
            return self.input_patronymic()
        return patronymic

    @staticmethod
    def digit_collect(string, sep):
        """
        DOCSTRING: Проверяет условие: "строка должна содержать только цифры и sep"
        INPUT: string - произвольная строка
               sep - допустимый разделитель символов строки
        RETURN: Возвращает '', если строка содержит недопустимые символы
                Возвращает строку из цифр без разделителя, если строка содержит только цифры и допустимый разделитель
        """
        for symbol in string:
            if symbol != sep and symbol.isdigit() is False:
                print('Использованы недопустимые символы!')
                digits = ''
                break
        else:
            digits = ''.join(string.split(sep))
        return digits

    @staticmethod
    def input_birth_date() -> str:
        birth_date = input('Дата рождения в формате ДД.ММ.ГГГГ: ')
        digits = Customer.digit_collect(birth_date, '.')
        if len(digits) == 8:
            return digits
        elif len(digits) != 8 and digits != '':
            print('Внимание! Некорректное количество символов в дате рождения')
        return Customer.input_birth_date()

    @staticmethod
    def input_passport_data():
        passport_data = input('Серия и номер паспорта: ')
        digits = Customer.digit_collect(passport_data, ' ')
        if len(digits) == 10:
            return digits
        elif len(digits) != 10 and digits != '':
            print('Внимание! Введено неверное количество цифр. Попробуйте еще раз')
        return Customer.input_passport_data()

    def get_data(self):  # Возвращает словарь с данными клиента
        print('Заполните анкету клиента')
        self.customer_data = {'Фамилия': self.input_surname(),
                              'Имя': self.input_name(),
                              'Отчество': self.input_patronymic(),
                              'Дата рождения': Customer.input_birth_date(),
                              'Паспорт': Customer.input_passport_data()
                              }
        return self.customer_data

    @staticmethod
    def write_to_file(path, info):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(info)

    def create_file(self):  # Создает файл клиента банка и файл физлица с одинаковым названием в
        # разных папках. Возвращат имя файла.
        self.customer_file = self.customer_data['Фамилия'] + self.customer_data['Имя'] + self.customer_data[
            'Отчество'] + self.customer_data['Дата рождения'] + self.customer_data['Паспорт'] + '.txt'
        Customer.write_to_file('Bank_clients/' + self.customer_file, str(self.customer_data))
        person_money = check_money(input('Нескромный вопрос: каким количеством наличных денег располагаете?: '))
        Customer.write_to_file('Physical_persons/' + self.customer_file, str(person_money))
        if self.customer_file in os.listdir(path='Bank_clients/'):
            print('Карточка клиента создана успешно')
        self.person_file = self.customer_file
        return self.person_file

    def incoming_customer_data(self):  # Запрашивает данные существующего клиента. Возвращает имя файла клиента банка
        # self.customer_file = self.input_surname() + self.input_name() + self.input_patronymic() + \
        #                      self.input_birth_date() + self.input_passport_data() + '.txt'
        # return self.customer_file
        customer_file = self.input_surname() + self.input_name() + self.input_patronymic() + self.input_birth_date() + self.input_passport_data() + '.txt'
        return customer_file

    def identification_client(self, customer_file):  # Идентификация клиента. Возвращает имя файла физлица.
        # if self.customer_file in os.listdir(path='Bank_clients/'):
        if customer_file in os.listdir(path='Bank_clients/'):
            self.customer_file = customer_file
            with open('Bank_clients/' + self.customer_file, 'r', encoding='utf-8') as file:
                dict_ = eval(file.read())
                name = dict_['Имя']
                surname = dict_['Отчество']
            print(f'Идентификация пройдена успешно. Добро пожаловать, {name} {surname} !\n')
            self.person_file = self.customer_file
        else:
            self.customer_file = ''
            print('Клиент отсутствует в базе!\n')
            answer = '0'
            while answer != '1' and answer != '2':
                print('Хотите стать клиентом нашего банка?\n'
                      '1) Да\n'
                      '2) Нет\n')
                answer = input()
                if answer == '1':
                    self.get_data()
                    self.create_file()
                    self.person_file = self.customer_file
                elif answer == '2':
                    print('До свидания!')
                else:
                    print('Неверный вариат ответа!')
        return self.person_file

    def status_select(self):
        print('Выберите ваш статус:\n'
              '1) Действующий клиент банка\n'
              '2) Новый клиент банка\n')
        choise = input()
        if choise == '1' or choise == '2':
            return choise
        else:
            print('Вариант с таким номером отсутствует!\n'
                  'Выберите один из предоставленных вариантов\n')
            return self.status_select()

    def add_deposit(self, amount):
        with open('Bank_clients/' + self.customer_file, 'r', encoding='utf-8') as file:
            client_info = eval(file.read())
            client_info['Дебет'] = amount
        Customer.write_to_file('Bank_clients/' + self.customer_file, str(client_info))

    def add_loan(self, amount):
        with open('Bank_clients/' + self.customer_file, 'r', encoding='utf-8') as file:
            client_info = eval(file.read())
            client_info['Кредит'] = amount
        Customer.write_to_file('Bank_clients/' + self.customer_file, str(client_info))

    def transfer(self):
        with open('Bank_clients/' + self.customer_file, 'r', encoding='utf-8') as file:
            client_info = eval(file.read())
        if 'Дебет' in client_info:
            amount = check_money(input('Укажите  сумму перевода:\n'))
            if client_info['Дебет'] >= amount:
                print('Укажите данные получателя')
                name = client.incoming_customer_data()
                try:
                    destination = open('Bank_clients/' + name, 'r', encoding='utf-8')
                except Exception:
                    print('Получатель не является клиентом нашего банка. Пока функционал программы ограничен,'
                          ' перевод невозможен')
                else:
                    receiver_info = eval(destination.read())
                    destination.close()
                    try:
                        receiver_info['Дебет'] += amount
                        Customer.write_to_file('Bank_clients/' + name, str(receiver_info))
                        client_info['Дебет'] -= amount
                        Customer.write_to_file('Bank_clients/' + self.customer_file, str(client_info))
                        print('Перевод выполнен!\n')
                    except Exception:
                        print('Невозможно выполнить перевод. У получателя не открыт расчетный счет!')
            elif client_info['Дебет'] < amount:
                print('На вашем счете недостаточно средств для проведения операции.')
            main_menu()
        else:
            print('Баланс вашего счета равен 0.00 руб. Для выполнения операции сначала пополните расчетный счет')
            main_menu()

    def account_balance(self):
        with open('Bank_clients/' + self.person_file, 'r', encoding='utf-8') as file:
            info = eval(file.read())
            if 'Дебет' in info.keys():
                print(f"Баланс вашего банковского счета: {info['Дебет']} руб.")
            else:
                print('У вас пока не открыт расчетный счет\n')
        main_menu()


class Client(Customer):
    def __init__(self, client_file=None):
        super().__init__(customer_file=None, customer_data=None)
        self.client_file = client_file
        self.money = self.read_money()

    def read_money(self) -> float:  # Возвращает остаток наличных средств у клиента
        with open(self.client_file, 'r') as file:
            info = float(file.read())
            return info

    def getting_loan(self, income) -> float:  # Возвращает значение: остаток наличных + заемные средства
        self.money = round(self.read_money() + float(income), 2)
        Customer.write_to_file(self.client_file, str(self.money))
        return income

    def debiting_money(self, debiting):  # Возвращает  и записывает в файл значение: остаток наличных - внесенные
        # средства, либо False, если недостаток средств
        if debiting > self.money:
            print('У вас недостаточно наличных средств для проведения данной операции!\n'
                  f'Напоминаем, что вы располагаете суммой: {self.money} руб.')
            return False
        else:
            self.money -= debiting
            Customer.write_to_file(self.client_file, str(round(self.money, 2)))
        return debiting


class Bank:

    @staticmethod
    def write_to_file(path, info):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(info)

    def __init__(self, name, corr_account_file):
        self.name = name
        self.corr_account_file = corr_account_file
        self.cor_account = self.read_cor_account()

    def greetings(self):
        print(f'Здравствуйте!\nДобро пожаловать в {self.name}!')
        print('В нашей инновационной консоли выбор нужного пункта меню осуществляется путем ввода соответствующей '
              'ему цифры и нажатия клавиши "Enter"')

    def read_cor_account(self):  # Остаток на к/счете на чтение
        with open(self.corr_account_file, 'r') as file:
            info = float(file.read())
            return info

    def receipt_of_money(self, amount):  # Внесение средств на к/счет
        self.cor_account = round(float(self.read_cor_account()) + amount, 2)
        Bank.write_to_file(self.corr_account_file, str(self.cor_account))

    def debiting_of_money(self, debiting):  # Списание средств с к/счета
        if debiting > self.read_cor_account():
            print('На к/счете недостаточно денег для проведения операции.\n'
                  'Вы же не хотите нас обанкротить?\n'
                  f'Максимально возможная сумма: {self.cor_account}')
            return False
        else:
            self.cor_account -= debiting
            Bank.write_to_file(self.corr_account_file, str(self.cor_account))
        return debiting

    def account_info(self):  # Вывод информации о балансе к/счета
        with open(self.corr_account_file, 'r') as file:
            print(f'Текущий баланс корр. счета: {file.read()} руб.')


def top_up_bank_account():
    amount = check_money(input('Укажите сумму для пополнения счета:\n'))
    if client.debiting_money(amount):
        bank.receipt_of_money(amount)
        customer.add_deposit(amount)
        print('Операция выполнена')
        main_menu()
    else:
        main_menu()


def get_loan():
    amount = check_money(input('Укажите желаемую сумму кредита:\n'))
    if bank.debiting_of_money(amount):
        client.getting_loan(amount)
        customer.add_loan(amount)
        print('Операция выполнена')
        main_menu()
    else:
        get_loan()


def create_account():
    with open('Bank_clients/' + customer.customer_file, 'r', encoding='utf-8') as file:
        info = eval(file.read())
        info['Дебет'] = 0
    Bank.write_to_file('Bank_clients/' + customer.customer_file, str(info))
    print('Счет открыт успешно')
    main_menu()


def check_money(balance):
    try:
        balance = round(float(balance.replace(',', '.')), 2)
    except Exception:
        return check_money(input('Сумма указана некорректно! Попробуйте еще раз:\n'))
    else:
        if balance < 0:
            return check_money(input('Сумма не должена быть отрицательной! Попробуйте еще раз:\n'))
        else:
            return balance


def main_menu():
    print('Выберите пункт меню:\n'
          '1) Открыть счет в банке\n'
          '2) Пополнить счет (включая открытие счета)\n'
          '3) Взять кредит\n'
          '4) Сделать перевод\n'
          '5) Баланс счета\n'
          '6) Выход\n')
    choise = input()
    if choise == '1':
        create_account()
    elif choise == '2':
        top_up_bank_account()
    elif choise == '3':
        get_loan()
    elif choise == '4':
        customer.transfer()
    elif choise == '5':
        customer.account_balance()
    elif choise == '6':
        print('До свидания!')
    else:
        print('Указан несуществующий пункт меню!\nПопробуйте еще раз!')
        main_menu()


if 'Bank_clients' not in os.listdir('.'):
    os.mkdir('Bank_clients')
if 'Physical_persons' not in os.listdir('.'):
    os.mkdir('Physical_persons')
if 'cor_account.txt' not in os.listdir('.'):
    balance = check_money(input('Господин председатель совета директоров, укажите баланс кор. счета вашего банка, руб.: '))
    Bank.write_to_file('cor_account.txt', str(balance))
    print('Благодарю! Больше мы вас не побеспокоим. Хорошего отдыха на Мальдивах!')
    print()
    print('________________________________________________________________________________________')
bank = Bank('Пегас банк', 'cor_account.txt')
bank.greetings()
customer = Customer()
choise = customer.status_select()
if choise == '1':
    print('Представьтесь, пожалуйста')
    customer.identification_client(customer.incoming_customer_data())
    # customer.incoming_customer_data()
    # customer.identification_client()
elif choise == '2':
    customer.get_data()
    customer.create_file()
if customer.customer_file:
    client = Client('Physical_persons/' + customer.person_file)
    main_menu()
