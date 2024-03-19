import qrcode

website_link = input("Enter the website link: ")
qr_version = int(input("Enter the QR code version (1-40): "))
qr_box_size = int(input("Enter the QR code box size: "))
qr_border = int(input("Enter the QR code border: "))

qr = qrcode.QRCode(version=qr_version, box_size=qr_box_size, border=qr_border)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color='black', back_color='white')
img.save('qr_code.png')