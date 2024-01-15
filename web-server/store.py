import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.text)
    print(r.status_code)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])

def post_consulta():
    url = "https://creditos.habitatguate.org/services/serbipagos.wsdl"
    payload = "<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:con=\"http://serbipagos.bi.com.gt/Consultar\">\r\n   <soapenv:Header/>\r\n   <soapenv:Body>\r\n      <con:Consultar>\r\n         <!--Optional:-->\r\n         <con:Input><![CDATA[<?xml version=\"1.0\" encoding=\"ISO-8859-1\" ?>\r\n    <mensaje>\r\n    <encabezado>\r\n        <convenio>747</convenio>\r\n        <proveedor></proveedor>\r\n        <codigoRetorno></codigoRetorno>\r\n        <mensajeRetorno></mensajeRetorno>\r\n        <autorizacionProveedor>00000000</autorizacionProveedor>\r\n        <autorizacionBanco>0</autorizacionBanco>\r\n    </encabezado>\r\n    <identificador>\r\n        <iden01 largo=\"CODIGO DE PRESTAMO\" corto=\"CODIGO D\">0100000215</iden01>\r\n        <iden02 largo=\"NOMBRE DE CLIENTE\" corto=\"NOMBRE D\"></iden02>\r\n        <iden03 largo=\"DPI\" corto=\"DPI     \"></iden03\r\n        ><iden04 largo=\"\" corto=\"\"></iden04>\r\n        <iden05 largo=\"\" corto=\"\"></iden05>\r\n        <iden06 largo=\"\" corto=\"\"></iden06>\r\n    </identificador>\r\n    <valor>\r\n        <val01  largo=\"PAGO DE PRESTAMO\" corto= \"PAGO DE \"></val01>\r\n        <val02  largo=\"\" corto= \"\"></val02>\r\n        <val03  largo=\"\" corto= \"\"></val03>\r\n        <val04  largo=\"\" corto= \"\"></val04>\r\n        <val05  largo=\"\" corto= \"\"></val05>\r\n        <val06  largo=\"\" corto= \"\"></val06>\r\n    </valor>\r\n</mensaje>]]> \r\n         </con:Input>\r\n      </con:Consultar>\r\n   </soapenv:Body>\r\n</soapenv:Envelope>\r\n"
    headers = {
        'Content-Type': 'text/xml',
        'SOAPAction': '"#POST"'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    print(response.status_code)