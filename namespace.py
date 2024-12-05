
def is_contains(word: str, list_: list):
    list_lower_set = {every.lower() for every in list_}
    if word.lower() in list_lower_set:
        print('True')
    elif word.lower() not in list_lower_set:
        print('False')
    return True

word = input('Введите слово: ')
list_ = input('Введите список слов, разделяя пробелом: ').split()
is_contains(word, list_)