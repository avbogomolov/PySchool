import requests


def test(url):
    response = requests.get(url)
    print(response.text)



#test('https://ironchampion.ru')
test('https://cdek.shopping/p/215425/nastolnyi-kompyuter-apple-mac-mini-m2-2023-8gb256gb-silver')

