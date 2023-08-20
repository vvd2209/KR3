from datetime import datetime

class Operation:
    def __init__(self, date, description, operation_to, amount, currency, operation_from=None):
        self.operation_from = operation_from
        self.currency = currency
        self.amount = amount
        self.operation_to = operation_to
        self.description = description
        self.date = date

    def __repr__(self):
        return f'дата перевода - {self.date}\n' \
               f'описание перевода - {self.description}\n' \
               f'откуда перевод - {self.operation_from}\n' \
               f'куда перевод - {self.operation_to}\n' \
               f'сумма перевода - {self.amount}\n' \
               f'валюта перевода - {self.currency}\n'

    def formate_date(self):
        """
        Функция порматирования даты в формате ДД.ММ.ГГГГ
        :return: дата в формате ДД.ММ.ГГГГ
        """
        old_date = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        new_date = old_date.strftime('%d.%m.%Y')
        return new_date

    def mask_from(self):
        """
        Функция маскировки номера карты или счета отправителя
        :return: маскированный номер карты или счета отправителя
        """
        name = ''
        numbers = ''
        # цикл отделения карты или счета от номера
        if self.operation_from is not None:
            for letter in self.operation_from:
                if letter.isdigit():
                    numbers += letter
                elif letter.isalpha():
                    name += letter

            if len(numbers) == 16:
                return f'{name} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'
            elif len(numbers) > 16:
                return f'{name} **{numbers[-4:]}'
        else:
            return ''

    def mask_to(self):
        """
        Функция маскировки номера карты или счета получателя
        :return: маскированный номер карты или счета получателя
        """
        name = ''
        numbers = ''
        # цикл отделения карты или счета от номера
        for letter in self.operation_to:
            if letter.isdigit():
                numbers += letter
            elif letter.isalpha():
                name += letter

        if len(numbers) == 16:
            return f'{name} {numbers[0:4]} {numbers[4:6]}** **** {numbers[-4:]}'
        elif len(numbers) > 16:
            return f'{name} **{numbers[-4:]}'