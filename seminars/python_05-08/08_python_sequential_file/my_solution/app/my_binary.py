import os  # os.SEEK_SET os.SEEK_CUR os.SEEK_END
from typing import BinaryIO

from app.data_builders import BlockBuilder, RecordBuilder


class MyBinary:
    def __init__(self, file: BinaryIO, encoding: str = 'ascii', fmt: str = '64s', block_factor: int = 1):
        self.file: BinaryIO = file
        rbuilder = RecordBuilder().with_fmt(fmt).with_fmt(fmt).with_encoding(encoding)
        self.bbuilder: BlockBuilder = BlockBuilder().with_block_factor(block_factor).with_rec_builder(rbuilder)

    def write_block(self, block) -> None:
        self.file.write(self.bbuilder.to_bytes(block))

    def read_block(self) -> list[tuple]:
        encoded = self.file.read(self.bbuilder.get_block_size())
        return self.bbuilder.from_bytes(encoded)

    def init_file(self) -> None:
        encoded = bytes(bytearray([0] * self.bbuilder.get_block_size()))
        self.file.write(encoded)

    def next_block(self, backwards=False) -> int:
        self.file.seek((-2 * int(backwards) + 1) * self.bbuilder.get_block_size(), os.SEEK_CUR)
        return self.file.tell()

    def restore(self):
        self.file.seek(0, os.SEEK_SET)
        return self.file.tell()

    def is_eof(self) -> bool:
        curr_pos = self.file.tell()
        self.file.seek(0, os.SEEK_END)
        end_pos = self.file.tell()
        self.file.seek(curr_pos, os.SEEK_SET)
        return end_pos <= curr_pos
