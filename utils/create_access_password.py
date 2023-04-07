import hashlib
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12
import os
import random
import module11



def createAccessPassword( pass_private = '' ):
    # Información de la factura
    date_authorization = '06042023'
    type_voucher = '01' # Factura
    ruc_issuer = '0503254849001'
    environment = '1'
    establishment = '001'
    punto_emision = '100'
    sequential = '000000001'
    aleatorio = str(random.randint(1, 999999999)).zfill(9) 

    # Combinación de la información de la factura y la clave privada
    password = date_authorization + type_voucher  + ruc_issuer + environment + establishment + punto_emision + sequential  + aleatorio
    digito_verificador = module11.modulo11(password)
    password += digito_verificador

    # Generación del hash SHA-1
    # password_access = hashlib.sha1(password.encode('utf-8')).hexdigest()

    # Salida de la clave de acceso generada
    return password

def getPasswordOfP12File():
    # ruta del archivo .p12
    ruta_p12 = 'utils/electronic-sign.p12'

    # contraseña del archivo .p12
    password_provided = str('narutO251993')
    password = password_provided.encode()
    
    # Load the PKCS12 file
    with open(os.path.abspath(ruta_p12), 'rb') as f:
        p12_data = f.read()

    # Parse the PKCS12 data
    private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(p12_data, password)

    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    return private_key_pem