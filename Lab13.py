#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    @abstractmethod
    def get_salary(self) -> float:
        pass

    @abstractmethod
    def pay_tax(self) -> float:
        pass



class EmployeeData:
    def __init__(self, employee_id: int, name: str, surname: str) :
        super().__init__()
        (self.employee_id, self.name, self.surname) = (employee_id, name, surname)


class SimpleEmployee(AbstractEmployee):
    def __init__(self, data: EmployeeData, unit_salary: float, unit_work: float) :
        super().__init__()
        self.unit_salary = unit_salary
        self.data = data
        self.unit_work = unit_work

    def get_salary(self) -> float:
        return self.unit_work * self.unit_salary

    def pay_tax(self) -> float:
        salary = self.get_salary()
        return salary * 0.18 + salary * 0.015

    def __str__(self) -> str:
        return f'{type(self).__name__}[id={self.data.employee_id}, name=`{self.data.name}`, ' \
               f'salary={self.get_salary()}, tax={self.pay_tax()}]'


class FixedSalaryEmployee(SimpleEmployee):
    def __init__(self, data: EmployeeData, month_salary: float) :
        super().__init__(data, unit_salary=month_salary, unit_work=1)


class HourlySalaryEmployee(SimpleEmployee):
    def __init__(self, data: EmployeeData, hourly_rate: float, hours: float) :
        super().__init__(data, unit_salary=hourly_rate, unit_work=hours)

class FOP(HourlySalaryEmployee):
    def get_salary(self) -> float:
        return super().get_salary() * 1.1

    def pay_tax(self) -> float:
        return self.get_salary() * 0.05 + 704



class RowsNumberSalaryEmployee(SimpleEmployee):
    def __init__(self, data: EmployeeData, row_price: float, rows_number: float) :
        super().__init__(data, unit_salary=row_price, unit_work=rows_number)

    def pay_tax(self) -> float:
        return super().pay_tax() + 704


employees: list = [
    FixedSalaryEmployee(EmployeeData(1, 'serhiy', '123'), month_salary=4280.0),
    HourlySalaryEmployee(EmployeeData(2, 'dmitro', '221'), hourly_rate=204.0, hours=40.0),
    FOP(EmployeeData(3, 'sash', '325'), hourly_rate=90.0, hours=40.0),
    FOP(EmployeeData(4, 'ivan', '328'), hourly_rate=51.0, hours=80.0),
    RowsNumberSalaryEmployee(EmployeeData(5, 'denis', '312'), row_price=6.5, rows_number=20)
]

for e in employees:
    print(e)

employees.sort(key=lambda employee: (employee.get_salary(), employee.data.surname), reverse=True)
print()
for e in employees:
    print(e)