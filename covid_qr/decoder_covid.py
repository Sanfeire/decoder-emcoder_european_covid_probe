from base45 import b45decode
import zlib
import cbor2
import pprint

#from urllib.parse import unquote
data = "HC1:V8F5 D ZDW$5YWFV%5GV4W$57L6NG8.%5-/6 A7%CB5 AD*5W$5R%5T8F707*DEE.E -DW0B.ID:R5I/5- 5RZCW$5HEFKUDUZC%:5GAFL%5%6BZ$5T$5L*5T6BW$59%5.DCT6BW$56K4/V5W$5$8CW$5558-+83:40W5V8FF$E5S7W$51*52X7W$5WNBF.BO$50.A81D8%59%5W$5H/5/$5+SA%K52JDW$5W$5KN8T%5W$5A%5E.EW$5YKF9%5W$5J:76*5I:5Y*9W$5D%5M7AA*5U.D-N9G7AW$5KOAW$5SA54%52X7 Z9A%5J:7L*56JBQ352X7W.4N%5V8FC*5Q$5/69+SA-$5E*5GDDPS6W$5Y*9%2C13C- 5SN92%5ADAW$5NA74:5J4FK$56%5A%6 $5F*5Y350PEB*5A0"
#data = unquote(data)

data = data.replace("HC1:", "")
z_data = b45decode(data)
print(z_data)
databytes = bytes(z_data)
print(databytes)
decompress = zlib.decompress(databytes)
print(decompress)
decoded = cbor2.loads(decompress)
#pprint.pprint(cbor2.loads(decoded.value[2]))
print(decoded)

