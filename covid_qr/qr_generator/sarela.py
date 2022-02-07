import qrcode

input_data = "HC1:6BFOXN%TSMAHN-H2YSLMN$VKYURDX9:D4K*F:46/7DCET8X2N8TLXK3W3NUJKCILML%ZJJ7JYKI2YCKF53$IM+IR0PTK2WH6PK6/EBPJA3P6*CMVZ4FW3LDM:UC*GPXS40 LHZA KE4+GKHGSRDWHK$DJTJLCVMTTJ%KNVUK:JMWJKYULY-KIVMZOM1JA20G9QD6IAN$36IASD9YHILIIX2MO.K1GGYIAHA6B 1*PP:+P*.1D9R+Q6646P$0.KC:XIBEIVG395EV3EVCK09D5WCFVA.QO5VA81K0ECM8CXVDC8C90JK.A+ C/8DXEDKG0CGJ5AL+-4I+LX76QW6-.QPR6Q3QR$P*NIV1J03T723LH2-5M:S20DJ92KFN2R63BVT4BL8PS113*IJC0JVE0I0N%G98AL3*I80TJ74F%CD 810H54PNY0Z*1QWQ%NEZL19%EK:F%SFA7G3L26AIHBRPU2D1A8/737EMZPHXM3JK IV0$D4 1 PBIX86NHL*EJZF 4WL5S VOAMM6XMBQSM14E3M6Y0 O6THI"

qr = qrcode.QRCode(
	version=1,
	box_size=10,
	border=5)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('sarela_2002.png')
