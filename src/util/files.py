def file(file_name):
    with open(file_name) as _file:
        pass


def read(fname="example.txt"):
    if fname[len(fname) - 4:len(fname) - 1] == ".txt":
        print(f"fname: {fname}")
        with open(fname, "r") as fname:
            return fname.read()
    else:
        with open(fname + ".txt", "r") as fname:
            return fname.read()


def write(line, fname="example.txt"):
    if fname[len(fname) - 4:len(fname) - 1] == ".txt":
        with open(fname, "w+") as fname:
            return fname.write(line)
    else:
        with open(fname + ".txt", "w+") as fname:
            return fname.write(line)
