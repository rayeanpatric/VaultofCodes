def read_and_write_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        with open(filename, 'w') as file:
            file.write(content.upper())
        print(f"File '{filename}' processed successfully.")
    except FileNotFoundError:
        """If the file sample.txt does not exist, the program will crash because 
        the open() function will raise a FileNotFoundError exception."""
        print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    filename = "sample.txt"
    read_and_write_file(filename)

if __name__ == "__main__":
    main()
