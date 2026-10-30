import csv

def get_atomic_mass(chemical_symbol: str)->float:
    atomic_mass = 0.0
    element_found = False
    try:
        with open('periodic_table.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['Symbol'] == chemical_symbol.upper():
                    atomic_mass = float(row['AtomicMass'])
                    element_found = True
            
            if not element_found:
                print(f"<{chemical_symbol}> does not match any symbol in the dataset!")
    except Exception as e:
        print(f"Error obtaining atomic number!\n {e}")
    return round(atomic_mass)

def get_atomic_number(chemical_symbol: str)->int:
    atomic_number = 0
    element_found = False
    try:
        with open('periodic_table.csv', mode='r', newline='') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                if row['Symbol'] == chemical_symbol.upper():
                    atomic_number = row['AtomicNumber']
                    element_found = True
                    
            if not element_found:
                print(f"<{chemical_symbol}> does not match any symbol in the dataset!")
    except Exception as e:
        print(f"Error obtaining atomic number!\n {e}")
    return atomic_number

if __name__ == '__main__':
    pass