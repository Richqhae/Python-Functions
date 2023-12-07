



# test_transaction_calculator.py

import unittest
from transaction_calculator import calculate_tax, add_transaction


class TestTransactionFunctions(unittest.TestCase):
    def test_calculate_tax(self):
        self.assertEqual(calculate_tax('electronics', 500.0), 50.0)
        self.assertEqual(calculate_tax('clothing', 100.0), 5.0)
        self.assertEqual(calculate_tax('books', 30.0), 0.0)
        self.assertEqual(calculate_tax('restaurant', 200.0), 30.0)

    def test_add_transaction(self):
        add_transaction('electronics', 500.0)
        add_transaction('clothing', 100.0)
        add_transaction('books', 30.0)

        self.assertEqual(len(transactions), 3)

        expected_transaction = {'item_type': 'electronics', 'price': 500.0, 'tax_amount': 50.0, 'total_amount': 550.0}
        self.assertEqual(transactions[0], expected_transaction)


if __name__ == '__main__':
    unittest.main()
