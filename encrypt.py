import orjson
import base64
with open("words.json") as fp:
    words = fp.read()

enc = base64.b64encode(bytes(words, "utf-8"))
enc = base64.b64encode(enc)
res = orjson.loads(base64.b64decode(base64.b64decode(enc)))

with open("words.txt", "w") as fp:
    fp.write(enc.decode("utf-8"))

print(orjson.loads(words) == res)
