import logging as logger
import sys
import os
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from os.path import dirname, abspath
from .operations import park_vehicle, create_parking_lot, seek_vehicle, exit_vehicle

current_dir = dirname(dirname(abspath(__file__)))

sys.path.append(current_dir)


def main():
    print("################## START #####################")

    while True:
        option = input("""Please choose one option from following:
        1.	create_parking_lot
        2.	park_vehicle (<----- IN)
        3.	seek_vehicle
        4.      exit_vehicle (-----> OUT)
        5.      terminate programme
        """)

        if int(option) == 1:
            print("################ create_parking_lot ##################")
            print('You have selected Create_parking_lot  option')
            number = int(input('Enter number of slots: '))
            print('Entered slots are {} '.format(number))
            create_parking_lot(number)
            continue

        elif int(option) == 2:
            print("#################### park_vehicle ###################")
            print("You have selected Park option \n")
            n = 2
            list1 = list(map(str, input('Enter vehicle reg no and color: ').strip().split()))[:n]
            park_vehicle(list1)
            continue

        elif int(option) == 3:
            print("################# seek_vehicle ######################")
            print("You have selected seek_vehicle option \n")
            # status()
            slot = int(input('Slot number: '))
            seek_vehicle(slot)
            continue

        elif int(option) == 4:
            print("################## exit_vehicle ####################")
            print("You have selected exit_vehicle option \n")
            slot = int(input('Slot number: '))
            exit_vehicle(slot)
            continue

        elif int(option) == 5:
            print("################## terminate programme ####################")
            print("You have selected terminate programme option \n")
            print('Programme terminated')
            break

        else:
            print('Sorry, that was incorrect input')
            continue


if __name__ == '__main__':
    main()
