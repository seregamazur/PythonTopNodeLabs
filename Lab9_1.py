#! /usr/bin/env/python 3
from functools import reduce


def get_points(cards_on_hand: list, combinations: dict) -> int:
    return reduce(lambda x, y: x + y, map(lambda n: combinations[n], cards_on_hand))


def get_combinations() -> dict:
    simple_cards = {}
    for i in range(1, 10):
        simple_cards[str(i)] = i
    figure_cards = dict.fromkeys(["T", "J", "Q", "K"], 10)
    all_cards = {**simple_cards, **figure_cards, **{"A": 11}}
    return all_cards


user_cards = input("Please input your cards:")
cards = user_cards.split()
combinations = get_combinations()
points = get_points(cards, combinations)
if points > 21:
    combinations['A'] = 1
    points = get_points(cards, combinations)
    if points > 21:
        result = "Bust"
print(result)
