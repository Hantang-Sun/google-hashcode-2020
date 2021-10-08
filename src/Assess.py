import random
import IO

sample_size = 30
library_sample_size = 100
magic = 10

def assess_library(days,no_of_books, books_per_day, signup_time,books,bookmaps):
    s = 0
    #if (signup_time < days // 2):
    div = (books_per_day * days / no_of_books)

    n = min(no_of_books,books_per_day * days) 

    for i in range (n):
        s += bookmaps[books[i]]

    score = s / signup_time 

    return score/ div
    #return 0

def choose(days,libs,bookmaps):
    select = []
    library_sample_size = min(len(libs),999999)
    while days >= min([l.signup_time for l in libs]):
        max_i = 0
        maxscore = 0
        for i in range (0,library_sample_size):
            index = i % len(libs)
            li =libs[index]
            if li.signup_time <= days:
                score = assess_library(days,li.no_of_books, li.books_per_day,li.signup_time, li.books,bookmaps)
                if score > maxscore:
                    maxscore = score
                    max_i = index
        select.append(libs[max_i])
        days -= libs[max_i].signup_time
        libs.remove(libs[max_i])
        if libs == []:
            break
    return select
