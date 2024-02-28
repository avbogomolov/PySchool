import requests
from getpass import getpass # Импортируем метод getpass из одноимённой библиотеки для ввода пароля доступа.
#
# def test(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         print("web is ok")
#         print(response)
#     elif response.status_code == 404:
#         print("web is not ok")



r = requests.get('https://ironchampion.ru')


print(r.text)
# test('https://ironchampion.ru', params=query)


