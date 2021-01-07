def read(file="example.txt"):
    if file[len(file) - 4:5] == ".txt":
        with open(file, "r") as file:
            return file.read()
    else:
        with open(file + ".txt", "r") as file:
            return file.read()


def write(line, file="example.txt"):
    if file[len(file) - 4:len(file)] == ".txt":
        with open(file, "w+") as file:
            return file.write(line)
    else:
        with open(file + ".txt", "w+") as file:
            return file.write(line)
