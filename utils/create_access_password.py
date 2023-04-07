import module11
from models.info_access_key import InfoAccessKey
from xades import xades

def createAccessKey( infoAccessKey: InfoAccessKey ):
    # Info de la invoice
    dateEmission = ''.join(infoAccessKey.getDateComplete())
    codDoc = ''.join(infoAccessKey.codDoc) # Doc type Invoice
    rucBusiness = ''.join(infoAccessKey.rucBusiness)
    environment = ''.join(infoAccessKey.environment)
    establishment = ''.join(infoAccessKey.establishment)
    pointEmission = ''.join(infoAccessKey.pointEmission)
    sequential = ''.join(infoAccessKey.sequential)
    randomNumber = ''.join(infoAccessKey.randomNumber)
    typeEmission = ''.join(infoAccessKey.typeEmission)

    # combination of data
    preAccessKey = dateEmission + codDoc  + rucBusiness + environment + establishment + pointEmission + sequential  + randomNumber + typeEmission
    print(len(preAccessKey))
    # checkerDigit = module11.modulo11(preAccessKey)
    checkDigit = xades.CheckDigit()
    checkerDigit = str(checkDigit.compute_mod11(preAccessKey))
    print(checkerDigit)
    # validate when the digit is 10
    if int(checkerDigit) == 10:
        checkerDigit = 1
    if int(checkerDigit) == 11:
        checkerDigit = 0

    #join preAccessKey with checkerDigit
    accessKey = preAccessKey + checkerDigit

    # return accessKey combination
    return accessKey
