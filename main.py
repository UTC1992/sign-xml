import os
import sys
import random
import asyncio
sys.path.append('./utils')

from utils import send_xml
from utils import sign_xml
from utils import create_access_password
from utils import create_xml

from models.info_to_sign_xml import InfoToSignXml
from models.info_access_key import InfoAccessKey
from models.info_tributaria import InfoTributaria
from dotenv import dotenv_values

# Add module

# load environments variables
env_vars = dotenv_values(".env")


def main():
    # create xml

    # info to create access key
    infoAccessKey = InfoAccessKey(
        '07',
        '04',
        '2023',
        '01',
        '0503254849001',
        '1',
        '1',
        '001',
        '100',
        '000000011',
        str(random.randint(1, 99999999)).zfill(8),
    )
    accessKey = create_access_password.createAccessKey(infoAccessKey)
    print('access key', len(accessKey))
    # info to tax
    infoTax = InfoTributaria(
        '1',
        '1',
        'MAURO OMAR GUANOLUISA ARCINIEGA',
        'TSCorp',
        infoAccessKey.rucBusiness,
        str(accessKey),
        infoAccessKey.codDoc,
        infoAccessKey.establishment,
        infoAccessKey.pointEmission,
        infoAccessKey.sequential,
        'Quito'
    )

    # generate xml
    xml = create_xml.createXml(infoTax)
    fileName = ''.join(accessKey) + '.xml'
    pathToSaveXml = os.path.join('xmls/no-signed-xml/' + fileName)

    # save xml in directory
    create_xml.saveXml(xml, pathToSaveXml)

    # sign xml
    # data certificate .p12
    nameCertificateP12 = infoAccessKey.rucBusiness + '.p12'
    pathCertificateP12 = os.path.join('certificatesP12/' + nameCertificateP12)
    passwordCertificate = env_vars["PASSWORD_P12"]

    # data file to sign
    pathXmlToSign = pathToSaveXml

    # data file signed
    nameXmlSigned = fileName
    pathXmlSigned = os.path.join('xmls/yes-signed-xml/' + nameXmlSigned)

    infoToSignXml = InfoToSignXml(
        pathXmlToSign,
        pathXmlSigned,
        pathCertificateP12,
        passwordCertificate
    )

    isXmlCreated = sign_xml.sign_xml_file(infoToSignXml)

    # sent xml to sri web service
    urlReception = env_vars["URL_RECEPTION"]
    urlAuthorization = env_vars["URL_AUTHORIZATION"]


    if isXmlCreated:
        send_xml.send_xml_to_reception(
            pathXmlSigned,
            urlReception,
        )

        send_xml.send_xml_to_authorization(
            accessKey,
            urlAuthorization,
        )

# run program
main()
