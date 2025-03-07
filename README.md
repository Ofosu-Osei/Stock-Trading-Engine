# Stock-Trading-Engine
A real-time stock trading engine built in Python that matches buy and sell orders across multiple tickers. With a modular design, it manages and simulates orders, integrating a lock-free counter implemented in C (via CFFI) for unique order ID generation.


## Installation
1. Clone the Repository:
```bash
git clone https://github.com/Ofosu-Osei/Stock-Trading-Engine
cd Stock-Trading-Engine
```
2. Create and Activate a Virtual Environment:
```bash
python -m venv .venv
source .venv/bin/activate    # On macOS/Linux
.venv\Scripts\activate       # On Windows
```
3. Install Dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```
4. Build the Lock-Free Extension
```bash
python c_ext/build_lockfree.py
```
This step compiles the C code and generates a .so file, making it importable as lockfree_counter.

## Usage
1. Run the Main Application
```bash
python app.py
```
**This will:**
- Initialize the OrderBook.
- Simulate orders (single-threaded or multi-threaded).
- Match orders and print trades to the console or logs.

2. Customize Simulation
**Edit the simulateOrders or simulateMultiThreadedOrders functions in modules/simulation.py to control:**
- Number of orders
- Ticker symbols
- Price ranges
- Concurrency levels

## Testing
**To run the unit tests locally:**
```bash
python -m unittest discover -s tests
```
- test_order.py checks the Order class (input validation, etc.).
- test_orderbook.py validates the logic for adding and matching orders.
- test_simulation.py tests order generation and concurrency.

