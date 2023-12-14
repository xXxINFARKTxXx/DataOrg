import csv
import os
import struct
from typing import BinaryIO


class SequentialFile():
    def __init__(
            self,
            filename,
            blocking_factor,
            encoding,
            fmt: str
    ):

        self.filename = filename
        self.blocking_factor = blocking_factor
        self.encoding = encoding
        self.fmt = format

        self.file: BinaryIO = None

        try:
            self.rec_size = struct.calcsize(self.fmt)
        except Exception as e:
            raise ValueError("Invalid format") from e

        try:
            self.file = open(filename, mode='rb+')
        except Exception as e:
            self.file = open(filename, mode='wb+')
            self.init_file()
        except Exception as e:
            raise IOError(f"Could not open or create file: {e.args}")

    def init_file(self):
        empt_block = bytes([0] * ((self.rec_size) * self.block_size))
        self.file.write(empt_block)

    def load_from_csv(self, csv_file: str):
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                rec = Record(row, coding='ascii', format=self.fmt)
                print(Record)

    def find_record_by_key(self, key: int) -> tuple:
        self._restore()
        while not self._eof():
            block = self.read_block(self.file)
            if block:
                for i in block:
                    if block[0] == key:
                        return i
        return tuple()

    def add_record(self, record):
        pass

    def delete_record_by_key(self, key):
        pass

    def update_record(self, record, key: int) -> None:
        self._restore()
        block = self.read_block(self.file)
        pass

    def reorg_file(self):
        pass

    def _restore(self):
        self.file.seek(0, os.SEEK_SET)

    def _next_block(self, backwards=False):
        self.file.seek((int(backwards) * (-2) + 1) * self.blocking_factor, os.SEEK_CUR)

    def _is_block_empty(self, ):
        pass

    def _eof(self):
        curr_pos = self.file.tell()
        self.file.seek(0, os.SEEK_END)
        end_pos = self.file.tell()
        self.file.seek(curr_pos, os.SEEK_SET)
        return end_pos <= curr_pos

    def write_block(self, file: BinaryIO, block: List[Dict]):
        binary_data = bytearray()

        for rec in block:
            rec_binary_data = self.record.dict_to_encoded_values(rec)
            binary_data.extend(rec_binary_data)

        file.write(binary_data)

    def read_block(self, file: BinaryIO):
        binary_data = file.read(self.block_size)
        block = []

        if len(binary_data) == 0:
            return block

        for i in range(self.blocking_factor):
            begin = self.record_size * i
            end = self.record_size * (i + 1)
            block.append(self.record.encoded_tuple_to_dict(binary_data[begin:end]))

        return block
    def __del__(self):
        if self.file is not None and not self.file.closed:
            self.file.close()
