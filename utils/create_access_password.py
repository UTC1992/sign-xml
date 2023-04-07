import module11
from models.info_access_key import InfoAccessKey


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

    # combination of data
    preAccessKey = dateEmission + codDoc  + rucBusiness + environment + establishment + pointEmission + sequential  + randomNumber
    checkerDigit = module11.modulo11(preAccessKey)

    #join preAccessKey with checkerDigit
    accessKey = preAccessKey + checkerDigit

    # return accessKey combination
    return accessKey
