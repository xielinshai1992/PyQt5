# -*- coding: utf-8 -*-
import struct




class DAAFrame:
    header = 0x0000
    type = 0x00
    length = 0x00000000
    body = b''
    checksum = 0x0000

    def pack(self):
        buffer = struct.pack("=HBI%dsH" % len(self.body), self.header, self.type, self.length, self.body, self.checksum)
        return buffer

    def unpack(self, data):
        (self.header, self.type, self.length, self.body, self.checksum) = struct.unpack("=HBI%dsH" % (len(data) - 9), data)