import requests


def gen_for_urls(urls: tuple) -> tuple:
    for resp in (requests.get(i) for i in urls):
        yield len(resp.content), resp.status_code, resp.url


urls = ('https://yandex.ru/', 'https://google.com/', 'https://epam.com/')

for r_len, status_code, url in gen_for_urls(urls):
    print(r_len, '->', status_code, '->', url)
