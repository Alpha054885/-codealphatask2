"""
====================================================================
PROJECT: Stock Portfolio Tracker
Author: Python Programming Intern
Task: Python Programming Internship - Task 2
Description:
    A console-based Python application that calculates the total
    investment value of a stock portfolio based on predefined
    stock prices and user-provided quantities. Demonstrates basic
    Python concepts including dictionaries, loops, functions,
    exception handling, and file operations.
====================================================================
"""

import os

# -------------------------------------------------------------------
# Predefined Stock Prices (Sample market data)
# -------------------------------------------------------------------
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 200
}

REPORT_FILENAME = "portfolio_report.txt"


def display_welcome():
    """Display a friendly welcome banner for the application."""
    print("\n" + "=" * 55)
    print("       WELCOME TO STOCK PORTFOLIO TRACKER")
    print("=" * 55)
    print("Track your stock investments easily and generate reports!")
    print("-" * 55)


def display_available_stocks(prices_dict):
    """
    Display available stocks and their predefined sample prices
    in a neatly formatted table.
    """
    print("\n[AVAILABLE STOCKS & SAMPLE PRICES]")
    print("-" * 35)
    print(f"{'Stock Symbol':<18} | {'Price per Share':<15}")
    print("-" * 35)
    for symbol, price in prices_dict.items():
        print(f"{symbol:<18} | ${price:<14.2f}")
    print("-" * 35)


def get_number_of_stocks(max_available):
    """
    Ask the user how many different stocks they want to add.
    Validates that the input is a positive whole number between 1 and max_available.
    """
    while True:
        user_input = input(f"\nHow many different stocks do you want to add (1 to {max_available})? ").strip()
        try:
            count = int(user_input)
            if 1 <= count <= max_available:
                return count
            elif count <= 0:
                print(">> [Error] Please enter a positive number greater than 0.")
            else:
                print(f">> [Error] You can select at most {max_available} different stocks.")
        except ValueError:
            print(">> [Error] Invalid input! Please enter a valid whole number.")


def get_stock_name(prices_dict, already_selected):
    """
    Prompt the user to enter a stock name.
    Accepts uppercase and lowercase inputs, validates against the predefined dictionary,
    and prevents duplicate selection in the same session.
    """
    while True:
        symbol = input("Enter stock symbol: ").strip().upper()

        if not symbol:
            print(">> [Error] Stock symbol cannot be empty. Please try again.")
            continue

        if symbol not in prices_dict:
            print(f">> [Error] '{symbol}' is not available in our list. Please choose from: {', '.join(prices_dict.keys())}")
            continue

        if symbol in already_selected:
            print(f">> [Error] You have already added '{symbol}'. Please select a different stock.")
            continue

        return symbol


def get_stock_quantity(symbol):
    """
    Prompt the user to enter the quantity purchased for a given stock.
    Validates that the input is a positive whole number (integer > 0).
    """
    while True:
        qty_input = input(f"Enter quantity for {symbol}: ").strip()
        try:
            qty = int(qty_input)
            if qty > 0:
                return qty
            elif qty == 0:
                print(">> [Error] Quantity cannot be zero. Please enter a positive number.")
            else:
                print(">> [Error] Quantity cannot be negative. Please enter a positive number.")
        except ValueError:
            print(">> [Error] Invalid quantity! Please enter a positive whole number (e.g., 1, 5, 10).")


def build_portfolio(prices_dict):
    """
    Collect stock selections and quantities from the user.
    Returns a list of dictionaries with stock details.
    """
    num_stocks = get_number_of_stocks(len(prices_dict))
    portfolio = []
    selected_symbols = set()

    print(f"\nPlease enter details for {num_stocks} stock(s):")
    for i in range(1, num_stocks + 1):
        print(f"\n--- Stock {i} of {num_stocks} ---")
        symbol = get_stock_name(prices_dict, selected_symbols)
        quantity = get_stock_quantity(symbol)

        price = prices_dict[symbol]
        investment = price * quantity

        selected_symbols.add(symbol)
        portfolio.append({
            "symbol": symbol,
            "price": price,
            "quantity": quantity,
            "investment": investment
        })

    return portfolio


def calculate_total_investment(portfolio):
    """Calculate the grand total investment across all stocks in the portfolio."""
    total = sum(item["investment"] for item in portfolio)
    return total


def format_portfolio_report(portfolio, total_investment):
    """
    Create a clean, formatted text string representing the portfolio summary report.
    Used for both console output and saving to file.
    """
    lines = []
    lines.append("=" * 62)
    lines.append("                 STOCK PORTFOLIO SUMMARY")
    lines.append("=" * 62)
    lines.append(f"{'Stock Name':<12} | {'Price ($)':<12} | {'Quantity':<10} | {'Investment ($)':<15}")
    lines.append("-" * 62)

    for item in portfolio:
        lines.append(
            f"{item['symbol']:<12} | "
            f"${item['price']:<11.2f} | "
            f"{item['quantity']:<10} | "
            f"${item['investment']:<14.2f}"
        )

    lines.append("-" * 62)
    lines.append(f"{'GRAND TOTAL INVESTMENT:':<38} | ${total_investment:<14.2f}")
    lines.append("=" * 62)

    return "\n".join(lines)


def display_portfolio_summary(portfolio, total_investment):
    """Display the portfolio report on the console."""
    print("\n" + format_portfolio_report(portfolio, total_investment))


def save_portfolio_report(portfolio, total_investment, filename=REPORT_FILENAME):
    """
    Save the portfolio report into a text file using basic file handling.
    Catches and handles file I/O errors gracefully.
    """
    report_content = format_portfolio_report(portfolio, total_investment)
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(report_content + "\n")
            file.write("\nReport generated successfully by Stock Portfolio Tracker.\n")
        print(f"\n[Success] Portfolio report has been successfully saved to '{filename}'.")
    except IOError as e:
        print(f"\n>> [Error] Failed to save portfolio report: {e}")


def ask_to_continue():
    """
    Ask the user whether they want to calculate another portfolio.
    Returns True to restart, False to exit.
    """
    while True:
        choice = input("\nDo you want to calculate another portfolio? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print(">> [Error] Invalid choice! Please type 'yes' or 'no'.")


def main():
    """Main program execution loop."""
    display_welcome()

    while True:
        # Step 1: Display available stocks
        display_available_stocks(STOCK_PRICES)

        # Step 2 & 3: Get user input and build portfolio
        portfolio = build_portfolio(STOCK_PRICES)

        # Step 4: Calculate total investment
        total_investment = calculate_total_investment(portfolio)

        # Step 5: Display portfolio summary
        display_portfolio_summary(portfolio, total_investment)

        # Step 6: Save summary to file
        save_portfolio_report(portfolio, total_investment, REPORT_FILENAME)

        # Step 7: Ask to continue or exit
        if not ask_to_continue():
            print("\n" + "=" * 55)
            print("Thank you for using Stock Portfolio Tracker. Goodbye!")
            print("=" * 55 + "\n")
            break


if __name__ == "__main__":
    main()
