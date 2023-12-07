#Quaye Richard
# 18 Nov 2023


import csv
from datetime import datetime

def qr_read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    qr_compound_dict = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key = row[key_column_index]
            qr_compound_dict[key] = row
    return qr_compound_dict

def apply_discount(original_price):
    """Apply a 10% discount to the original price."""
    return original_price * 0.9

def main():
    try:
        # Store name
        store_name = "Your Store Name"

        # Call read_dictionary function and store the compound dictionary in products_dict
        products_dict = qr_read_dictionary('products.csv', 0)

        # Print store name at the top of the receipt
        print(f"{store_name} Receipt\n")

        # Open the request.csv file for reading
        with open('request.csv', newline='') as request_file:
            # Skip the first line of the request.csv file containing column headings
            next(request_file)

            total_items = 0
            subtotal = 0

            # Loop through each row in the request.csv file
            for row in csv.reader(request_file):
                # Use the requested product number to find the corresponding item in the products_dict
                product_number = row[0]
                product_info = products_dict.get(product_number)

                # If the product is found, print the product name, requested quantity, and product price
                if product_info:
                    product_name = product_info[1]
                    quantity = int(row[1])
                    price = float(product_info[2])

                    # Check for discounts based on day and time
                    current_day = datetime.now().strftime("%A")
                    current_time = datetime.now().strftime("%H:%M:%S")
                    
                    if current_day in ['Tuesday', 'Wednesday']:
                        price = apply_discount(price)
                        print(f"Discount Applied (Tuesday/Wednesday): 10% off {product_name}")

                    elif datetime.strptime(current_time, "%H:%M:%S").time() < datetime.strptime("11:00:00", "%H:%M:%S").time():
                        price = apply_discount(price)
                        print(f"Discount Applied (Before 11:00 a.m.): 10% off {product_name}")

                    total_items += quantity
                    subtotal += quantity * price
                    print(f"{product_name}: {quantity} @ {price:.2f}")

        # Print the number of ordered items and subtotal
        print(f"\nTotal items: {total_items}")
        print(f"Subtotal: ${subtotal:.2f}")

        # Calculate and print sales tax and total amount due
        qr_tax_rate = 0.06
        qr_sales_tax = subtotal * qr_tax_rate
        qr_total_due = subtotal + qr_sales_tax
        print(f"Sales Tax (6%): ${qr_sales_tax:.2f}")
        print(f"Total Due: ${qr_total_due:.2f}")

        # Print a thank you message
        print("\nThank you for shopping with us!")

        # Print a coupon for one of the products
        if total_items > 0:
            random_product = list(products_dict.values())[0]
            print(f"\nCoupon: Get 20% off {random_product[1]} on your next visit!")

        # Print an invitation for the customer to complete an online survey
        print("\nPlease complete our online survey for a chance to win a gift card!")

        # Get and print the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\nDate and Time: {current_datetime}")

    except FileNotFoundError:
        print("Error: One or both of the CSV files not found.")

    except KeyError:
        print("Error: Product number not found in the catalog.")

if __name__ == "__main__":
    # Call the main function
    main()
