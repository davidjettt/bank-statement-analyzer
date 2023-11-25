# Bank Statement Analyzer

This Python script detects creation of a new PDF file in a targt folder using Watchdog and analyzes a Chase bank statement in PDF format and calculates the total number of transactions and the total amount of those transactions.

## How it works

The script is run. When a new PDF file gets uploaded to the 'statements' folder, it reads the pages that contain the account activity, and extracts the text from those pages. It then splits the text into lines and processes each line.

A line is considered a transaction if it meets the following criteria:

-   The first item in the line contains a slash (/) and is 5 characters long (a transaction date).
-   The second item in the line is not 'Payment'.

For each transaction, the script increments a counter and adds the amount of the transaction (the last item in the line) to a running total.

At the end, the script prints the total number of transactions and the total amount.

## Usage

To use this script, you need to have a Python environment set up and the necessary libraries installed: **watchdog** and **pypdf2**.

Run the script with:

```bash
python main.py
```
