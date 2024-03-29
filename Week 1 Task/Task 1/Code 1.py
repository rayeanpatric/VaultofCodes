# This program reverses a string.
"""This program has no error and runs perfectly. 
No changes were done except commenting. 
Program perfectly runs with no 
modifications and the logic is correct."""

def reverse_string(s):
    reversed = ""
    for i in range(len(s) - 1, -1, -1):
        # Iterate over the input string in reverse order and add each character to the reversed string.
        reversed += s[i]
    return reversed

def main():
    #Prints the reversed string to the console.

    input_string = "Hello, world!"
    reversed_string = reverse_string(input_string)
    print(f"Reversed string: {reversed_string}")

if __name__ == "__main__":
    main()