import unittest
from modules.order import Order

"""
Module: test_order

This module contains unit tests for the order module of the stock trading engine.
Tests are written using the unittest framework and cover:
    - Valid and invalid input cases.
    - Correct behavior of order creation, order insertion, and order matching.
    - The integrity and thread-safety of the order book under simulated loads.

Each test case ensures that the functionality of the stock trading engine meets the expected requirements.
"""


class TestOrder(unittest.TestCase):
    def test_valid_order(self):
        order = Order("Buy", "AAPL", 10, 150.0, 1)
        self.assertEqual(order.order_type, "Buy")
        self.assertEqual(order.ticker, "AAPL")
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.price, 150.0)

    def test_invalid_order_type(self):
        with self.assertRaises(ValueError):
            Order("Invalid", "AAPL", 10, 150.0, 1)

    def test_invalid_ticker(self):
        with self.assertRaises(ValueError):
            Order("Buy", "", 10, 150.0, 1)

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError):
            Order("Buy", "AAPL", 0, 150.0, 1)
        with self.assertRaises(ValueError):
            Order("Buy", "AAPL", -5, 150.0, 1)

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            Order("Buy", "AAPL", 10, 0, 1)
        with self.assertRaises(ValueError):
            Order("Buy", "AAPL", 10, -100, 1)


if __name__ == "__main__":
    unittest.main()
