import json
print("*************Bienvenido a Mundo Libro! c:*************")
print("                  ***** Menu *****")
print("a) Mantenedor de usuario \t b) Reportes \t c) Salir")

while True:
    opcion=[input(f"Escriba la alternativa del menu que requiera:   ")]
    a=""
    b=""
    c=""
    if a==a:
        print("Ok :D")
        print("1.- Agregar usuario \t 2.- Editar usuario \t 3.- Eliminar usuario \t 4.- Buscar usuario \t 5.- Volver")
        respuesta=[input(f"Ahora escriba el número de la opción que desee:   ")]
        if respuesta==1: #Agregar usuario: Al listado de usuarios existente en el Json, agregamos al final de la lista el nuevo usuario
            print(" Ok!, Agreguemos un usuario ")
            def agregarJson(UsuarioID:int):
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
        elif respuesta==2:
                print("Vamos a editar el usuario! c:")
                def editarJson(UsuarioID:int):
                    with open("biblioteca.json", mode="w") as editarJson:
                        leerJson=json.dump(editarJson)
        elif respuesta==3:
            print("Eliminemos el usuario :c")
            def eliminarUsuario(UsuarioID:int):
                with open("biblioteca.json", mode="r") as eliminarJson:
                    leerJson=json.load(eliminarJson)
                for Usuario in (leerJson["Usuario"]):
                    if Usuario["ID"] == UsuarioID:
                        leerJson["UsuarioID"].pop
        elif respuesta==4:
            print("Busquemos un usuario")
        elif respuesta==5:
            print("Volvamos al menu principal!")
        else:
            break    
    elif b==b:
        print("Ok, veremos los reportes :D")
    else:
        print("Haz escogido salir :C")