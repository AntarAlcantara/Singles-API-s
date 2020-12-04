import requests
import json
import urllib3
import xmltodict as xml

opc = 0 
while opc != 5: 
    print("____________________________") 
    print("| 1.-  Enlistar Roliuxs  |")
    print("____________________________")
    print("| 2.-   agregar Rolita     |")
    print("____________________________")
    print("| 3.-   modificar rolita   |")
    print("____________________________")
    print("| 4.-  eliminar Rolita :c  |")
    print("____________________________")
    opc = int(input("Opcion a elegir: ")) 
    
    if opc == 1:
      apiUrl = "http://otmintegs.sytes.net:9000/MusicApi/listaCancion.php"
      resp = requests.get(apiUrl)
      if not resp.status_code == 200:
        raise Exception("Algo ha salido mal. Error: {}. Resumen: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)

    if opc == 2:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/altaCancion.php"
      idcancion = input ("ID de la Roliux: ")
      idalbum = input ("ID del album: ")
      nombrecancion = input("Nombre de la Rolita: ")
      duracion = input("Cuanto dura? (La Cancion): ")
      data={
        "idcancion" : idcancion,
        "idalbum" : idalbum,
        "nombrecancion" : nombrecancion,
        "duracion" : duracion

      }
      resp = requests.post( apiUri, data = data )
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del  API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = xml.parse(resp.text)
      print(" Response Data:") 
      print( json.dumps(xm, indent = 4)) 

    if opc == 3:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/modificaCancion.php"
      idcancion = input ("ID de la Roliux: ")
      idalbum = input ("ID del album: ")
      nombrecancion = input("Nombre de la Rolita: ")
      duracion = input("Cuanto dura? (La Cancion): ")
      data={
        "idcancion" : idcancion,
        "idalbum" : idalbum,
        "nombrecancion" : nombrecancion,
        "duracion" : duracion

      }
      resp = requests.post( apiUri, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)
    
    if opc == 4:
      apiUri = "http://otmintegs.sytes.net:9000/MusicApi/eliminaCancion.php"
      idcancion = input("ID de la Rolita que eliminara: ")
      data={
        "idcancion" : idcancion,
      }
      resp = requests.post( apiUri, data = data)
      if not resp.status_code == 200:
        raise Exception("Respuesta incorrecta del API. Status code: {}. Text: {}".format(resp.status_code, resp.text))
      xm = resp.content
      print(xm)
