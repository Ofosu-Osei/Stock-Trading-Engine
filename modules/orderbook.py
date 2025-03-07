import threading
from .order import Order
from lockfree_counter import lib
import logging

"""
Module: orderbook

This module provides the OrderBook class for managing and matching stock trading orders.
Features include:
    - Maintaining separate, sorted lists for Buy and Sell orders for each ticker.
    - Supporting up to 1,024 unique ticker symbols.
    - Inserting orders in sorted order: Buy orders are sorted in descending order (highest price first),
      while Sell orders are sorted in ascending order (lowest price first).
    - Matching orders by comparing the best (top) Buy order with the best Sell order for each ticker.
    - Handling concurrent modifications via thread-safe mechanisms.

"""

logger = logging.getLogger(__name__)


class OrderBook:
    def __init__(self):

        self.tickers = []
        self.buy_orders = []
        self.sell_orders = []
        self.order_id = lib.create_counter(0)
        self.lock = threading.Lock()  # For thread-safe operations

    def getTickerIndex(self, ticker):
        # Simple linear search to find ticker index
        for idx, _ticker in enumerate(self.tickers):
            if _ticker == ticker:
                return idx
        # If not found and capacity < 1024, add new ticker
        if len(self.tickers) < 1024:
            self.tickers.append(ticker)
            self.buy_orders.append([])  
            self.sell_orders.append([])  
            return len(self.tickers) - 1
        else:
            raise Exception("Ticker capacity reached")

    def addOrder(self, order_type, ticker, quantity, price):
        """
        Adds an order to the order book.
        The order is inserted into the appropriate list in sorted order.
        """
        try:
            with self.lock:  # Ensure thread-safety
                idx = self.getTickerIndex(ticker)
                new_order_id = lib.increment_counter(self.order_id)
                order = Order(order_type, ticker, quantity, price, new_order_id)
                

                if order_type == "Buy":
                    inserted = False
                    orders = self.buy_orders[idx]
                    # Insert order in descending order: highest price first
                    for i in range(len(orders)):
                        if price > orders[i].price:
                            orders.insert(i, order)
                            inserted = True
                            break
                    if not inserted:
                        orders.append(order)
                elif order_type == "Sell":
                    inserted = False
                    orders = self.sell_orders[idx]
                    # Insert order in ascending order: lowest price first
                    for i in range(len(orders)):
                        if price < orders[i].price:
                            orders.insert(i, order)
                            inserted = True
                            break
                    if not inserted:
                        orders.append(order)
                logger.info(f"Order added: {order}")
        except Exception as e:
            logger.error(f"Error adding order: {e}")

    def matchOrdersForTicker(self, idx):
        """
        Matches orders for a specific ticker.
        Executes a trade if the best Buy order's price is >= the best Sell order's price.
        """
        try:
            buy_list = self.buy_orders[idx]
            sell_list = self.sell_orders[idx]
            while buy_list and sell_list:
                best_buy = buy_list[0]
                best_sell = sell_list[0]
                if best_buy.price >= best_sell.price:
                    trade_qty = min(best_buy.quantity, best_sell.quantity)
                    logger.info(
                        f"Trade on {self.tickers[idx]}: {trade_qty} shares at price {best_sell.price} "
                        f"between Buy order {best_buy.order_id} and Sell order {best_sell.order_id}"
                    )

                    best_buy.quantity -= trade_qty
                    best_sell.quantity -= trade_qty

                    if best_buy.quantity == 0:
                        buy_list.pop(0)
                    if best_sell.quantity == 0:
                        sell_list.pop(0)
                else:
                    break
        except Exception as e:
            logger.error(f"Error matching orders for ticker {self.tickers[idx]}: {e}")

    def matchOrders(self):
        """
        Matches orders across all tickers.
        This routine operates in O(n) time relative to the total number of orders.
        """
        try:
            for idx in range(len(self.tickers)):
                self.matchOrdersForTicker(idx)
        except Exception as e:
            logger.error(f"Error during matching orders: {e}")
