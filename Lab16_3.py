#!/usr/bin/env python3

import csv
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup


class School:
    def __init__(self, name: str, phone: str, email: str, director_name: str,
                 students_number: str, link: str) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.director_name = director_name
        self.students_number = students_number
        self.link = link


def string_formate(value: str) -> str:
    return value.replace("\'", '').replace("\"", '').replace("\n", ' ')


def cast_tuple(tr):
    return tr.select_one('th'), tr.select_one('td')


def table_tuple_text(x) -> tuple:
    if x[0] and x[1]:
        key = ' '.join(x[0].text.split())
        raw_value = ' '.join(x[1].text.split())
        value = raw_value if raw_value else '-'
        if key == 'E-mail:' and value != '-':
            value = re.findall("'<a.*>(.*)</a>'",
                               urllib.parse.unquote(x[1].select_one('a')['onclick']))[0]
        return_tuple = (key, value)
    else:
        return_tuple = None
    return return_tuple


class Scrapper:
    def __init__(self, base_url, query) -> None:
        self.base_url = base_url
        self.soup = BeautifulSoup(requests.get(base_url + query).content,
                                  'html.parser')

    def set_link(self, link):
        self.soup = BeautifulSoup(requests.get(link).content, 'html.parser')

    def table_dict(self):
        return dict(
            filter(lambda t: t is not None,
                   map(table_tuple_text,
                       map(cast_tuple, self.soup.select('table > tr'))))
        )

    def get_update_link(self, a):
        link = self.base_url + a['href']
        self.set_link(link)
        return link

    def get_link(self):
        return self.soup.select('table > tr > td > a')

    def get_schools(self) -> list:
        schools = []
        for a in self.get_link():
            link = self.get_update_link(a)
            table_dict = self.table_dict()
            school = School(string_formate(table_dict['Name:']),
                            string_formate(table_dict['Telephone:']),
                            string_formate(table_dict['E-mail:']),
                            string_formate(table_dict['Head:']),
                            string_formate(table_dict['Pupil count:']),
                            string_formate(link))
            schools.append(school)
        return schools


def main():
    url = "https://if.isuo.org/"
    school_id = "authorities/schools-list/id/620"
    schools = Scrapper(url, school_id).get_schools()
    with open("School_list.csv", 'w', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        for school in schools:
            csv_writer.writerow([
                school.name,
                school.phone,
                school.email,
                school.director_name,
                school.students_number,
                school.link
            ])


if __name__ == '__main__':
    main()
