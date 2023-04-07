import json
import xmltodict
from lxml import etree


def jsonToXml(json_str):

    # Convert JSON to Python dictionary
    data = json.loads(json_str)

    # Convert dictionary to XML string
    xml_str = xmltodict.unparse(data)

    return xml_str


def createXml(access_key):
    root = etree.Element('factura', attrib={
                         'id': 'comprobante', 'version': '1.0.0'})
    infoTributaria = etree.SubElement(root, 'infoTributaria')
    ambiente = etree.SubElement(infoTributaria, 'ambiente')
    ambiente.text = '1'
    tipoEmision = etree.SubElement(infoTributaria, 'tipoEmision')
    tipoEmision.text = '1'
    razonSocial = etree.SubElement(infoTributaria, 'razonSocial')
    razonSocial.text = 'MAURO OMAR GUANOLUISA ARCINIEGA'
    nombreComercial = etree.SubElement(infoTributaria, 'nombreComercial')
    nombreComercial.text = 'TSCorp'
    ruc = etree.SubElement(infoTributaria, 'ruc')
    ruc.text = '0503254849001'
    claveAcceso = etree.SubElement(infoTributaria, 'claveAcceso')
    claveAcceso.text = access_key
    codDoc = etree.SubElement(infoTributaria, 'codDoc')
    codDoc.text = '01'
    estab = etree.SubElement(infoTributaria, 'estab')
    estab.text = '001'
    ptoEmi = etree.SubElement(infoTributaria, 'ptoEmi')
    ptoEmi.text = '100'
    secuencial = etree.SubElement(infoTributaria, 'secuencial')
    secuencial.text = '000000001'
    dirMatriz = etree.SubElement(infoTributaria, 'dirMatriz')
    dirMatriz.text = 'Barrio: ISIMBO Calle: PRINCIPAL Número: S/N'

    infoFactura = etree.SubElement(root, 'infoFactura')
    fechaEmision = etree.SubElement(infoFactura, 'fechaEmision')
    fechaEmision.text = '06/04/2023'
    dirEstablecimiento = etree.SubElement(infoFactura, 'dirEstablecimiento')
    dirEstablecimiento.text = 'Barrio: ISIMBO Calle: PRINCIPAL Número: S/N '
    # contribuyenteEspecial = etree.SubElement(
    #     infoFactura, 'contribuyenteEspecial')
    # contribuyenteEspecial.text = '1'
    obligadoContabilidad = etree.SubElement(
        infoFactura, 'obligadoContabilidad')
    obligadoContabilidad.text = 'NO'
    tipoIdentificacionComprador = etree.SubElement(
        infoFactura, 'tipoIdentificacionComprador')
    tipoIdentificacionComprador.text = '04'
    # guiaRemision = etree.SubElement(infoFactura, 'guiaRemision')
    # guiaRemision.text = '1'
    razonSocialComprador = etree.SubElement(infoFactura, 'razonSocialComprador')
    razonSocialComprador.text = 'Cliente Demo'
    identificacionComprador = etree.SubElement(infoFactura, 'identificacionComprador')
    identificacionComprador.text = '9999999999999'
    direccionComprador = etree.SubElement(infoFactura, 'direccionComprador')
    direccionComprador.text = 'Quito, Amazonas'
    totalSinImpuestos = etree.SubElement(infoFactura, 'totalSinImpuestos')
    totalSinImpuestos.text = '100'
    totalDescuento = etree.SubElement(infoFactura, 'totalDescuento')
    totalDescuento.text = '0.00'
    
    totalConImpuestos = etree.SubElement(infoFactura, 'totalConImpuestos')
    
    totalImpuesto1 = etree.SubElement(totalConImpuestos, 'totalImpuesto')
    codigo1 = etree.SubElement(totalImpuesto1, 'codigo')
    codigo1.text = '2'
    codigoPorcentaje1 = etree.SubElement(totalImpuesto1, 'codigoPorcentaje')
    codigoPorcentaje1.text = '0'
    baseImponible1 = etree.SubElement(totalImpuesto1, 'baseImponible')
    baseImponible1.text = '100'
    valor1 = etree.SubElement(totalImpuesto1, 'valor')
    valor1.text = '0.00'

    # totalImpuesto2 = etree.SubElement(totalConImpuestos, 'totalImpuesto')
    # codigo2 = etree.SubElement(totalImpuesto2, 'codigo')
    # codigo2.text = '2'
    # descuentoAdicional2 = etree.SubElement(totalImpuesto2, 'descuentoAdicional')
    # descuentoAdicional2.text = '2'
    # codigoPorcentaje2 = etree.SubElement(totalImpuesto2, 'codigoPorcentaje')
    # codigoPorcentaje2.text = '2'
    # baseImponible2 = etree.SubElement(totalImpuesto2, 'baseImponible')
    # baseImponible2.text = '2'
    # valor2 = etree.SubElement(totalImpuesto2, 'valor')
    # valor2.text = '2'

    # totalImpuesto3 = etree.SubElement(totalConImpuestos, 'totalImpuesto')
    # codigo3 = etree.SubElement(totalImpuesto3, 'codigo')
    # codigo3.text = '2'
    # codigoPorcentaje3 = etree.SubElement(totalImpuesto3, 'codigoPorcentaje')
    # codigoPorcentaje3.text = '2'
    # baseImponible3 = etree.SubElement(totalImpuesto3, 'baseImponible')
    # baseImponible3.text = '2'
    # valor3 = etree.SubElement(totalImpuesto3, 'valor')
    # valor3.text = '2'

    propina = etree.SubElement(infoFactura, 'propina')
    propina.text = '0'
    importeTotal = etree.SubElement(infoFactura, 'importeTotal')
    importeTotal.text = '100'
    moneda = etree.SubElement(infoFactura, 'moneda')
    moneda.text = 'DOLAR'

    pagos = etree.SubElement(infoFactura, 'pagos')
    pago = etree.SubElement(pagos, 'pago')
    formaPago = etree.SubElement(pago, 'formaPago')
    formaPago.text = '20'
    total = etree.SubElement(pago, 'total')
    total.text = '100'
    # plazo = etree.SubElement(pago, 'plazo')
    # plazo.text = '2'
    # unidadTiempo = etree.SubElement(pago, 'unidadTiempo')
    # unidadTiempo.text = '2'

    # valorRetIva = etree.SubElement(infoFactura, 'valorRetIva')
    # valorRetIva.text = '2'
    # valorRetRenta = etree.SubElement(infoFactura, 'valorRetRenta')
    # valorRetRenta.text = '2'

    # end infoFactura

    detalles = etree.SubElement(root, 'detalles')
    detalle = etree.SubElement(detalles, 'detalle')
    codigoPrincipal = etree.SubElement(detalle, 'codigoPrincipal')
    codigoPrincipal.text = 'PRODUCTO-001'
    # codigoAuxiliar = etree.SubElement(detalle, 'codigoAuxiliar')
    # codigoAuxiliar.text = '2'
    descripcion = etree.SubElement(detalle, 'descripcion')
    descripcion.text = 'EQUIPO DE COMPUTO'
    cantidad = etree.SubElement(detalle, 'cantidad')
    cantidad.text = '1.0'
    precioUnitario = etree.SubElement(detalle, 'precioUnitario')
    precioUnitario.text = '100'
    descuento = etree.SubElement(detalle, 'descuento')
    descuento.text = '0.00'
    precioTotalSinImpuesto = etree.SubElement(detalle, 'precioTotalSinImpuesto')
    precioTotalSinImpuesto.text = '100'

    # detallesAdicionales = etree.SubElement(detalle, 'detallesAdicionales')
    # etree.SubElement(detallesAdicionales, 'detAdicional', attrib={'nombre': 'Marcha Chevrolet', 'valor': 'Chevrolet'})
    # etree.SubElement(detallesAdicionales, 'detAdicional', attrib={'nombre': 'Modelo', 'valor': '2012'})
    # etree.SubElement(detallesAdicionales, 'detAdicional', attrib={'nombre': 'Chasis', 'valor': '8LDETA03V20003289'})

    impuestos = etree.SubElement(detalle, 'impuestos')

    impuesto = etree.SubElement(impuestos, 'impuesto')
    codigo = etree.SubElement(impuesto, 'codigo')
    codigo.text = '2'
    codigoPorcentaje = etree.SubElement(impuesto, 'codigoPorcentaje')
    codigoPorcentaje.text = '0'
    tarifa = etree.SubElement(impuesto, 'tarifa')
    tarifa.text = '0.0'
    baseImponible = etree.SubElement(impuesto, 'baseImponible')
    baseImponible.text = '100'
    valor = etree.SubElement(impuesto, 'valor')
    valor.text = '0.00'

    infoAdicional = etree.SubElement(root, 'infoAdicional')
    campoAdicional = etree.SubElement(infoAdicional, 'campoAdicional', attrib={'nombre': 'email'})
    campoAdicional.text = 'demo@gmail.com'

    tree = etree.ElementTree(root)
    tree.write('catalog.xml', xml_declaration=True,
              encoding='UTF-8', standalone=True)
