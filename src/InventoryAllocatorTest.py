import unittest
from InventoryAllocator import *


class InventoryAllocatorTest(unittest.TestCase):

    def test_one_warehouse(self):  # Test to check in a single warehouse
        # p1 = Product("apple", "5")
        # p2 = Product("banana", "7")
        i1 = InventoryAllocator()
        result = i1.calculate_cheapest_shipment({"Banana": 1}, [
            {"name": 'owd', "inventory": {"apple": 1}},
            {"name": 'dm', "inventory": {"apple": 2, "Banana": 2}}
        ])
        self.assertEqual(result, ['{ dm : { Banana : 2 }}'])

    def test_zero_order(self):  # Test to check if there are orders with empty count
        input1 = {"apple": 0}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'Banana': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 3, 'mango': 2}}]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2), "No allocation")

    def test_multiple_orders(self):  # Test to check multiple orders in inventories
        input1 = {"apple": 2, "mango": 2}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'Banana': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 3, 'mango': 2}}]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2),
                         ['{ dm : { apple : 2 }}', '{ pdm : { mango : 2 }}'])

    def test_insufficientInventory(self):  # Test to check if the're not enough orders in the inventory
        input1 = {"apple": 7}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'Banana': 2}}]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2), "No allocation")

    def test_multipleWarehouses(self):  # Test to check in multiple warehouses
        input1 = {"apple": 4}
        input2 = [{'name': 'dm', 'inventory': {'apple': 4, 'Banana': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 4, 'mango': 2}}]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2),
                         ['{ dm : { apple : 4 }}'])

    def test_split_multipleWarehouses(self):  # Test to split an order across multiple warehouses if needed
        input1 = {"mango": 2, "apple": 6}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'mangO': 2, "ban": 6}},
                  {'name': 'odm', 'inventory': {'apple': 2, 'mango': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 3, 'mango': 3}}
                  ]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2),
                         ['{ odm : { mango : 2 }}', ['{ dm : { apple : 2 }}', '{ odm : { apple : 2 }}', '{ pdm : { apple : 3 }}']])

    def test_incorrect_unavailable_orders(
            self):  # Test to return no allocation if the orders are incorrect or unavailable
        input1 = {"app": 7, "ban": 6}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'Banana': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 3, 'mango': 2}}]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2), "No allocation")

    def test_case_sensitivity(self):  # Test to check if the orders are case sensitive
        input1 = {"APPLE": 1, "mango": 2}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'Banana': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 3, 'mango': 2}}]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2),
                         ['{ pdm : { mango : 2 }}'])

    def test_ship_completely_onewarehouse(self):  # Test to ship the order completely from one warehouse instead of shipping from multiple warehouses
        input1 = {"mango": 2, "apple": 6}
        input2 = [{'name': 'dm', 'inventory': {'apple': 2, 'mangO': 2, "ban": 6}},
                  {'name': 'odm', 'inventory': {'apple': 2, 'mango': 2}},
                  {'name': 'pdm', 'inventory': {'apple': 3, 'mango': 3}},
                  {'name': 'mdm', 'inventory': {'apple': 7, 'mango': 3}}
                  ]
        i1 = InventoryAllocator()
        self.assertEqual(i1.calculate_cheapest_shipment(input1, input2),
                         ['{ odm : { mango : 2 }}', '{ mdm : { apple : 7 }}'])


if __name__ == '__main__':
    unittest.main()
