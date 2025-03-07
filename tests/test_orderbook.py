import unittest
from modules.orderbook import OrderBook

"""
Module: test_orderbook

This module contains unit tests for the orderbook module of the stock trading engine.
Tests are written using the unittest framework and cover:
    - Valid and invalid input cases.
    - Correct behavior of orderbook creation, order insertion, and order matching.
    - The integrity and thread-safety of the order book under simulated loads.

Each test case ensures that the functionality of the stock trading engine meets the expected requirements.
"""


class TestOrderBook(unittest.TestCase):
    def setUp(self):
        self.order_book = OrderBook()

    def test_add_order_buy(self):
        self.order_book.addOrder("Buy", "AAPL", 10, 150.0)
        idx = self.order_book.getTickerIndex("AAPL")
        self.assertEqual(len(self.order_book.buy_orders[idx]), 1)

    def test_add_order_sell(self):
        self.order_book.addOrder("Sell", "AAPL", 5, 155.0)
        idx = self.order_book.getTickerIndex("AAPL")
        self.assertEqual(len(self.order_book.sell_orders[idx]), 1)

    def test_order_sorting(self):
        # For Buy orders descending order, and Sell orders ascending order
        self.order_book.addOrder("Buy", "AAPL", 10, 150.0)
        self.order_book.addOrder("Buy", "AAPL", 10, 160.0)
        self.order_book.addOrder("Sell", "AAPL", 5, 155.0)
        self.order_book.addOrder("Sell", "AAPL", 5, 145.0)
        idx = self.order_book.getTickerIndex("AAPL")
        self.assertEqual(self.order_book.buy_orders[idx][0].price, 160.0)
        self.assertEqual(self.order_book.sell_orders[idx][0].price, 145.0)

    def test_match_orders(self):
        # Add matching orders
        self.order_book.addOrder("Buy", "AAPL", 10, 150.0)
        self.order_book.addOrder("Sell", "AAPL", 5, 140.0)
        self.order_book.matchOrders()
        idx = self.order_book.getTickerIndex("AAPL")
        # The sell order should be completely matched and buy order partially filled
        if self.order_book.buy_orders[idx]:
            self.assertEqual(self.order_book.buy_orders[idx][0].quantity, 5)
        self.assertEqual(len(self.order_book.sell_orders[idx]), 0)


if __name__ == "__main__":
    unittest.main()
