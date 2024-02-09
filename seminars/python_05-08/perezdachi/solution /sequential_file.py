import os
from typing import BinaryIO, List, Dict

from binary_file import BinaryFile
from constants import *


class SequentialFile(BinaryFile):
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
            block = self.blocking_factor * [self.empty_record]
            self.write_block(f, block)

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
        block = [new_rec]
        with open(self.filename, "rb+") as f:
            while not self._eof(f):
                block = sorted([elem for elem in self.read_block(f) + block if elem["id"] >= 0], key=lambda k: k["id"])
                f.seek(-self.block_size, os.SEEK_CUR)
                if len(block) < self.blocking_factor: break
                self.write_block(f, block[:self.blocking_factor])
                block = block[self.blocking_factor:]
            for i in range(self.blocking_factor - len(block)): block.append(self.empty_record)
            if block[0]["status"] != 0: self.write_block(f, block)
            return True

    def delete_by_id(self, idx):
        with open(self.filename, mode="rb+") as f:
            [block, index] = self._find_by_id(idx, f)
            if block is None: return False
            block.pop(index)
            while not self._eof(f):
                block += self.read_block(f)
                f.seek(-self.block_size, os.SEEK_CUR)
                self.write_block(f, block[:self.blocking_factor])
                block = block[self.blocking_factor:]
            for i in range(self.blocking_factor - len(block)): block.append(self.empty_record)
            if block[0]["status"] != 0: self.write_block(f, block)
