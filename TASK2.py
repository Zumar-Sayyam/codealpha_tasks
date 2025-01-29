class StockPortfolio:
    def __init__(self):
        self.portfolio = {}
        self.mock_prices = {
            "AAPL": 150.25,
            "GOOGL": 2800.75,
            "AMZN": 3450.60,
            "TSLA": 720.50,
            "MSFT": 299.99
        }

    def add_stock(self, symbol, shares):
        """Add a stock to the portfolio."""
        if not symbol.isalpha() or len(symbol) < 1:  # Ensures the symbol contains only letters and isn't empty
            print(f"Invalid stock symbol: {symbol}. Symbols should only contain letters.")
            return
        if symbol not in self.mock_prices:
            print(f"Invalid stock symbol: {symbol}. Please enter a valid symbol.")
            return
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol} to your portfolio.")

    def remove_stock(self, symbol, shares):
        """Remove a stock from the portfolio."""
        if symbol not in self.portfolio:
            print(f"Stock {symbol} is not in your portfolio.")
            return
        if shares >= self.portfolio[symbol]:
            self.portfolio.pop(symbol)
            print(f"Removed all shares of {symbol} from your portfolio.")
        else:
            self.portfolio[symbol] -= shares
            print(f"Removed {shares} shares of {symbol} from your portfolio.")

    def fetch_stock_price(self, symbol):
        """Fetch the mock stock price."""
        price = self.mock_prices.get(symbol)
        if price is not None:
            return price
        else:
            print(f"Could not fetch data for {symbol}. Check if the symbol is correct.")
            return None

    def portfolio_value(self):
        """Calculate the total value of the portfolio."""
        total_value = 0.0
        invalid_symbol = False  # Flag to track invalid symbols
        for symbol, shares in self.portfolio.items():
            price = self.fetch_stock_price(symbol)
            if price is None:  # If any stock symbol is invalid
                invalid_symbol = True
            else:
                total_value += price * shares
                print(f"{symbol}: {shares} shares @ ${price:.2f} per share")

        if invalid_symbol:
            print("\nSome stock symbols were invalid. Please correct them before viewing the total portfolio value.")
        else:
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")


if __name__ == "__main__":
    portfolio = StockPortfolio()

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio Value")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            portfolio.add_stock(symbol, shares)

        elif choice == "2":
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            portfolio.remove_stock(symbol, shares)

        elif choice == "3":
            portfolio.portfolio_value()

        elif choice == "4":
            print("Exiting portfolio tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

