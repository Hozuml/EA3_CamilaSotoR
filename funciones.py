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
def editarJson(UsuarioID:int):
    with open("biblioteca.json", mode="w") as editarJson:
        leerJson=json.dump(editarJson)
#ELIMINAR USUARIO
def eliminarUsuario(UsuarioID:int):
    with open("biblioteca.json", mode="r") as eliminarJson:
        leerJson=json.load(eliminarJson)
    for Usuario in (leerJson["Usuario"]):
        if Usuario["ID"] == UsuarioID:
            leerJson["UsuarioID"].pop
