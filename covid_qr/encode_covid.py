from base45 import b45encode
from base45 import b45decode
import base45
import zlib
import cbor2
import pprint

#decoder estructure "base45.b45encode"

#from urllib.parse import unquote
data = ("""

{
  "1": "DE",
  "4": 1651928945,
  "6": 1620392945,
  "-260": {
    "1": {
      "v": [
        {
          "ci": "01DE/00000/1119349007/BW1DDJEZX2B0VGVYII1QN7DDU#S",
          "co": "DE",
          "dn": 2,
          "dt": "2021-05-07",
          "is": "Bundesministerium für Gesundheit",
          "ma": "ORG-100030215",
          "mp": "EU/1/20/1528",
          "sd": 2,
          "tg": "840539006",
          "vp": "1119349007"
        }
      ],
      "dob": "1970-01-01",
      "nam": {
        "fn": "Dießner Musterfrau",
        "gn": "Erika Dörte",
        "fnt": "DIESSNER<MUSTERFRAU",
        "gnt": "ERIKA<DOERTE"
      },
      "ver": "1.0.0"
    }
  }
}

""")
#data = unquote(data)

#data = data.replace("HC1:", "")
databytes = bytes(data)
z_data = base45.b45decode(z_data)
#databytes = bytes(z_data)
compress = zlib.compress(databytes)
#coded = cbor2.loads(compress)
#pprint.pprint(cbor2.loads(decoded.value[2]))
print (data)
