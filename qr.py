import qrcode


drive_link = "https://drive.google.com/file/d/1FQa6Drq4MRXitjls9WYF2UJ5jrU6CvaS/view?usp=drivesdk)…"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(drive_link)
qr.make(fit=True)

# Generate Image
img = qr.make_image(fill_color="black", back_color="white")

# Save QR Code
img.save("B_Ajaz_Ali.png")

print("✅ QR Code generated successfully!")
print("B_Ajaz_Ali.png")