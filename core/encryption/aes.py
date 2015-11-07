#
# Crypto.Cipher AES wrapper that supports variable length strings when using CBC mode.
# https://pypi.python.org/pypi/pycrypto
#
import base64
from Crypto import Random
from Crypto.Cipher import AES

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]

class AesEncryptor:

    @staticmethod
    def try_decrypt(text, encryptionKey):
        try:
            decrypted = AesEncryptor.decrypt(text, encryptionKey)
            return True, decrypted
        except Exception:
            pass

        return False, None

    @staticmethod
    def encrypt(text, encryptionKey):
        text = pad(text)
        encryptionKey = pad(encryptionKey)
        iv = Random.new().read(BS)
        aes = AES.new(encryptionKey, AES.MODE_CBC, iv)
        return base64.b64encode(iv + aes.encrypt(text))
        
    @staticmethod
    def decrypt(encrypted, encryptionKey):
        # normalize key
        encryptionKey = pad(encryptionKey)
        encrypted = base64.b64decode(encrypted)
        iv = encrypted[:16]
        aes = AES.new(encryptionKey, AES.MODE_CBC, iv)
        return unpad(aes.decrypt(encrypted[16:])).decode("utf-8")

