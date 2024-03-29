# Python program that validates user input.
def get_age():
    age = input("Please enter your age: ")
    if age.isnumeric() and int(age) >= 18: 
        """Since the default datatype of input is string it should 
        be typecasted to integer before using comparison operator 
        with integer. So age >= 18 is changed to int(age) >= 18"""
        return int(age)
    else:
        return None

def main():
    age = get_age()
    if age:
        print(f"You are {age} years old and eligible.")
    else:
        print("Invalid input. You must be at least 18 years old.")

if __name__ == "__main__":
    main()
