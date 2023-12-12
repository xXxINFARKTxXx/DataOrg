def read_by_chars(file_name : str):
    with open(file_name) as file:
        while True:
            char =  file.read(1)
            if not char:
                break
            print(char, end='', sep='')
    pass