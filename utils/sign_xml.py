from xades.x import Xades,
import os

# Cargar clave privada en formato .p12
cert_path = "electronic-sign.p12"
clave_privada = create_access_password.getPasswordOfP12File()

# Cargar archivo XML a firmar
xml_path = "catalog.xml"
xml_data = open(xml_path, "rb").read()

# Firmar archivo XML
signed_xml = XMLSigner().sign(
    data=xml_data,
    key=clave_privada,
    algorithm="rsa-sha256",
    reference_uri="#comprobante",
)

# Escribir archivo XML firmado
signed_xml_path = "archivo_firmado.xml"
with open(signed_xml_path, "wb") as f:
    f.write(signed_xml)