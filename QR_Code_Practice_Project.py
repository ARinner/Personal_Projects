# python -m venv venv
# .\venv\Scripts\activate
# pip install qrcode[pil]

# creates a virtual environment in your current folder, activates the virtual environment so that when you install packages
# activates the virtual environment so that when you install packages
# pip is Python’s package manager.
# all done in terminal


import qrcode
# Define your data (Will change later)
data = 'Did this work?!'

#Generate your QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# create an image from the QR Code instance
img = qr.make_image(fill_color="black", back_color="white")
# Save the image to a file
img.save("qr_code.png")
# Display the image (optional)
print("QR code generated and saved as qr_code.png")
# Open the image file to display it (optional)  


