import base64
import logging
import os
from xades.xades import Xades, CheckDigit
from suds.client import Client

from models.info_to_sign_xml import InfoToSignXml


def sign_xml_file(infoToSignXml: InfoToSignXml):
    try:
        xades = Xades()
        xades.sign(
            infoToSignXml.pathXmlToSign,
            infoToSignXml.pathXmlSigned,
            infoToSignXml.pathSignatureP12,
            infoToSignXml.passwordSignature)
        return True
    except Exception as e: 
        logging.error('Error to sign xml: %s' % str(e))
    

