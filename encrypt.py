import orjson
import base64

a = orjson.loads(open("words.json").read())
a = '\n'.join([x for x in a if len(x) == 5])
open("words.txt", "wb").write(
    base64.b64encode(
        base64.b64encode(
            bytes(
                a,
                "utf-8"
            )
        )
    )
)
