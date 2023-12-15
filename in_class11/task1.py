import requests

#читаем весь каталог
BASE_URL = 'https://fakestoreapi.com'
response = requests.get(f'{BASE_URL}/products')
print(response.json())

#добавляем новый продукт :)
new_product = {
    'title': 'Potato',
    'price': 1000,
    'description': 'POTATO!!!!!!!!!',
    'image': 'https://primamediamts.servicecdn.ru/f/main/3949/3948745.jpg?965c5b5ad817924cb5f474590eca2d6d',
    'category': 'vegetables'
}
response = requests.post(f'{BASE_URL}/products', json=new_product)
print(response.json())

#удаляем продукт :(

response = requests.delete(f"{BASE_URL}/products/21")
print(response.json())