def file(file_name, text, access_type="r"):
    with open(file_name, access_type) as _file:
        if access_type == "r":
            return read(file_name)
        elif access_type == "w+":
            return write(text, file_name)


def read(fname="example.txt"):
    if fname[len(fname) - 4:len(fname) - 5] == ".txt":
        print(f"fname: {fname}")
        with open(fname, "r") as fname:
            return fname.read()
    else:
        with open(fname + ".txt", "r") as fname:
            return fname.read()


def write(line, fname="example.txt"):
    if fname[len(fname) - 4:len(fname) - 5] == ".txt":
        with open(fname, "w+") as fname:
            return fname.write(line)
    else:
        with open(fname + ".txt", "w+") as fname:
            return fname.write(line)


def resolve_filename(file):
    if {file[len(file) - 4:file[len(file -5)]]}:
        pass


