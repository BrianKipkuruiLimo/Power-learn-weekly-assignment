def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    Args:
        price (float): The original price of the item
        discount_percent (float): The discount percentage to apply
    
    Returns:
        float: The final price after discount (if 20% or higher), otherwise original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Main program to interact with user
def main():
    try:
        # Prompt user for original price
        price = float(input("Enter the original price of the item: $"))
        
        # Prompt user for discount percentage
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate the final price using the function
        final_price = calculate_discount(price, discount_percent)
        
        # Display the result
        if discount_percent >= 20:
            print(f"\nDiscount applied! ({discount_percent}%)")
            print(f"Original price: ${price:.2f}")
            print(f"Final price after discount: ${final_price:.2f}")
            print(f"You saved: ${price - final_price:.2f}")
        else:
            print(f"\nNo discount applied (discount must be 20% or higher)")
            print(f"Price remains: ${final_price:.2f}")
    
    except ValueError:
        print("Please enter valid numeric values for price and discount percentage.")

# Run the program
if __name__ == "__main__":
    main()