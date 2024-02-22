import requests


def test(url):
    response = str(requests.get(url))
    a = '<Response [200]>'
    if response == a:
        print(f'ответ от сервера: 200')
    else:
        print("Не верный ответ")


test('https://ironchampion.ru')