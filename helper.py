def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number:")
            

def is_even(n):
    return n % 2 == 0

if __name__ == "__main__":
    
    print(f"is_even(2): {is_even(2)}")   # True
    print(f"is_even(7): {is_even(7)}")   # False
    num = get_number("Enter a number: ")
    print(f"You entered {num}")
    