import zlib
import base64
import base45
import cbor2
import cose
from cose.messages import CoseMessage

data = """{"v":[{"ci":"URN:UVCI:01:DE:187/37512422923","co":"DE","dn":2,"dt":"2021-09-24","is":"Robert Koch-Institut","ma":"ORG-100030215","mp":"EU/1/20/1528","sd":2,"tg":"840539006","vp":"1119349007"}],"dob":"1956-05-12","nam":{"fn":"Simpson","gn":"Homer","fnt":"SIMPSON","gnt":"HOMER"},"ver":"1.0.0"}"""


desr_cbor2 = cbor2.dumps(data)
cose = CoseMessage.encode(desr_cbor2)
compress_zlib = zlib.compress(cose)
data_b45 = base45.b45encode(compress_zlib)

print (data_b45)
