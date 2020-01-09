import hashlib

hash = "record.db"

print("Hello,Python")
hash1 = hashlib.md5
hash1.update(hash.encode("utf-8"))

print(hash1.digest())

