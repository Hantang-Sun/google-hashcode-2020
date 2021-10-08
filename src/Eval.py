from IO import *

def select_all(libs: [Library], total_days: int):
    x = 0
    list_list = []
    for lib in libs:
        x += lib.signup_time
        list_list.append(select_books(lib, total_days - x))
    return list_list


def rate_lib(library: Library, pts: [int]):
    expectation = 0
    exp_sqr = 0
    acc = 0
    length = len(library.books)
    for i in range(0, length, max(1, length // 500)):
        p = pts[library.books[i]]
        expectation += p
        exp_sqr += p ** 2
        acc += 1
    expectation //= acc
    variance = exp_sqr - expectation ** 2
    return variance + expectation


def select_books(library: Library, days_to_ship: int):
    return library.id, library.books[:days_to_ship * library.books_per_day]


