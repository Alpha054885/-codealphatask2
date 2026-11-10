# Stock Portfolio Tracker

**Python Programming Internship – Task 2**

A beginner-friendly, console-based Python project that calculates the total investment value of a user's stock portfolio using predefined stock prices and user-entered quantities.

---

## 1. Project Objective

The primary objective of this project is to develop a command-line tool that allows users to:
1. View available stock listings with their predefined sample prices.
2. Select multiple stocks and specify the quantity purchased for each.
3. Validate user inputs (stock names and quantities) to prevent crashes.
4. Calculate individual stock investments and the overall portfolio total.
5. Display a clean, formatted portfolio report on the console.
6. Automatically save the final report to a text file (`portfolio_report.txt`).
7. Allow users to calculate multiple portfolios in a single session without restarting the program.

---

## 2. Key Features

- **Predefined Stock Catalog**: Sample prices for popular stocks (`AAPL`, `TSLA`, `GOOGL`, `MSFT`, `AMZN`).
- **Flexible Stock Name Input**: Case-insensitive matching (accepts `aapl`, `AAPL`, `Aapl`, etc.).
- **Duplicate Prevention**: Prevents adding the same stock twice in one portfolio calculation.
- **Robust Input Validation**:
  - Validates stock names against the available list.
  - Enforces positive whole numbers for share quantities (rejects zero, negative values, and non-numeric input).
  - Handles invalid entries gracefully using `try-except` blocks without crashing.
- **Clear Financial Formatting**: Displays all stock prices and totals with proper dollar currency notation (`$`) and two decimal places.
- **Automated File Export**: Exports the generated summary to `portfolio_report.txt`.
- **Interactive Session Loop**: Asks users if they wish to analyze another portfolio before exiting.

---

## 3. Python Concepts Demonstrated

This project adheres strictly to fundamental, beginner-level Python constructs:

| Concept | Implementation in Project |
| :--- | :--- |
| **Dictionaries** | Used `STOCK_PRICES` to store stock tickers and their corresponding share prices. |
| **Variables & Data Types** | Integers, floats, strings, lists, sets, and booleans for data tracking. |
| **User Input & Output** | `input()` for interactive prompts and formatted `print()` / f-strings for tables. |
| **Conditional Logic** | `if`, `elif`, `else` statements for validation and flow control. |
| **Loops** | `while` loops for input retry loops and program restart; `for` loops for iterating items. |
| **Functions** | Modular function design (`build_portfolio`, `display_available_stocks`, `save_portfolio_report`, etc.). |
| **Arithmetic Operations** | Multiplication (`price * quantity`) and summation (`sum()`) for total calculation. |
| **File Handling** | Safe context manager (`with open(...)`) to write reports to disk with error handling. |
| **Exception Handling** | `try-except (ValueError, IOError)` to prevent unexpected runtime termination. |

---

## 4. Predefined Stock Prices

| Ticker | Company Name | Sample Price |
| :---: | :--- | :---: |
| **AAPL** | Apple Inc. | $180.00 |
| **TSLA** | Tesla, Inc. | $250.00 |
| **GOOGL** | Alphabet Inc. (Google) | $150.00 |
| **MSFT** | Microsoft Corporation | $300.00 |
| **AMZN** | Amazon.com, Inc. | $200.00 |

*Note: These are fixed sample prices for internship demonstration purposes and do not represent live market feeds.*

---

## 5. Project File Structure

```text
Stock_Portfolio_Tracker/
│
├── stock_tracker.py       # Main Python source code
├── README.md              # Project documentation and guide
├── portfolio_report.txt   # Generated text report file
└── requirements.txt       # Project requirements (built-in standard library)
```

---

## 6. Installation & Execution Guide

### Prerequisites
- Python 3.6 or higher installed on your machine.
- Verify your Python installation by running:
  ```bash
  python3 --version
  ```
  *(or `python --version` on Windows)*

### Method 1: Running via Terminal / Command Prompt

1. Open your terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd /path/to/Stock_Portfolio_Tracker
   ```
3. Run the script:
   ```bash
   python3 stock_tracker.py
   ```
   *(On Windows, run: `python stock_tracker.py`)*

### Method 2: Running in Visual Studio Code (VS Code)

1. Open **Visual Studio Code**.
2. Click **File > Open Folder...** and select the `Stock_Portfolio_Tracker` folder.
3. Open `stock_tracker.py` in the editor.
4. Click the **Run Python File** button in the top-right corner, or open the integrated terminal (`Ctrl + \`` or `Cmd + \``) and type:
   ```bash
   python3 stock_tracker.py
   ```

---

## 7. Sample Terminal Run

```text
=======================================================
       WELCOME TO STOCK PORTFOLIO TRACKER
=======================================================
Track your stock investments easily and generate reports!
-------------------------------------------------------

[AVAILABLE STOCKS & SAMPLE PRICES]
-----------------------------------
Stock Symbol       | Price per Share
-----------------------------------
AAPL               | $180.00        
TSLA               | $250.00        
GOOGL              | $150.00        
MSFT               | $300.00        
AMZN               | $200.00        
-----------------------------------

How many different stocks do you want to add (1 to 5)? 2

Please enter details for 2 stock(s):

--- Stock 1 of 2 ---
Enter stock symbol: AAPL
Enter quantity for AAPL: 5

--- Stock 2 of 2 ---
Enter stock symbol: tsla
Enter quantity for TSLA: 2

==============================================================
                 STOCK PORTFOLIO SUMMARY
==============================================================
Stock Name   | Price ($)    | Quantity   | Investment ($) 
--------------------------------------------------------------
AAPL         | $180.00      | 5          | $900.00        
TSLA         | $250.00      | 2          | $500.00        
--------------------------------------------------------------
GRAND TOTAL INVESTMENT:                | $1400.00       
==============================================================

[Success] Portfolio report has been successfully saved to 'portfolio_report.txt'.

Do you want to calculate another portfolio? (yes/no): no

=======================================================
Thank you for using Stock Portfolio Tracker. Goodbye!
=======================================================
```

---

## 8. Sample Output File (`portfolio_report.txt`)

```text
==============================================================
                 STOCK PORTFOLIO SUMMARY
==============================================================
Stock Name   | Price ($)    | Quantity   | Investment ($) 
--------------------------------------------------------------
AAPL         | $180.00      | 5          | $900.00        
TSLA         | $250.00      | 2          | $500.00        
--------------------------------------------------------------
GRAND TOTAL INVESTMENT:                | $1400.00       
==============================================================

Report generated successfully by Stock Portfolio Tracker.
```

---

## 9. Verification & Test Cases

The application has been tested against the following scenarios:

### Test Case 1: Standard Calculation
- **Input**: `AAPL` (Quantity: 5), `TSLA` (Quantity: 2)
- **Calculation**: $(180 \times 5) + (250 \times 2) = 900 + 500 = \$1400.00$
- **Result**: PASSED

### Test Case 2: Multi-Stock Calculation
- **Input**: `GOOGL` (Quantity: 3), `MSFT` (Quantity: 2)
- **Calculation**: $(150 \times 3) + (300 \times 2) = 450 + 600 = \$1050.00$
- **Result**: PASSED

### Test Case 3: Error Handling & Edge Cases
- **Invalid Stock Name** (e.g., `BITCOIN`, `XYZ`): Displays an informative error listing valid stocks, re-prompts without crash.
- **Case-Insensitive Input** (e.g., `aapl`, `msft`): Automatically normalized to uppercase and processed.
- **Zero Quantity** (e.g., `0`): Rejected with an explicit message that quantity must be greater than zero.
- **Negative Quantity** (e.g., `-5`): Rejected with an error message and re-prompted.
- **Non-Numeric Quantity** (e.g., `five`, `abc`): Trapped by `try-except ValueError` and re-prompted cleanly.
- **Duplicate Stock Selection**: Rejects adding the same stock more than once in a single portfolio session.
