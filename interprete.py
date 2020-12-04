import requests
import json
import urllib3
import xmltodict as xml

opc = 0 
while opc != 5: 
    print("____________________________") 
    print("| 1.- Enlistar interprete  |")
    print("____________________________")
    print("| 2.-       agregar        |")
    print("____________________________")
    print("| 3.-    modificar         |")
    print("____________________________")
    print("| 4.-      eliminar        |")
    print("____________________________")
    opc = int(input("Opcion a elegir: ")) 
    
    if opc == 1:
      apiUrl = "http://otmintegs.sytes.net:9000/MusicApi/listaInterprete.php"
      resp = requests.get(apiUrl)
      if not resp.status_code == 200:
        raise Exception("Algo ha salido mal. Error: {}. Resumen: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)

    if opc == 2:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/altaInterprete.php"
      numinterprete = input("ID de interprete: ")
      nom = input("Ingrese el nombre: ")
      pic = input("Ingrese el link de la fotito: ")
      data={
        "idinterprete" : numinterprete,
        "nombreinterprete" : nom,
        "fotointerprete" : pic
      }
      resp = requests.post( apiUri, data = data )
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del  API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = xml.parse(resp.text)
      print(" Response Data:") 
      print( json.dumps(xm, indent = 4)) 

    if opc == 3:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/modificaInterprete.php"
      numinterprete = input("ID del interprete a actualizar: ")
      nom = input("Nombre del interprete: ")
      pic = input("Ingrese el link de la fotito: ")
      data={
        "idinterprete" : numinterprete,
        "nombreinterprete" : nom,
        "fotointerprete" : pic
      }
      resp = requests.post( apiUri, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)
    
    if opc == 4:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/eliminaInterprete.php"
      numinterprete = input("ID del interprete que eliminara: ")
      data={
        "idinterprete" : numinterprete,
      }
      resp = requests.post( apiUri, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)
