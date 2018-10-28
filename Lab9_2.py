#! /usr/bin/env/python 3
NUMBC = {
    0: "",1: "одна",2: "дві",3: "три",4: "чотири",5: "п\'ять",6: "шість",
    7: "сім",8: "вісім",9: "дев\'ять",10: "десять",11: "одинатцять",12: "дванадцять",13: "тринадцять",
    14: "чотирнадцять",15: "п\'ятнадцять",   16: "шістнацять",17: "сімнадцять",
    18: "вісімнадцять",19: "дев\'ятнадцять",20: "двадцять",30: "тридцять",40: "сорок",50: "п\'ятдесят",
    60: "шістдесят",70: "сімдесят",80: "вісімдесят",90: "дев\'яносто",100: "сто",
    200: "двісті",300: "триста",400: "чотириста",500: "п\'ятсот",600: "шістсот",
    700: "сімсот",800: "вісімсот",900: "дев\'ятсот",
}


def get_last_digit(n: int) -> int:
    return int(str(n)[-1])


def number_split(money: int) -> list:
    return [int(n) for n in str(money)]


def end_word(n: int, variants: list) -> str:
    not_in_range = n not in range(5, 21)
    if get_last_digit(n) == 1 and not_in_range:
        return variants[0]
    elif get_last_digit(n) in (2, 3, 4) and not_in_range:
        return variants[1]
    return variants[2]


def cent_output(cent: int) -> str:
    return "{} {}".format(cent, end_word(cent, ["копійка", "копійки", "копійок"]))

def mapped_numbers(money):
    numbers = number_split(money)
    numbers = [numbers[i] * (10 ** (len(numbers) - 1 - i)) for i in range(len(numbers))]
    for i in range(len(numbers) - 1):
        if numbers[i] == 10:
            numbers.insert(i, numbers.pop(i) + numbers.pop(i))
    return numbers


def cash_dict(money: int, end_values: list) -> tuple:
    numbers = mapped_numbers(money)
    cash = " ".join(map(lambda n: NUMBC[n], numbers)).strip()
    end = end_word(numbers[-1], end_values)
    return cash, end


def banknote_output(money: int) -> str:
    money = str(money)
    before_thousands = int("".join(reversed(money[-1:-4:-1])))
    (pronunciation_number, end_word_number) = cash_dict(before_thousands, ["гривнi","гривня", "гривень"])
    if len(money) <= 3:
        return "{} {}".format(pronunciation_number, end_word_number)
    else:
        thousands = int("".join(reversed(money[-4::-1])))
        (pronunciation_thousands, end_word_thousands) = cash_dict(thousands, ["тисяча", "тисячі", "тисяч"])
        if before_thousands != 0:
            return "{} {} {} {}".format(pronunciation_thousands, end_word_thousands,
                                        pronunciation_number, end_word_number)
        else:
            return "{} {}".format(pronunciation_thousands, end_word_thousands)


cash = input("Please put your money here:")
if cash.__contains__(","):
    split = cash.split(",")
else:
    split = cash.split(".")
before = int(split[0])
after= int(split[1])
print((banknote_output(before)).capitalize(),cent_output(after))