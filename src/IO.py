def readf(file):
    f = open(file, "r")
    all_line = f.readlines()
    return [l.split() for l in all_line]


def writef(dest, output):
    f = open(dest, "w")
    for l in output:
        f.write(" ".join(l))


def get_data(file):
    lines = readf(file)
    no_of_books = int(lines[0][0])
    no_of_libs = int(lines[0][1])
    days = int(lines[0][2])
    pts = list(map(int, lines[1]))
    all_data = Data(no_of_books, no_of_libs, days, pts, [])
    for i in range(2, len(lines) - 1, 2):
        lib_info = lines[i]
        book_list = list(map(int, lines[i + 1]))
        book_list = sorted(book_list, key=lambda x: -pts[x])
        temp_lib = Library(i // 2 - 1, int(lib_info[0]), int(lib_info[1]), int(lib_info[2]), book_list)
        all_data.add_lib(temp_lib)
    return all_data


def write_result_file(file, result: [(int, [int])]):
    output = str(len(result)) + "\n"
    for lib in result:
        output += str(lib[0]) + " " + str(len(lib[1])) + "\n"
        books_str = list(map(str, lib[1]))
        output += " ".join(books_str) + "\n"
    writef(file, output)
    print("File " + file + " created successfully!")


class Library:
    def __init__(self, id, no_of_books, signup_time, books_per_day, books):
        self.books = books
        self.books_per_day = books_per_day
        self.signup_time = signup_time
        self.id = id
        self.no_of_books = no_of_books

    def print_lib_info(self):
        print("Library ID: " + str(self.id))
        print("Number of books: " + str(self.no_of_books))
        print("Signup time: " + str(self.signup_time) + " days")
        print("Can ship " + str(self.books_per_day) + " per day")
        print("Books: " + str(self.books) + "\n")


class Data:
    def __init__(self, no_of_books, no_of_libs, days, books, libs):
        self.books = books
        self.libs = libs
        self.days = days
        self.no_of_libs = no_of_libs
        self.no_of_books = no_of_books

    def add_lib(self, new_lib):
        self.libs.append(new_lib)

    def print_data(self):
        print("Total number of books:" + str(self.no_of_books))
        print("Number of libraries: " + str(self.no_of_libs))
        print("Days: " + str(self.days))
        print("Scores of the books: " + str(self.books))
        for lib in self.libs:
            lib.print_lib_info()
