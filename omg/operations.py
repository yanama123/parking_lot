LOT = {}
DATA = {}
# R_NO_COLOR = {}
# SLOT_NO_REG = {}
# SLOT_NO_COLOR = {}


def create_parking_lot(n):
    for i in range(n):
        LOT[i + 1] = False
    print(f"Created a parking lot with {n} slots")


def park(args):
    registration_number = args[0]
    color = args[1]
    slot = 0
    for i in LOT.keys():
        if LOT[i] is False:
            LOT[i] = True
            slot = i
            break

    if slot == 0:
        print("Sorry, parking lot is full")
        return

    DATA[slot] = dict(registration_number=registration_number, color=color)
    print(f"Allocated slot number: {slot}")


# def leave(slot):
#     if slot in LOT:
#         if LOT[slot] is True:
#             LOT[slot] = False
#
#         registration_number = DATA[slot]['registration_number']
#         color = DATA[slot]['color']
#
#         if color in R_NO_COLOR:
#             R_NO_COLOR[color].remove(registration_number)
#
#         if registration_number in SLOT_NO_REG:
#             SLOT_NO_REG.pop(registration_number)
#
#         if color in SLOT_NO_COLOR:
#             SLOT_NO_COLOR[color].remove(slot)
#
#         print(f"Slot number {slot} is free")


def status():
    print("Slot No.\tRegistration No.\tColor")
    for slot in LOT:
        if LOT[slot] is True:
            print(f"{slot}\t\t{DATA[slot]['registration_number']}\t\t{DATA[slot]['color']}")


def status_with_slot(number):
    print("Slot No.\tRegistration No.\tColor")
    for slot in LOT:
        if slot == number:
            print(f"{slot}\t\t{DATA[slot]['registration_number']}\t\t{DATA[slot]['color']}")
            break

