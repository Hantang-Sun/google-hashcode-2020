from IO import *
from Assess import *
from Eval import *

file1 = "a_example.txt"
file2 = "b_read_on.txt"
file3 = "c_incunabula.txt"
file4 = "d_tough_choices.txt"
file5 = "e_so_many_books.txt"
file6 = "f_libraries_of_the_world.txt"

files = [file1, file2, file3, file4, file5, file6]

debug = True
score = 0

for file in files:
    libs_data = get_data("../tests/"+ file)
    libs = choose(libs_data.days, libs_data.libs, libs_data.books)
    books = select_all(libs, libs_data.days)
    filename = file.split(".")[0]
    write_result_file("../outputs/"+filename+"result.txt", books)
    if debug:
        s = sum([sum([libs_data.books[b] for b in i[1]]) for i in books])
        print("File " + file + " has score: " + str(s))
        score += s

if debug:
    print("total: " + str(score))
