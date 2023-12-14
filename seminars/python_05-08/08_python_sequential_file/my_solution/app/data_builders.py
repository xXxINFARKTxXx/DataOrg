import struct


class RecordBuilder:

    def __init__(self, fmt: str = "64s", encoding: str = 'ascii'):
        self.fmt = fmt
        self.fmt_size = struct.calcsize(self.fmt)
        self.encoding = encoding

    def with_fmt(self, fmt: str) -> 'RecordBuilder':
        self.fmt = fmt
        return self

    def with_encoding(self, encoding: str) -> 'RecordBuilder':
        self.encoding = encoding
        return self

    def get_fmt_size(self) -> int:
        return struct.calcsize(self.fmt)

    def build_to_bytes(self, rec: tuple) -> bytes:
        rec = tuple([v.encode(encoding=self.encoding) if isinstance(v, str) else v for v in rec])
        return struct.pack(self.fmt, *rec)

    def build_from_bytes(self, buff: bytes) -> tuple:
        rec = struct.unpack(self.fmt, buff)
        return tuple([v.decode(encoding=self.encoding) if isinstance(v, bytes) else v for v in rec])


class BlockBuilder:

    def __init__(self, block_factor: int = 1, rec_builder: RecordBuilder = None):
        self.block_factor = block_factor
        self.rec_builder = RecordBuilder() if rec_builder is None else rec_builder

    def with_block_factor(self, block_factor: int) -> 'BlockBuilder':
        self.block_factor = block_factor
        return self

    def with_rec_builder(self, rec_builder: RecordBuilder) -> 'BlockBuilder':
        self.rec_builder = rec_builder
        return self

    def get_block_size(self) -> int:
        return self.rec_builder.get_fmt_size() * self.block_factor

    def to_bytes(self, block: list[tuple]) -> bytes:
        enc_data = bytearray()
        for rec in block:
            enc_data += self.rec_builder.build_to_bytes(rec)
        return bytes(enc_data)

    def from_bytes(self, data: bytes) -> list[tuple]:
        enc_data = bytearray(data)

        dec_data: list[tuple] = []
        rec_size = self.rec_builder.get_fmt_size()

        for i in range(self.block_factor):
            enc_rec = enc_data[i * rec_size:(i + 1) * rec_size]
            dec_rec = self.rec_builder.build_from_bytes(enc_rec)
            dec_data.append(dec_rec)
        return dec_data
