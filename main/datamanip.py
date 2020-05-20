def print_to_file(filename, string):
    fout = open(filename, "w+")
    fout.write(string)
    fout.close()

def read_and_extract_information(filename):
    fin = open(filename)
    inf = fin.readlines()
    fin.close()
    return inf
