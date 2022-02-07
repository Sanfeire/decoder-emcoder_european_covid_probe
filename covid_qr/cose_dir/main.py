from cose.messages import CoseMessage
from binascii import unhexlify, hexlify
from cose.messages import Sign1Message
from cose.keys import CoseKey
from cose.headers import Algorithm, KID
from cose.algorithms import EdDSA
from cose.keys.curves import Ed25519
from cose.keys.keyparam import KpKty, OKPKpD, OKPKpX, KpKeyOps, OKPKpCurve
from cose.keys.keytype import KtyOKP
from cose.keys.keyops import SignOp, VerifyOp
from cose.keys import OKPKey, CoseKey
from cose.algorithms import Es256
from os import urandom
from cose.keys.keytype import KtyEC2
from cose.keys.keyparam import KpAlg, EC2KpD, EC2KpCurve
from cose.keys.curves import P256
import sys

message = "A401624445041A632EFCA9061A614DC929390103A101A4617681AA626369781E55524E3A555643493A30313A44453A3138372F333735313234323239323362636F62444562646E026264746A323032312D30392D323462697374526F62657274204B6F63682D496E737469747574626D616D4F52472D313030303330323135626D706C45552F312F32302F3135323862736402627467693834303533393030366276706A3131313933343930303763646F626A313935362D30352D3132636E616DA462666E6753696D70736F6E62676E65486F6D657263666E746753494D50534F4E63676E7465484F4D45526376657265312E302E30"

# Generate random keypair: OKPKpD - private key, OKPKpX - public key



if (len(sys.argv)>1):
	message=str(sys.argv[1])

message=message.encode()

priv = urandom(32)
keyid=b'\x0cK\x15Q+\xe9\x14\x01'

# msg = Sign1Message(phdr = {Algorithm: ECDSA, KID: b'mycrypto'},payload = message.encode())
msg = Sign1Message(phdr={Algorithm: Es256, KID: keyid}, payload=message)

cose_key = {
KpKty: KtyEC2,
KpAlg: Es256, # ECDSA-with-SHA256
EC2KpCurve: P256, 
EC2KpD: priv,
}

# See https://python-cwt.readthedocs.io/en/stable/algorithms.html

cose_key = CoseKey.from_dict(cose_key)


msg.key = cose_key


en = msg.encode(tag=True,sign=True)

print("Key: ",cose_key)
print("Private Key: ",hexlify(cose_key.d))
print("Public Key: ",hexlify(cose_key.x))

print ("\nMessage: ",message)
print ("\nCOSE message: ",en)
print ("\nCOSE encoded (hex): ",hexlify(en).decode())

cos = CoseMessage.decode(en)

cos.key = cose_key

print ("Signature: ",cos.verify_signature())

print ("Decrypted: ",cos.payload.decode())
