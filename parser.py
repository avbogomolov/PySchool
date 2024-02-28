import requests


def test(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("web is ok")
    elif response.status_code == 404:
        print("web is not ok")



test('https://ironchampion.ru')

