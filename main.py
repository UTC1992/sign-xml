import sys
import random
sys.path.append('./utils')
import os

# Add module
from utils import create_xml
from utils import create_access_password
from utils import sign_xml
from models.info_tributaria import InfoTributaria
from models.info_access_key import InfoAccessKey
from models.info_to_sign_xml import InfoToSignXml

# create xml

# info to create access key
infoAccessKey = InfoAccessKey(
    '07',
    '04',
    '2023',
    '01',
    '0503254849001',
    '1',
    '001',
    '100',
    '000000002',
    str(random.randint(1, 999999999)).zfill(9) 
)
accessKey = create_access_password.createAccessKey(infoAccessKey)

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
fileName = ''.join(accessKey)+'.xml'
pathToSaveXml = os.path.join('xmls/no-signed-xml/'+fileName)

# save xml in directory
#create_xml.saveXml(xml, pathToSaveXml)

# sign xml
infoToSignXml = InfoToSignXml(

)

sign_xml.sign_xml()


