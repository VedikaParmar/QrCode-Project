import qrcode

data = "https://www.cgitinstituteindore.com"

code = qrcode.QRCode(
    version=1,
    error_correction= qrcode.constants.ERROR_CORRECT_L,
    border=4,
    box_size=10,
    )

code.add_data(data)
code.make(fit=True)

img = code.make_image(fill_color='black',back_color='white')

img.save("OurQr.png")


