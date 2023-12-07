#Quaye Richard
#4 Nov. 2023


from formula import parse_formula

NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1


SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def qr_make_periodic_table():
    qr_periodic_table_dict = {
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        # Add the rest of the elements following the same pattern
        # ...
    }
    return qr_periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    qr_total_molar_mass = 0.0

    for element in symbol_quantity_list:
        symbol = element[SYMBOL_INDEX]
        quantity = element[QUANTITY_INDEX]

        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        qr_total_molar_mass += atomic_mass * quantity

    return qr_total_molar_mass

def main():
    # Get a chemical formula for a molecule from the user.
    formula_input = input("Enter the molecular formula of the sample: ")

    # Get the mass of a chemical sample in grams from the user.
    mass_input = float(input("Enter the mass in grams of the sample: "))

    # Call the make_periodic_table function and store the periodic table in a variable.
    periodic_table = qr_make_periodic_table()

    # Call the parse_formula function to convert the chemical formula given by the user to a compound list.
    symbol_quantity_list = parse_formula(formula_input)

    # Call the compute_molar_mass function to compute the molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)

    # Compute the number of moles in the sample.
    moles = mass_input / molar_mass

    # Print the molar mass.
    print(f"{molar_mass:.5f} grams/mole")

    # Print the number of moles.
    print(f"{moles:.5f} moles")

if __name__ == "__main__":
    # Add a call to the main function, protected with an if statement
    main()
