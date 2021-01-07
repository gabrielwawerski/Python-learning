# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def test():
    """pass"""
    width = 20
    height = 2 * 2

    width * height


def get_input(prompt="> "):
    return input(prompt)


def get_and_print_user_text():
    print(get_input())


def _c_to_kelvin(value):
    zero = 273.15
    return format(float(zero + value), '.2f') if value > 0 else format(float(zero - (-value)), '.2f')


def c_to_kelvin(value):
    pass


from util import files
# thanks to this, file is executable (i think) or usable/exportable as a module
if __name__ == '__main__':
    gabe = "lul"
    from src.scripts import board_calculator as board

    #board.calc_print_user_board()
    a_file = files.read("koszerny")
    files.write("Ha! Nowa linia!\n" * 1, "koszerny")
    # print_hi('Gabe')
    # print(input("fuck: "))
    # x = get_input()
    # print(x)
    # get_and_print_user_text()

    # user_input = get_input("Celsius to Kelvin\ntemp in c: ")
    # print(_c_to_kelvin(int(user_input)))
    #
    # while user_input != "q":
    #     user_input = get_input()
    #     print(_c_to_kelvin(int(user_input)))


def menu():
    user_input = input("1. Write\n2.Read\nx. exit> ")

    # write to file
    if user_input == "1":
        print(get_input())
        print(files.read("../koszerny.txt"))
    # read file
    elif user_input == "2":
        file_name = input("file name: ")
        files.read(file_name)
    # exit
    elif user_input == "x":
        import sys
        sys.exit()

# print(files.file_read("koszerny"))


class File:
    def __set__(self, instance, value):
        pass
