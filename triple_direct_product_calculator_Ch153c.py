# This script analyzes which irreducible representations in a point group
# can have non-zero matrix elements for the Lx, Ly, and Lz operators (components of angular momentum)

# Import the point group data from the separate file
from direct_product_tables_2 import point_groups

# Symmetrize the direct product table since Γ₁ ⊗ Γ₂ = Γ₂ ⊗ Γ₁
def symmetrize_direct_product_table(table):
    extended = {}
    for (ir1, ir2), result in table.items():
        # Add both (ir1, ir2) -> result and (ir2, ir1) -> result
        extended[(ir1, ir2)] = result
        extended[(ir2, ir1)] = result  # Add the symmetric entry
    return extended

# Test if the triple product (Γ ⊗ L_irrep) ⊗ Γ contains the totally symmetric irrep
def triple_product_contains_totally_symmetric(irrep, pg_data, operator='Lz'):
    # Get the appropriate irrep for the selected operator and totally symmetric irrep
    if operator == 'Lx':
        L_irrep = pg_data["Lx_irrep"]
    elif operator == 'Ly':
        L_irrep = pg_data["Ly_irrep"]
    else:  # Default to Lz
        L_irrep = pg_data["Lz_irrep"]
        
    totally_symmetric = pg_data["totally_symmetric"]
    direct_product_table = pg_data["direct_products"]
    
    # Step 1: Calculate the first product Γ ⊗ L_irrep
    first = direct_product_table.get((irrep, L_irrep))
    if not first:
        return False, None, None  # If the product isn't defined, return False and None for products
    
    # For reducible representations (sums of irreps)
    if "+" in first:
        # Split the reducible representation into its component irreps
        components = [comp.strip() for comp in first.split("+")]
        
        # Calculate the second product for each component
        all_second_products = []
        for component in components:
            second = direct_product_table.get((component, irrep))
            if second:
                all_second_products.append(second)
                
        # Combine all second products into a single string
        combined_second = " + ".join(all_second_products)
        
        # Check if any component contains the totally symmetric irrep
        contains_totally_symmetric = False
        for second in all_second_products:
            if totally_symmetric == second or (totally_symmetric in second and "+" in second):
                contains_totally_symmetric = True
                break
                
        return contains_totally_symmetric, first, combined_second
    else:
        # Step 2: Calculate the second product (Γ ⊗ L_irrep) ⊗ Γ
        second = direct_product_table.get((first, irrep))
        
        # For Oh, the result might be a reducible representation
        if second and "+" in second:
            # Check if the totally symmetric irrep is one of the components
            components = [comp.strip() for comp in second.split("+")]
            contains_totally_symmetric = totally_symmetric in components
            return contains_totally_symmetric, first, second
        else:
            # Step 3: Check if the result equals the totally symmetric representation
            contains_totally_symmetric = second == totally_symmetric
            return contains_totally_symmetric, first, second


# Let the user choose the point group and angular momentum operator
def main():
    print("Point Group Analysis for Angular Momentum Matrix Elements")
    print("========================================================")
    print("This script determines which irreducible representations")
    print("can have non-zero matrix elements for the Lx, Ly, or Lz operators.")
    print()
    print("Available point groups:")
    print("1. D4h (Lz transforms as A2g, Lx/Ly as Eg)")
    print("2. Oh (Lz/Lx/Ly transform as T1g)")
    print("3. D3h (Lz transforms as A2', Lx/Ly as E')")
    print("4. Td (Lz/Lx/Ly transform as T1)")
    print()
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        pg_name = "D4h"
    elif choice == "2":
        pg_name = "Oh"
    elif choice == "3":
        pg_name = "D3h"
    elif choice == "4":
        pg_name = "Td"
    else:
        print("Invalid choice. Defaulting to D4h.")
        pg_name = "D4h"
    
    # Choose which angular momentum operator to analyze
    print("\nChoose angular momentum operator:")
    print("1. Lx")
    print("2. Ly")
    print("3. Lz")
    print("4. All (Lx, Ly, Lz)")
    
    op_choice = input("Enter your choice (1-4): ")
    
    if op_choice == "1":
        operators = ["Lx"]
    elif op_choice == "2":
        operators = ["Ly"]
    elif op_choice == "3":
        operators = ["Lz"]
    elif op_choice == "4":
        operators = ["Lx", "Ly", "Lz"]
    else:
        print("Invalid choice. Defaulting to Lz.")
        operators = ["Lz"]
    
    # Get the data for the selected point group
    pg_data = point_groups[pg_name]
    
    # Symmetrize the direct product table
    pg_data["direct_products"] = symmetrize_direct_product_table(pg_data["direct_products"])
    
    # Process each selected operator
    for operator in operators:
        # Build a table of results by testing each irrep
        results = []
        for ir in pg_data["irreps"]:
            # For each irrep, determine if it can have non-zero matrix elements
            # and get the detailed direct product results
            contains_totally_symmetric, first_product, second_product = triple_product_contains_totally_symmetric(ir, pg_data, operator)
            results.append((ir, contains_totally_symmetric, first_product, second_product))
        
        # Display the results without pandas
        print(f"\n{operator} Matrix Element Test in {pg_name}")
        print("=" * (len(f"{operator} Matrix Element Test in {pg_name}")))
        print(f"In {pg_name}, {operator} transforms as {pg_data[f'{operator}_irrep']}")
        print()
        
        # Create a simple table format with detailed direct product results
        print(f"{'Irrep Γ':<10} | {'⟨Γ|'+operator+'|Γ⟩ ≠ 0?':<12} | {'Γ ⊗ ' + pg_data[f'{operator}_irrep']:<20} | {'(Γ ⊗ ' + pg_data[f'{operator}_irrep'] + ') ⊗ Γ':<30}")
        print("-" * 80)
        
        for irrep, result, first_product, second_product in results:
            print(f"{irrep:<10} | {str(result):<12} | {str(first_product):<20} | {str(second_product):<30}")
        
        print()
        print(f"Physical meaning: If True, states transforming as that irrep")
        print(f"can have non-zero angular momentum along the {operator[-1]}-axis.")
        print()
    
    print("For non-zero matrix elements, the triple product must contain")
    print(f"the totally symmetric irrep ({pg_data['totally_symmetric']}).")

if __name__ == "__main__":
    main()
