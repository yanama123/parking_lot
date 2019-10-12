# importing the required modules
import os
import argparse
__path__ = [os.path.dirname(os.path.abspath(__file__))]
from .operations import create_parking_lot, park, status

class Driver:
    def __init__(self):
        pass

    def main(self):
        # create parser object
        parser = argparse.ArgumentParser(description="Parking Lot!")

        # defining arguments for parser object
        parser.add_argument("-cr", "--create_parking_lot", type=int,
                            metavar="Create parking lot", default=None,
                            help="Given n number of slots, create a parking slot.")

        parser.add_argument("-park", "--park", type=str, nargs=2,
                            metavar="Park a vehicle with given registration number", default=None,
                            help="Park a vehicle with given registration number.")

        parser.add_argument("-seek", "--seek", type=int,
                            metavar="Details of the car parked in the slot", default=None,
                            help="Details of the car parked in the slot.")

        # parse the arguments from standard input
        args = parser.parse_args()

        # calling functions depending on type of argument
        if args.create_parking_lot is not None:
            print('args number', args.create_parking_lot)
            create_parking_lot(args.create_parking_lot)
        elif args.park is not None:
            print('args', args.park)
            park(args.park)
        elif args.seek is not None:
            print('args', args.seek)
            status()



if __name__ == '__main__':
    obj = Driver()
    obj.main()
