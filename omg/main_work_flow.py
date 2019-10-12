import logging as logger
import sys
import os
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from os.path import dirname, abspath, join, exists
from argparse import ArgumentParser
from time import sleep
from .operations import status, park, create_parking_lot, status_with_slot

current_dir = dirname(dirname(abspath(__file__)))

sys.path.append(current_dir)


def main():
    print("###############START#########################")

    while True:
        option = input("""Please choose one option from following:
        1.	Create_parking_lot
        2.	Park
        3.	Seek
        4.      Exit
        """)

        if int(option) == 1:
            print("################Create_parking_lot##################")
            print('You have selected Create_parking_lot  option')
            number = int(input('Enter number of slots: '))
            print('Entered slots are {} '.format(number))
            create_parking_lot(number)
            continue

        elif int(option) == 2:
            print("####################Park###################")
            print("You have selected Park option \n")
            n = 2
            list1 = list(map(str, input('Enter vehicle reg no and color: ').strip().split()))[:n]
            park(list1)
            continue

        elif int(option) == 3:
            print("###############seek#########################")
            print("You have selected Seek option \n")
            # status()
            slot = int(input('Slot number: '))
            status_with_slot(slot)
            continue

        elif int(option) == 4:
            print("##################Exit####################")
            print("You have selected Exit option \n")
            print('Exited from programme')
            break

        else:
            print('Sorry, that was incorrect input')
            continue


if __name__ == '__main__':
    parser = ArgumentParser(description='Arguments for parking lot')
    args = parser.parse_args()
    main()
