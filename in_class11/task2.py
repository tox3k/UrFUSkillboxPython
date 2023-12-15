import requests

BASE_URL = 'https://fakestoreapi.com'
result = []
response = requests.get(f'{BASE_URL}/products')
# Все продукты с ценой ниже 20
response_json = response.json()
for i in response_json:
    if i['price'] < 20:
        result.append(i)
print('Продукты с ценой ниже 20:')
print('\n'.join(str(i) for i in result), '\n')

#Все категории товаров
categories = set()
for i in response_json:
    categories.add(i['category'])
print('Все категории товаров:')
print('\n'.join(list(categories)), '\n')

#Все продукты категории jewelery
jewelery_prod = []
for i in response_json:
    if i['category'] == 'jewelery':
        jewelery_prod.append(i)
print('Все товары категории jewelery:')
print('\n'.join(str(i) for i in jewelery_prod), '\n')

#Все пользователи
users_response = requests.get(f'{BASE_URL}/users') #Че за позор, кто вообще хранит в исходном виде пароли пользователей :/
print('Все пользователи:')
print('\n'.join(str(i) for i in users_response.json()), '\n')

#Добавляем пользователя (данные украл из документации с сайта fakestoreapi :) )
new_user = {
    'email':'John@gmail.com',
    'username':'johnd',
    'password':'m38rmF$',
    'name':{
        'firstname':'Андрей',
        'lastname':'Колчин'
    },
    'address':{
        'city':'kilcoole',
        'street':'7835 new road',
        'number':3,
        'zipcode':'12926-3874',
        'geolocation':{
            'lat':'-37.3159',
            'long':'81.1496'
                }
            },
    'phone':'1-570-236-7033'
}
add_new_user_response = requests.post(f'{BASE_URL}/users', json=new_user)
print('Добавлен новый пользователь:')
print(add_new_user_response.json())