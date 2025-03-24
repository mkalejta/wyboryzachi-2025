import qrcode

# Podaj link, który ma być zakodowany w QR
link = "https://wyboryzachi-2025.pl/"

# Tworzenie obiektu QRCode
qr = qrcode.QRCode(
    version=1,  # Rozmiar QR (1 to najmniejszy)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Rozmiar pojedynczej komórki
    border=4,  # Grubość granicy
)

# Dodanie danych (linku) do QR
qr.add_data(link)
qr.make(fit=True)

# Tworzenie obrazu
img = qr.make_image(fill='black', back_color='white')

# Zapisz obraz do pliku
img.save("qr_code.png")
