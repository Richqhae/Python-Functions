#Quaye Richard
# 4th December,2023
#This is Quaye Richard final project on tax calculations
#  




# tax_transaction_calculator.py

# Define tax rates
qr_tax_rates = {
    'electronics': 0.1,
    'clothing': 0.05,
    'books': 0.0,
    'restaurant': 0.15,
}

# Initialize transactions list
transactions = []


def calculate_tax(item_type, price):
    """Calculate tax for a given transaction."""
    if item_type in qr_tax_rates:
        tax_rate = qr_tax_rates[item_type]
        tax_amount = price * tax_rate
        return tax_amount
    else:
        return 0.0


def qr_add_transaction(item_type, price):
    """Add a transaction to the transactions list."""
    tax_amount = calculate_tax(item_type, price)
    total_amount = price + tax_amount
    transaction = {'item_type': item_type, 'price': price, 'tax_amount': tax_amount, 'total_amount': total_amount}
    transactions.append(transaction)


def display_transactions():
    """Display all transactions."""
    for transaction in transactions:
        print(
            f"Item Type: {transaction['item_type']}, Price: ${transaction['price']:.2f}, "
            f"Tax Amount: ${transaction['tax_amount']:.2f}, Total Amount: ${transaction['total_amount']:.2f}"
        )

# Student's comment
# During lesson 13, I spent approximately 8 hours working on the final project. I read documentation on Python dictionaries and lists, watched video tutorials on modular programming, and experimented with different approaches to implement the transaction calculator.

# I divided the code into functions to improve modularity. The calculate_tax function calculates the tax for a given item type and price. The add_transaction function adds a transaction to the transactions list, including tax calculations. The display_transactions function prints details of all transactions.

# Example transactions
qr_add_transaction('electronics', 500.0)
qr_add_transaction('clothing', 100.0)
qr_add_transaction('books', 30.0)
qr_add_transaction('restaurant', 200.0)

# Display all transactions
display_transactions()
