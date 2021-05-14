from check_sum import checksum

class DataParser:
    dataPool: bytes = b''

    def accept(self, data: bytes):
        self.dataPool += data
        lower_bound = self.dataPool.find(0x4f3c.to_bytes(length=2, byteorder='big', signed=False))
        if lower_bound < 0:
            return
        self.dataPool = self.dataPool[lower_bound:]
        if len(self.dataPool) < 9:
            return
        frame_type = int.from_bytes(self.dataPool[2:3], byteorder='little', signed=False)
        frame_length = int.from_bytes(self.dataPool[3:7], byteorder='little', signed=False)
        if len(self.dataPool) < frame_length:
            return
        frame_data = self.dataPool[0:(frame_length - 2)]

        if not checksum(frame_data) == int.from_bytes(self.dataPool[(frame_length - 2):frame_length], byteorder='little', signed=False):
            self.dataPool = self.dataPool[2:]
            self.accept(b'')
            return
        frame_body = self.dataPool[7:(frame_length - 2)]
        self.dataPool = self.dataPool[frame_length:]
        return frame_type, frame_body
