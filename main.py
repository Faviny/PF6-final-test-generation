import requests


def dish_fetch(id):

    response = requests.get(
        "https://api-colombia.com/api/v1/TypicalDish"
    )

    platos = response.json()

    for plato in platos:

        if plato["id"] == id:

            return plato


def mostrar_menu():

    response = requests.get(
        "https://api-colombia.com/api/v1/TypicalDish"
    )

    platos = response.json()

    print("\n===== PLATOS TÍPICOS COLOMBIANOS =====\n")

    for plato in platos[:10]:

        print(plato["id"], "-", plato["name"])

    opcion = int(input("\nSeleccione un plato: "))

    plato = dish_fetch(opcion)

    if plato:

        print("\n" + "*" * 20)

        print("Nombre:", plato["name"])

        print("Descripción:", plato["description"])

    else:

        print("Opción inválida")


def main():

    mostrar_menu()


if __name__ == "__main__":
    main()