import qrcode as pygr

def Qrcode_Maker(data):
    qr = pygr.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)
    pic = qr.make_image()
    pic.save('qrcode.png')
Qrcode_Maker('https://www.yandex.ru')