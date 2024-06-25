import json

with open("biblioteca.json" , mode="r") as archivoJson:
    leerJson = json.load(archivoJson)
    Usuario={
        "UsuarioID": len(leerJson["Usuario"])+1,
        "Nombre": "Camila Soto",
        "Email": "lalala123@yahoo.com",
        "FechaRegistro": "2024-06-25"
        }
    leerJson["Usuario"].append(Usuario)

with open("biblioteca.json", mode="w") as archivoJson:
    json.dump(leerJson,archivoJson, indent=4)

# EDITAR USUARIO with open("biblioteca.json", mode="w") as archivoJson:

#ELIMINAR USUARIO
