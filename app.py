from modules.orderbook import OrderBook
from modules.simulation import simulateOrders, simulateMultiThreadedOrders
from modules.logging_config import setup_logging
import logging

"""
Module: main

This module serves as the entry point for the stock trading engine application.
It performs the following actions:
    - Initializes an instance of the OrderBook.
    - Runs simulations to generate random orders (both single-threaded and multi-threaded).
    - Invokes the order matching process to execute trades based on matching criteria.
    - Demonstrates the integration of order creation, order management, and order matching.

"""
setup_logging(log_to_file=True, log_file="logs/app.log", log_level=logging.DEBUG)
logger = logging.getLogger(__name__)


def main():
    try:
        logger.info("Starting the stock trading engine.")
        # First, we create an instance of the order book
        order_book = OrderBook()

        # Simulate orders in a single-threaded manner
        simulateOrders(order_book, num_orders=100)

        # Simulate concurrent order additions from multiple threads
        simulateMultiThreadedOrders(order_book, num_threads=4, orders_per_thread=50)

        # And then we attempt to match orders across all tickers
        order_book.matchOrders()
    except Exception as e:
        logger.error(f"Error in main execution: {e}")


if __name__ == "__main__":
    main()
