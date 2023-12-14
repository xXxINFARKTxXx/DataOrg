import csv

from my_app.bin_files.serial_block_file import SerialBlockFile


def read_csv(file_path):
    records = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        # Пропустим заголовок, если он есть
        next(csv_reader, None)
        for row in csv_reader:
            if len(row) == 4:
                records.append(tuple([int(row[0]), row[1], row[2], int(row[3])]))
    return records


if __name__ == '__main__':
    filename = "data/data.myDBF"
    csv_file = "data/data.csv"
    header_fmt = "i28s"
    rec_fmt = "ii12s11s"
    records: list[tuple] = read_csv(csv_file)
    dbf_file = SerialBlockFile(filename, header_fmt=header_fmt, block_factor=3, rec_fmt=rec_fmt)
    print(dbf_file.load_from_csv(csv_file))
    dbf_file.print_file()
