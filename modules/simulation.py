import random
import threading
import logging

"""
Module: simulation

This module simulates a live trading environment by generating random orders for the OrderBook.
It provides functions to:
    - Generate random orders (both Buy and Sell) for a set of predefined ticker symbols.
    - Simulate single-threaded order additions.
    - Simulate concurrent order additions using multiple threads.

"""

logger = logging.getLogger(__name__)


def simulateOrders(order_book, num_orders=1000):
    """
    Simulates random order additions to the order book.
    """
    possible_tickers = [
        "AAPL",
        "GOOG",
        "MSFT",
        "AMZN",
        "FB",
        "TSLA",
        "NFLX",
        "NVDA",
        "ONYM",
        "INTC",
    ]
    for _ in range(num_orders):
        try:
            order_type = "Buy" if random.random() < 0.5 else "Sell"
            ticker = random.choice(possible_tickers)
            quantity = random.randint(1, 100)
            price = round(random.uniform(100, 500), 2)
            order_book.addOrder(order_type, ticker, quantity, price)
        except Exception as e:
            logger.error(f"Error in simulateOrders: {e}")


def simulateMultiThreadedOrders(order_book, num_threads=4, orders_per_thread=250):
    """
    Simulates multiple threads concurrently adding orders.
    """
    threads = []

    def thread_function():
        for _ in range(orders_per_thread):
            try:
                order_type = "Buy" if random.random() < 0.5 else "Sell"
                ticker = random.choice(["AAPL", "GOOG", "ONYM", "AMZN", "FB"])
                quantity = random.randint(1, 100)
                price = round(random.uniform(100, 500), 2)
                order_book.addOrder(order_type, ticker, quantity, price)
            except Exception as e:
                logger.error(f"Error in thread order simulation: {e}")

    for _ in range(num_threads):
        t = threading.Thread(target=thread_function)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
