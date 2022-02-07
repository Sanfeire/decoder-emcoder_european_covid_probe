import zlib
import cose
from base45 import *
import base45
import base64

data = (b""" 
x.m.mÖì ..·¤|i.ÓZ»ÿ%Ü'¾óó..3¨.B Ë/³.Óîe7.Õ9EYEU¹s.Õíu...Vx«,··º§»7îfq«.v.n.W#jË¹ü),âx/..Ä
Ûe£ê...y«Ùö.l/e1/oxéµÿy.PX7.¼®1½.¯+.}X¿...ë.Dð«Ûa_X...¸#óÎé.æ-+..¯`yÏ.Û.@.Fy'×÷c--¶xã.uÃ±±¥Nó<¿P...i=.°..ÒÖ[.¶^t.&ëµVµ|ú²g
³.CØ.×Dã.´áÛë./-.9T³.º+7j.....¥CgÃë¨.X...E¥vÔ¨..ê.zô§M©.D¸ÿ§.Õ.ê?¯.. n£úß/¯[ìN...Ù.HPkª.rnUKeïPe.µ.»S¥Áf.·ô¨.)k.?=À.M|Å.E¥?.Ð.}Z³â¥`ÏÓ( .=.'&.RÃðx¢..øt.¶(é°HjØTÃÎ..¹Ó7.viÂø.4{.óæ.N._½l_Üt.ø¼ÙÌëí
KX¡ç.=Qmñß.è.98/Mw·n.°öåÃÔÈ"Ê.ÇÚA6Ô.ø.é¯2.Ëw(6Ùs#Èú.s
àö
"""

data_b45 = base45.b45encode(data)
print(data_b45)
