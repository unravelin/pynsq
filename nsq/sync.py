

import socket
import struct

from nsq import protocol


class SyncConn(object):
    def __init__(self, timeout=1.0):
        self.buffer = ''
        self.timeout = timeout
        self.s = None

    def connect(self, host, port):
        assert isinstance(host, str)
        assert isinstance(port, int)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(self.timeout)
        self.s.connect((host, port))
        self.s.send(protocol.MAGIC_V2)

    def _readn(self, size):
        while True:
            if len(self.buffer) >= size:
                break
            packet = self.s.recv(4096)
            if not packet:
                raise Exception('failed to read %d' % size)
            self.buffer += packet
        data = self.buffer[:size]
        self.buffer = self.buffer[size:]
        return data

    def read_response(self):
        size = struct.unpack('>l', self._readn(4))[0]
        return self._readn(size)

    def send(self, data):
        self.s.send(data)
