#! /usr/bin/env python3

def camelMethod(word: str) -> str:
    split = word.split('_')
    return split[0] + ''.join(map(lambda s: str(s).capitalize(), split[1:]))


def snake_method(text: str) -> str:
    under_words: [str] = list(filter(lambda s: '_' in s, text.split()))
    camel_words: [str] = list(map(lambda word: camelMethod(word), under_words))
    for under, camel in zip(under_words, camel_words):
        text = text.replace(under, camel)
    return text
line = "print([res_square ** 2 for res_square in input_array if res_square > 18 ])"
print(camelMethod(line))
