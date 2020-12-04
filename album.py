import requests
import json
import urllib3
import xmltodict as xml

opc = 0 
while opc != 5: 
    print("____________________________") 
    print("| 1.-   Enlistar Album     |")
    print("____________________________")
    print("| 2.-    agregar Album     |")
    print("____________________________")
    print("| 3.-    modificar Album   |")
    print("____________________________")
    print("| 4.-    eliminar Album    |")
    print("____________________________")
    opc = int(input("Opcion a elegir: ")) 
    
    if opc == 1:
      apiUrl = "http://otmintegs.sytes.net:9000/MusicApi/listaAlbum.php"
      resp = requests.get(apiUrl)
      if not resp.status_code == 200:
        raise Exception("Algo ha salido mal. Error: {}. Resumen: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)

    if opc == 2:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/altaAlbum.php"
      idalbum = input ("Id del album: ")
      nomalbum = input ("Nombre del album: ")
      numinterprete = input("ID de interprete: ")
      anio = input("Año de Publicacion: ")
      pic = input("Ingrese el link de la fotito: ")
      data={
        "idalbum" : idalbum,
        "nombrealbum" : nomalbum,
        "idinterprete" : numinterprete,
        "aniopublicacion" : anio,
        "fotoalbum" : pic

      }
      resp = requests.post( apiUri, data = data )
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del  API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = xml.parse(resp.text)
      print(" Response Data:") 
      print( json.dumps(xm, indent = 4)) 

    if opc == 3:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/modificaAlbum.php"
      idalbum = input ("Id del album: ")
      nomalbum = input ("Nombre del album: ")
      numinterprete = input("ID de interprete: ")
      anio = input("Año de Publicacion: ")
      pic = input("Ingrese el link de la fotito: ")
      data={
        "idalbum" : idalbum,
        "nombrealbum" : nomalbum,
        "idinterprete" : numinterprete,
        "aniopublicacion" : anio,
        "fotoalbum" : pic

      }
      resp = requests.post( apiUri, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)
    
    if opc == 4:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/eliminaAlbum.php"
      idalbum = input("ID del Album que eliminara: ")
      data={
        "idalbum" : idalbum,
      }
      resp = requests.post( apiUri, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)


