#!/usr/bin/env python3

import bs4
import requests
import csv
import re

url = "https://price.ua/catc839t14/page{}.html?price[min]=10000&price[max]=20000"


def string_formate(value: str) -> str:
    return value.replace("\'", "").replace("\"", "").replace("\n", " ")


def write_products(response, writer) -> None:
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    laptop = soup.find_all(class_="product-block")

    for notebook in laptop:
        name = laptop.find(class_="model-name").text
        price = laptop.find(class_="price").text
        all_desc = laptop.find_all(class_='short-descr-line')
        desc = '\n'.join([desc.text.strip() for desc in all_desc])
        link = laptop.find(class_='btn')['href']
        if link[0] == '/':
            link = "https://price.ua" + link
        photo_link = notebook.find(class_='photo-wrap').find('img')['src']
        photo_link = f"https:{photo_link}"
        writer.writerow([string_formate(name),
                         string_formate(price),
                         string_formate(desc),
                         string_formate(link),
                         string_formate(photo_link)])


k = 1

with open("laptops.csv", 'w', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    while True:
        r = requests.get(url=url.format(i))
        page = int(re.search(r'page\d+', r.url).group(0).replace('page', '')) \
            if k != 1 else 1
        if k != page:
            break
        else:
            write_products(r, csv_writer)
            k += 1
