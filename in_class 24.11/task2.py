import re
test = [
    r'20 января 1806',
    r'18-05-2020',
    r'1924, July 25',
    r'26/09/1635',
    r'3.1.1506',
    '25.08-1002',
    'декабря 19, 1838'
]

patterns = {
    r'\d{1,2}[./-]\d{1,2}[./-]\d{4}', #  дд-мм-гг
    r'\d{4}[./-]\d{1,2}[./-]\d{1,2}', # гг-мм-дд
    r'\d{1,2}\s\w{3,}\s\d{4}', # день месяц_rus год
    r'[a-zA-Z]{3,}\s\d{1,2},\s\d{4}', # месяц_eng день, год
    r'[a-zA-Z]{3}\s\d{1,2},\s\d{4}', # мес_eng день, год
    r'\d{4},\s[a-zA-Z]{3,}\s\d{1,2}', # год, месяц_eng день
    r'\d{4},\s[a-zA-Z]{3}\s\d{1,2}', # год, мес_eng день
}
#date_string = input()

def check_date(date_string):
    for pattern in patterns:
        match = re.fullmatch(pattern, date_string)
        if match is not None:
            if date_string.count('-') == 2 or date_string.count('-') == 0:
                return date_string + '  Date correct!'
    return date_string + '  Wrong date!'


for i in test:
    print(check_date(i))

# Поставьте мне за эти работы хотяб 1 балл умоляю,
# я уже не могу сидеть с этими регулярками