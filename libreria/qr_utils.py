import qrcode
import os

def generar_qr(data, filename="codigo_qr.png", carpeta="output"):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    ruta_completa = os.path.join(carpeta, filename)
    qr = qrcode.make(data)
    qr.save(ruta_completa)
    print(f"✅ Código QR guardado en: {ruta_completa}")