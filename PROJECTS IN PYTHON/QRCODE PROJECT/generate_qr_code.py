"""i am installing both qrcode and another library pillow that is used for
image handling"""
#importing qrcode
import qrcode
data  = "https://chatgpt.com/"

#creating a QRCODE instance
qr = qrcode.QRCode(version=1,  #gr code complexity
error_correction=qrcode.constants.ERROR_CORRECT_L, #low error correction
box_size=10,     #this is the size of qr code in pixels
border=4     #border thickness and 4 is by default
)

#now we will add data to this instance
qr.add_data(data)     #adds the data
qr.make(fit=True)

#now we are going to make image
img  = qr.make_image(fill="black",back_color="white")

#save the QRCODE instance as an image, we have already given the data to it
img.save("qrcode.png")

#show qrcode
img.show()
