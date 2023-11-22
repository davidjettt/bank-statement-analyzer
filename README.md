# Bank Statement Analyzer

This Python script analyzes a Chase bank statement in PDF format and calculates the total number of transactions and the total amount of those transactions.

## How it works

The script opens a PDF file, reads the pages that contain the account activity, and extracts the text from those pages. It then splits the text into lines and processes each line.

A line is considered a transaction if it meets the following criteria:

-   The first item in the line contains a slash (/) and is 5 characters long (a transaction date).
-   The second item in the line is not 'Payment'.

For each transaction, the script increments a counter and adds the amount of the transaction (the last item in the line) to a running total.

At the end, the script prints the total number of transactions and the total amount.

## Usage

To use this script, you need to have a Python environment set up and the necessary libraries installed. You also need to replace `bank_statement` with the path to your PDF file.

Run the script with:

```bash
python main.py
```
