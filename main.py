import sys
import json

sys.path.append('./utils')

# Add module
from utils import module11
from utils import create_xml
from utils import create_access_password
from utils import sign_xml

from xades_bes_sri_ec import xades

# number = 310120230105032548490012001100000000005
# checker = module11.modulo11(number)
# print(checker)

# with open('invoice.json', 'r') as f:
#     dataJson = json.load(f)


# json_str = json.dumps(dataJson)
# xmlFile = createXml.jsonToXml(json_str)

# with open('xml-file.xml', 'w') as f:
#     f.write(xmlFile)


# private_key = create_access_password.getPasswordOfP12File()
# access_key = create_access_password.createAccessPassword()

# print( access_key)
# print( len(access_key))

access_key = create_access_password.createAccessPassword()
create_xml.createXml(access_key)

sign_xml.sign_xml()

