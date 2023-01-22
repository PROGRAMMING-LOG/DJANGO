import base64
import random
from Crypto.Cipher import AES
from hashlib import sha256

class AESCipher(object):
    def __init__(self, key, block_size=32):
        self.bs = block_size
        if len(key) >= len(str(block_size)):
            self.key = key[:block_size]
        else:
            self.key = self._pad(key)

    def generate_salt(self, digit_num):
        digits_and_alphabets = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join(random.sample(digits_and_alphabets, digit_num)).encode()

    def encrypt(self, raw):
        raw = self._pad(raw)
        salt = self.generate_salt(AES.block_size)
        salted = ''.encode()
        dx = ''.encode()
        while len(salted) < 48:
            hash = dx + self.key.encode() + salt
            dx = sha256(hash).digest()
            salted = salted + dx

        key = salted[0:32]
        iv = salted[32:48]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        print(raw)
        return base64.b64encode(salt + cipher.encrypt(raw))

    def mb_encrypt(self, raw):
        raw = base64.b64encode(raw.encode('utf-8')).decode('utf-8')

        raw = self._pad(raw)
        salt = self.generate_salt(AES.block_size)
        salted = ''.encode()
        dx = ''.encode()
        while len(salted) < 48:
            hash = dx + self.key.encode() + salt
            dx = sha256(hash).digest()
            salted = salted + dx

        key = salted[0:32]
        iv = salted[32:48]

        cipher = AES.new(key, AES.MODE_CBC, iv)
        return base64.b64encode(salt + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        salt = enc[0:16]
        rounds = 3

        data00 = self.key.encode() + salt
        hash = {}
        hash[0] = sha256(data00).digest()
        result = hash[0]
        for i in range(1, rounds):
            hash[i] = sha256(hash[i - 1] + data00).digest()
            result += hash[i]

        key = result[0:32]
        iv = result[32:48]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.decrypt(enc[16:]).decode()

    def mb_decrypt(self, enc):
        enc = base64.b64decode(enc)
        salt = enc[0:16]
        rounds = 3

        data00 = self.key.encode() + salt
        hash = {}
        hash[0] = sha256(data00).digest()
        result = hash[0]
        for i in range(1, rounds):
            hash[i] = sha256(hash[i - 1] + data00).digest()
            result += hash[i]

        key = result[0:32]
        iv = result[32:48]
        cipher = AES.new(key, AES.MODE_CBC, iv)

        decrypt_enc = cipher.decrypt(enc[16:])
        return base64.b64decode(decrypt_enc).decode()

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]
