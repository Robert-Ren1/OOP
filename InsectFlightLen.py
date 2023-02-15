import InsectClass as I


def main():
    mosquito = I.Insect('mosquito',2,4)
    housefly = I.Insect('housefly',2,4)

    mosquito.flight_length()
    housefly.flight_length()

    print("The length of Ladybug is going to fly is", mosquito.get_miles())


main()
