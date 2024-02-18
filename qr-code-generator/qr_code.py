import qrcode
import uuid

def generate_qrcode(text):
    
    filename = f"qrcode_{str(uuid.uuid4())[:8]}.png"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as: {filename}")

url = input("Enter your url: ")
generate_qrcode(url)
