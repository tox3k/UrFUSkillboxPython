import re
import doctest

def check_password(password):
    """Проверяет пароль на соответствие заданным требованиям

    :param password: пароль-строка
    :return:
    >>> check_password(r'rtG&3FG#Tr^e')
    'Good password!'
    >>> check_password(r'a^A1@*@1Aa')
    'Good password!'
    >>> check_password(r'oF^a1D@y5%e6')
    'Good password!'
    >>> check_password(r'enroi#$*rkdeR#$*092uwedchf34tguv394h')
    'Good password!'

    >>> check_password(r'пароль')
    'Bad password!'
    >>> check_password(r'password')
    'Bad password!'
    >>> check_password(r'qwerty')
    'Bad password!'
    >>> check_password(r'lOngPa$$W0Rd')
    'Bad password!'
    """
    match = re.fullmatch(r'(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9])([^,\.!?\s]){8,}', password)
    if match and len(set(re.findall(r'[\^$%@#&*]', password))) > 2:
        return 'Good password!'
    return 'Bad password!'
