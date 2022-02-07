import qrcode

input_data = "HC1:6BFOXN*TS0BI$ZD4N9:9S6RCVN5+O30K3/XIV0W23NTDEPWK G2EP4J0B3KLASMUG8GJL8LLG.3SA3/-2E%5VR5VVBJZILDBZ8D%JTQOL2009UVD0HX2JN*4CY009TX/9F/GZ%5U1MC82*%95HC2FCG2K80H-1GW$5IKKQJO0OPN484SI4UUIMI.J9WVHWVH+ZE/T9MX1HRIWQHCR2HL9EIAESHOP6OH6MN9*QHAO96Y2/*13A5-8E6V59I9BZK6:IR/S09T./0LWTHC0/P6HRTO$9KZ56DE/.QC$QUC0:GOODPUHLO$GAHLW 70SO:GOV636*2. KOKGKZGJMI:TUNBGKD3LWTC509X6Q3QR$P*NIC0J$+T5IJLAF5.BZHIH2E+HPR$MV*OI%K6ZNWBRZ+P/Q8G8J.XR H9/UIGSU6MHIS77SGF1WTRG-VFXQGDVBK*RZP3/UI2YUQKEQQG%+N6$DU+VWQGTVBUVPQRHIY1VS11O1IR3MME9G4Z+3PJ5**SZ0DKISN%AX:VQMMQ4J%J1%NJ6IFXQFZX6:RRJPU$I0PTSZZICFSNDS4+5XR2A*D95O%+VC1AP$S%U27JRWPB$*0$SU TI"

qr = qrcode.QRCode(
	version=1,
	box_size=10,
	border=5)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('erika_doerte.png')
