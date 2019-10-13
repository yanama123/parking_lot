import sys
import unittest

from io import StringIO
from unittest.mock import patch
from parking_lot.operations import seek_vehicle, create_parking_lot, exit_vehicle, park_vehicle
from parking_lot.constants import PARKING_LOT, DATA


class ParkingLotTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    @patch.dict(PARKING_LOT, {}, clear=True)
    def test_create_parking_lot(self):
        slots = 4
        expected_output = {1: False,
                           2: False,
                           3: False,
                           4: False,
                           }
        expected_print = "Created a parking lot with {} slots".format(slots)
        create_parking_lot(slots)
        self.assertDictEqual(PARKING_LOT, expected_output)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_print)

    @patch.dict(PARKING_LOT, {}, clear=True)
    def test_create_parking_lot_failure(self):
        slots = 4
        expected_output = {1: False,
                           2: False,
                           3: False,
                           4: False,
                           }
        expected_print = "Created a parking lot with {} slots".format(slots)
        create_parking_lot(slots)
        self.assertDictEqual(PARKING_LOT, expected_output)
        self.assertEqual(sys.stdout.getvalue().strip(), expected_print)

    @patch.dict(PARKING_LOT, {1: True, 2: False, 3: True, 4: False}, clear=True)
    @patch.dict(DATA, {}, clear=True)
    def test_park_vehicle(self):
        arguments = ["KA-53-EU-5172", "Black"]
        park_vehicle(arguments)

        self.assertDictEqual(DATA, {2: {'registration_number': arguments[0], 'color': arguments[1]}})
        self.assertEqual(sys.stdout.getvalue().strip(), "Allocated slot number: 2")

    @patch.dict(PARKING_LOT, {1: True, 2: True}, clear=True)
    @patch.dict(DATA, {1: {'registration_number': "KA-01-HH-1234", 'color': "White"},
                       2: {'registration_number': "KA-01-HH-9999", 'color': "White"}}, clear=True)
    def test_seek_vehicle(self):
        slot = 2

        seek_vehicle(slot)
        self.assertEqual(sys.stdout.getvalue().strip(),
                         "Slot No.\tRegistration No.\tColor\n2\t\tKA-01-HH-9999\t\tWhite")

    @patch.dict(PARKING_LOT, {1: False, 2: True}, clear=True)
    def test_exit_vehicle(self):
        slot = 2

        exit_vehicle(slot)
        self.assertEqual(sys.stdout.getvalue().strip(), "Slot number {} is free".format(slot))


if __name__ == "__main__":
    unittest.main()
