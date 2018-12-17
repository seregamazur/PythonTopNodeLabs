
import requests
import bs4
import csv


# link to scrap: https://price.ua/catc839t14.html?price[min]=10000&price[max]=20000


def write_page_to_html(content):
    with open('index.html', 'w') as file:
        file.write(content)


def get_laptops_list(response) -> list:
    soup = bs4.BeautifulSoup(response.content, "html.parser")
    return soup.find_all(class_='product-block')


def get_laptop_name(laptop) -> str:
    return laptop.find(class_='model-name').text


def get_laptop_price(laptop) -> str:
    return laptop.find(class_='price').text


def get_laptop_short_desc(laptop) -> str:
    all_desc = laptop.find_all(class_='short-descr-line')
    return '\n'.join([desc.text.strip() for desc in all_desc])


def get_laptop_link(laptop) -> str:
    href = laptop.find(class_='btn')['href']
    if href[0] == '/':
        href = "https://price.ua" + href
    return href


def get_laptop_photo_link(laptop) -> str:
    return f"https:{laptop.find(class_='photo-wrap').find('img')['src']}"


def main():
    url = "https://price.ua/catc839t14/page{}.html?price[min]=10000&price[max]=20000"
    with open("laptops.csv", 'w') as file:
        laptops_writer = csv.writer(file)
        laptops_writer.writerow(['name', 'price', 'description', 'link', 'photo link'])
        for i in range(1, 60):
            content = get_laptops_list(requests.get(url=url.format(i)))
            for laptop in content:
                laptops_writer.writerow([get_laptop_name(laptop),
                                         get_laptop_price(laptop),
                                         get_laptop_short_desc(laptop),
                                         get_laptop_link(laptop),
                                         get_laptop_photo_link(laptop)])
    # TODO: make loop util pages ends
    # print(content)
    # print(get_laptop_photo_link(content))


if __name__ == '__main__':
    main()