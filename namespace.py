
calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(text: str):
    count_calls()
    string_ = []
    x1 = len(text)
    x2 = text.upper()
    x3 = text.lower()
    string_.append(x1)
    string_.append(x2)
    string_.append(x3)
    x4 = tuple(string_)
    return x4

def is_contains(text_2: str, list_: list):
    result = 0
    count_calls()
    list_lower_set = {every.lower() for every in list_}
    if text_2.lower() in list_lower_set:
        result = True
    else:
        result = False
    return result

text = input('Введите текст: ')
print(string_info(text))
print()

text_2 = input('Введите текст 2: ')
list_ = input('Введите список сравнения, разделяя пробелом:').split()
print(is_contains(text_2, list_))
print()

print(calls)
