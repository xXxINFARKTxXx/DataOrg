import csv

from my_app.bin_files.binary_file import BinaryFile


class SerialBlockFile(BinaryFile):
    def __init__(self, filename, header_fmt, block_factor, rec_fmt: str = ""):
        super().__init__(filename, header_fmt, block_factor=block_factor, rec_fmt=rec_fmt)
        self.block_factor = block_factor

    # returns decoded record if exists else empty tuple
    def find_by_id(self, idx: int) -> tuple:
        self.restore_file()
        while not self.is_eof():
            recs = self.read_block()
            for rec in recs:
                if rec[0] == idx:
                    return rec
            self.next_block()
        return tuple()

    # returns amount of written records
    def add_new_record(self, rec: tuple) -> int:
        if self.find_by_id(rec[0]):
            return -1
        self.restore_file()
        while not self.is_eof():
            if self.insert_record(rec):
                return 1
            self.next_block()
        self.write_block([rec])
        return 1

    # returns amount of records printed
    def print_file(self, sep='\n') -> int:
        self.restore_file()
        recs_counter = 0
        while not self.is_eof():
            block = self.read_block()
            for rec in block:
                print(rec, end=sep)
            recs_counter += len(block)
            self.next_block()
        return recs_counter

    # returns amount of updated records
    def update_record(self, rec: tuple) -> int:
        pass

    # returns amount of updated records
    def delete_record_by_id(self, idx: int) -> int:
        pass

    # returns amount of loaded records
    def load_from_csv(self, filename: str) -> int:
        records = []
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)

            next(csv_reader, None)
            for row in csv_reader:
                if len(row):
                    records.append(tuple([int(row[0]), int(row[3]), row[1], row[2]]))
        counter = 0
        for rec in records:
            counter += self.add_new_record(rec)
        return counter
