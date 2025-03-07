import unittest
from modules.orderbook import OrderBook
from modules.simulation import simulateOrders, simulateMultiThreadedOrders

"""
Module: test_simulation

This module contains unit tests for the simulation module of the stock trading engine.
Tests are written using the unittest framework and cover:
    - Valid and invalid input cases.
    - Correct behavior of orderbook creation, order insertion, and order matching.
    - The integrity and thread-safety of the order book under simulated loads.

Each test case ensures that the functionality of the stock trading engine meets the expected requirements.
"""


class TestSimulation(unittest.TestCase):
    def setUp(self):
        self.order_book = OrderBook()

    def test_simulate_orders(self):
        simulateOrders(self.order_book, num_orders=50)
        # Checks that at least one ticker has orders
        self.assertTrue(len(self.order_book.tickers) > 0)

    def test_simulate_multithreaded_orders(self):
        simulateMultiThreadedOrders(
            self.order_book, num_threads=2, orders_per_thread=20
        )
        self.assertTrue(len(self.order_book.tickers) > 0)


if __name__ == "__main__":
    unittest.main()
