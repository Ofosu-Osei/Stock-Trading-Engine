"""
Module: order

This module defines the Order class, which represents an individual order in the stock trading engine.
Each Order instance includes:
    - order_type: a string indicating the type of order ("Buy" or "Sell")
    - ticker: the stock symbol for the order
    - quantity: the number of shares to trade (must be a positive integer)
    - price: the price per share (must be a positive number)
    - order_id: a unique identifier for the order

The Order class validates input parameters to ensure that each order is created with valid attributes.
"""

class Order:
    def __init__(self, order_type, ticker, quantity, price, order_id):
        if order_type not in ["Buy", "Sell"]:
            raise ValueError(f"Invalid order type: {order_type}. Must be 'Buy' or 'Sell'.")
        if not ticker or not isinstance(ticker, str):
            raise ValueError("Ticker symbol cannot be an empty string.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not (isinstance(price, int) or isinstance(price, float)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        self.order_type = order_type
        self.ticker = ticker
        self.quantity = quantity
        self.price = price
        self.order_id = order_id

    def __repr__(self):
        return f"Order({self.order_type}, {self.ticker}, {self.quantity}, {self.price}, {self.order_id})"