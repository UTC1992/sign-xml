import base64
import logging
from suds.client import Client
import zeep

from models.info_to_sign_xml import InfoToSignXml

def send_xml_to_reception(pathXmlSigned: str, urlToReception: str):
    # get xml from directory
    with open(pathXmlSigned, 'rb') as f:
        xml_signed = f.read()

    # encode xml to base64 and decode in utf-8
    base64_binary_xml = base64.b64encode(xml_signed).decode('utf-8')

    try:
        sri_client = Client(urlToReception)
        response_suds = sri_client.service.validarComprobante(
            base64_binary_xml)
        
        logging.info("Success to send xml")
        logging.warning(response_suds)
    except Exception as e:
        logging.error('Error to send xml for reception: %s' % str(e))

def send_xml_to_authorization(accessKey: str, urlToAuthorization: str):
    try:
        sri_client = zeep.Client(urlToAuthorization)
        response_suds = sri_client.service.autorizacionComprobante(accessKey)
        
        logging.info("Success in authorization")
        logging.warning(response_suds)
    except Exception as e:
        logging.error('Error to send xml for reception: %s' % str(e))
