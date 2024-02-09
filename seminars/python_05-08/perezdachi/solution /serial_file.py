import os
from typing import Dict, BinaryIO, List

from binary_file import BinaryFile
from constants import *


class SerialFile(BinaryFile):
    def __init__(self, filename, record, blocking_factor, empty_key=-1):
        BinaryFile.__init__(self, filename, record, blocking_factor, EMPTY_RECORD, empty_key)

    def _eof(self, file: BinaryIO) -> bool:
        curr_pos = file.tell()
        file.seek(0, os.SEEK_END)
        end_file = file.tell()
        file.seek(curr_pos, os.SEEK_SET)
        return curr_pos >= end_file

    def _find_by_id(self, idx: int, file: BinaryIO) -> [List[Dict], int]:
        while not self._eof(file):
            block = self.read_block(file)
            for i in range(len(block)):
                if block[i]["id"] == idx and block[i]["status"]:
                    return [block, i]
        return [None, -1]

    def init_file(self) -> None:
        with open(self.filename, "wb") as f:
            self.write_block(f, self.blocking_factor * [self.empty_record])

    def find_by_id(self, idx) -> Dict:
        if idx <= -1:
            raise Exception(WRONG_INPUT_EXCEPTION)
        with open(self.filename, "rb") as f:
            return self._find_by_id(idx, f)[0]

    def print_file(self) -> None:
        with open(self.filename, "rb") as f:
            while not self._eof(f):
                for record in self.read_block(f):
                    print(record)

    def add_record(self, new_rec: Dict) -> bool:
        if self.find_by_id(new_rec["id"]) is not None:
            return False

        new_rec["status"] = 1
        with open(self.filename, "rb+") as f:
            while not self._eof(f):
                block = self.read_block(f)

                # check if block has empty space
                for i in range(len(block)):
                    if block[i]["status"] == 0:
                        block[i] = new_rec
                        f.seek(-self.block_size, os.SEEK_CUR)
                        self.write_block(f, block)
                        return True

            # if all block spaces are not empty
            f.seek(0, os.SEEK_END)
            block = [self.empty_record] * self.blocking_factor
            block[0] = new_rec
            self.write_block(f, block)
            return True

    def delete_record(self, idx) -> bool:
        if idx <= -1:
            raise Exception(WRONG_INPUT_EXCEPTION)

        with open(self.filename, "rb+") as f:
            # find record
            block, index = self._find_by_id(idx, f)
            if index == -1:
                return False

            # delete record from block
            block[index] = self.empty_record

            # check if block is not empty
            for record in block:
                if record["status"] != 0:
                    # if it is not, then write
                    f.seek(-self.block_size, os.SEEK_CUR)
                    self.write_block(f, block)
                    return True

            # else if it is empty and at the end of file, then truncate
            if self._eof(f):
                f.seek(-self.block_size, os.SEEK_CUR)
                f.truncate()
            # else write
            else:
                f.seek(-self.block_size, os.SEEK_CUR)
                self.write_block(f, block)

            return True
