import json
from operator import itemgetter
from class_operation import Operation

def load_json(file_name):
    """
    Функция получаения данных об операциях из файла
    """
    with open(file_name, encoding='utf-8') as file:
        dict_json = json.load(file)

    new_dict = []
    for dict in dict_json:
        if dict:
            new_dict.append(dict)

    return new_dict


def get_list_executed(operation_list):
    """
    Функция, которая получает 5 последних отфильтрованных по статусу EXECUTED выполненных операций
    :return: последние 5 выполненных операций
    """
    # фильтрация операций по статусу "EXECUTED"
    executed_list = []
    for operation in operation_list:
        if operation['state'] == "EXECUTED":
            executed_list.append(operation)

    # сортировка операций по дате
    newlist = sorted(executed_list, key=itemgetter('date'), reverse=True)

    return newlist[0: 5]


def get_list_class(executed_list):
    """
    Функция создания массива экземпляров класса
    :return: массив экземпляров класса
    """

    # пустой список для массива экземпляров класса
    operations = []
    for operation in executed_list:
        if 'from' in operation.keys():
            date = operation['date']
            description = operation['description']
            operation_to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']
            operation_from = operation['from']
            operations.append(Operation(date, description, operation_to, amount, currency, operation_from))
        else:
            date = operation['date']
            description = operation['description']
            operation_to = operation['to']
            amount = operation['operationAmount']['amount']
            currency = operation['operationAmount']['currency']['name']
            operations.append(Operation(date, description, operation_to, amount, currency))
    return operations