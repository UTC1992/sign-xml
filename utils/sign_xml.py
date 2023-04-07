import base64
import logging
import os
from pathlib import Path

from xades.xades import Xades, CheckDigit
from suds.client import Client

def sign_xml_file():
    try: 
        
        path_xml_signed = os.path.abspath('signed-xmls/factura-firmada.xml')

        name_xml = 'no-signed-xmls/factura.xml'
        path_xml = os.path.join(name_xml)

        name_p12 = 'cs.p12'
        path_p12 = os.path.join(name_p12)

        password = 'narutO251993'.encode()
        
        xades = Xades()
        xades.sign(path_xml,path_xml_signed, path_p12, password)


        with open(path_xml_signed, 'rb') as f:
            xml_signed = f.read()

        base64_binary_xml = base64.b64encode(xml_signed).decode('utf-8')

        
        try:
          sri_client = Client(URL_RECEPTION)
          response_suds = sri_client.service.validarComprobante(base64_binary_xml)

          logging.info("Success to send xml")
          logging.warning(response_suds)
        except Exception as e: 
          logging.error('Error al enviar el documento: %s' % str(e))
            
    except Exception as e: 
        logging.error('Error al firmar el documento: %s' % str(e))

def check_digit(text):
    check = CheckDigit()
    return check.compute_mod11(text)


def leer_archivo(ruta, modo='r'):

    with open(ruta, modo) as archivo:
        return archivo.read()

    
  