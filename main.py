import json


def dish_fetch(id):

    datos_json = """
    [
        {
            "id": 1,
            "name": "Bandeja Paisa",
            "region": "Antioquia"
        },

        {
            "id": 5,
            "name": "Ajiaco",
            "region": "Bogotá"
        },

        {
            "id": 15,
            "name": "Lechona",
            "region": "Tolima"
        }
    ]
    """

    platos = json.loads(datos_json)

    for plato in platos:

        if plato["id"] == id:

            return plato


def mostrar_menu():

    print("\n===== PLATOS TÍPICOS COLOMBIANOS =====\n")

    print("1 - Bandeja Paisa")
    print("5 - Ajiaco")
    print("15 - Lechona")

    opcion = int(input("\nSeleccione un plato: "))

    plato = dish_fetch(opcion)

    if plato:

        print("\n" + "*" * 20)

        print("Nombre:", plato["name"])
        print("Región:", plato["region"])

    else:

        print("Opción inválida")


def main():

    mostrar_menu()


if __name__ == "__main__":
    main()