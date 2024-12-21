# Agenda realizada con programación funcional
# Es decir, se basa en la utilización de funciones

def mostrar_menu():
    print("\n--- AGENDA DE CONTACTOS: ---")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

# Generamos la función para AGREGAR un contacto
def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el teléfono del contacto:")
    email = input("Por favor introduzca el email del contacto:")
    # Generamos una lista o array, cuya KEY va a ser el nombre
    # Y los valores se guardarán en otro diccionario 
    agenda[nombre] = { "telefono": telefono, "email": email}
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

# Generamos la función para ELIMINAR un contacto
def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        # Puesto que nombre es la KEY de los datos, 
        # se eliminarán todos los que tenga asociados
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

# Generamos la función para BUSCAR un contacto
def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que está buscando: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}")
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

# Generamos la función para LISTAR los contactos
def listar_contactos(agenda):
    if agenda:
        print("\nLista de contactos: ")
        for nombre,info in agenda.items():
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            # para separar, le indicamos que escriba "-" 20 veces
            print("-" * 20)
    else:
        print("La agenda aún está vacía")


# CREAMOS UN DICCIONARIO PARA CONTROLAR LAS ACCIONES
def agenda_contactos():
    agenda = {}

    while True:
        mostrar_menu()
        opcion = input("Por favor elija una opción: ")
        print("\n")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta luego!")
            break
        else:
            print("Por favor seleccione una opción válida (del 1 al 5)")

agenda_contactos()