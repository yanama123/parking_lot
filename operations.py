from .constants import PARKING_LOT, DATA


def create_parking_lot(n):
    """

    :param n: number of slots
    :return:
    """
    for i in range(n):
        PARKING_LOT[i + 1] = False
    print(f"Created a parking lot with {n} slots")


def park_vehicle(arguments):
    """

    :param arguments: arguments contains reg no and color of a vehicle
    :return:
    """
    registration_number = arguments[0]
    color = arguments[1]
    slot = 0
    for i in PARKING_LOT.keys():
        if PARKING_LOT[i] is False:
            PARKING_LOT[i] = True
            slot = i
            break

    if slot == 0:
        print("Sorry, parking lot is full")
        return

    DATA[slot] = dict(registration_number=registration_number, color=color)
    print(f"Allocated slot number: {slot}")


def exit_vehicle(slot):
    """

    :param slot: slot number to be exited
    :return:
    """
    if slot in PARKING_LOT:
        if PARKING_LOT[slot] is True:
            PARKING_LOT[slot] = False
        print(f"Slot number {slot} is free")


def seek_vehicle(number):
    """

    :param number: slot number to be check the status
    :return:
    """
    print("Slot No.\tRegistration No.\tColor")
    for slot in PARKING_LOT:
        if slot == number:
            print(f"{slot}\t\t{DATA[slot]['registration_number']}\t\t{DATA[slot]['color']}")
            break

