>>> import zlib
>>> import base64
>>> import base45
>>> import cbor2
>>> data = "{1: 'NO', 4: 1635199200, 6: 1624347447, -260: {1: {'r': [{'ci': 'URN:UVCI:01:NO:PRV/EV6EVFPHCEGX108VC', 'co': 'NO', 'df': '2021-04-26', 'du': '2021-10-26', 'fr': '2021-04-26', 'is': 'Norwegian Institute of Public Health', 'tg': '840539006'}], 'dob': '1979-05-12', 'nam': {'fn': 'Telokk', 'gn': 'Gry', 'fnt': 'TELOKK', 'gnt': 'GRY'}, 'ver': '1.3.0'}}}"
>>> print (data)
{1: 'NO', 4: 1635199200, 6: 1624347447, -260: {1: {'r': [{'ci': 'URN:UVCI:01:NO:PRV/EV6EVFPHCEGX108VC', 'co': 'NO', 'df': '2021-04-26', 'du': '2021-10-26', 'fr': '2021-04-26', 'is': 'Norwegian Institute of Public Health', 'tg': '840539006'}], 'dob': '1979-05-12', 'nam': {'fn': 'Telokk', 'gn': 'Gry', 'fnt': 'TELOKK', 'gnt': 'GRY'}, 'ver': '1.3.0'}}}
>>> desr_cbor2 = cbor2.dumps(data)
>>> print(desr_cbor2)
b"y\x01^{1: 'NO', 4: 1635199200, 6: 1624347447, -260: {1: {'r': [{'ci': 'URN:UVCI:01:NO:PRV/EV6EVFPHCEGX108VC', 'co': 'NO', 'df': '2021-04-26', 'du': '2021-10-26', 'fr': '2021-04-26', 'is': 'Norwegian Institute of Public Health', 'tg': '840539006'}], 'dob': '1979-05-12', 'nam': {'fn': 'Telokk', 'gn': 'Gry', 'fnt': 'TELOKK', 'gnt': 'GRY'}, 'ver': '1.3.0'}}}"
>>> compress_zlib = zlib.compress(desr_cbor2)
>>> print (compress_zlib)
b'x\x9ce\x8fAO\x83@\x10\x85\xe3?\xd9\xdb\\\xa0\xce.\x0b\x94\xbd\x12\xa4M\r\x10b\x89\xa6\xa9\tE@R\x84\x84.\x9a\x86\xf0\xdfe\xb7\xea\xc5\xd3\xee\xfb\xde\xcb\x9b\x99\xeb\xdd\xebD\x05\x81(\x06\x83pA\xa8c\xd9\xd4\xf3\x18\xa2A\x1c%\x19\xb7\xb8\xcb\xb9k\x10\x939(\x88JO0\x80 \x87\t\x8afya\x9fFb\x9f\xf9[\x81TD\xb1H\xd2\xec>\xc8\x9c {H6~\x10>S\\g\xfe\xd2\x0eE\x0f\xbf\x93\xe0\xadR\x7f\x86\x8c\x9a\xc8\x97f\xcd\xc6?F\xf1\x87U\xc3\xff\\s\xd1=\xfd\xf0U\xd6M\xde\x91mw\x91\x8d\x1ceI\xfa\x8a$\xe3\xa9m\n\xb2)\xf3V\xbe\xab\xb4\xacUz\xcd\xd1\xb6<D\x07\xe6\xa3\x1a\xd5\x9f\x14\xa5\x9e\xeb\x99h\x9b\x94\xa9d\x97\x7f\x80:\xae\xea\x94\xf7T\xb6\xfd\xf9\xacx\xadu8\\\xf5B\x9d\xd4n\xf0\x18\xefv7W\x830}\x81y\x91\x9f\xa5\xde\x98\xae\xac\x15\xc2<\xcf\xdf\xc0\x96W\xfc'
>>> data_b45 = base45.b45encode(compress_zlib)
>>> print (data_b45)
b'6BFY$COB8UQG:32ZWSGOR.VB.2Q*K1R+NVYKET1PKC53LX71-58*XG5+5T2H*ASCBNI0PO9UK7S8UJ  TIXTEV0V25XRGND81SCK-Q653IA82V47AN/XP3ODORIQ55XH9-56254C91/.CGFCI+83AKPPBHTAOIM-TQ7.78XJFQF0+6I22AOAR6D:OQ*W8%9O7ISEJAJ0HOPJD6JS0Q/:71OU+$AWCW*SET$7AHU64R76SX$D1IIOQ3%F9*KH6ZSEZDONMEYUV4O$$MC A*0QW1N0R837TTH3:4K8.KDZT4ADWZIBWCF5G$I7MTT1CV06NGPVNBF% E$XB/I8M%Q*FUCCU$:6EQG:%FQGF98KE6SV3MZX2.U7+CSC0JR5'
>>>
