#1. program cat.py that takes a filename as command-line argument and prints all the contents of that file
import sys

def print_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if len(sys.argv) != 2:
    print("Usage: python cat.py <Nit.txt>")
else:
    filename = sys.argv[1]
    print_file_contents(filename)

#2. program wc.py that takes filename as argument and counts number of lines, words and chars in file.
import sys

if len(sys.argv) != 3:
        print("File name not entered")
        
else:
    source_filename = sys.argv[1]
    destination_filename = sys.argv[2]


    try:
            with open(source_filename, 'r') as source_file:
                source_contents = source_file.read()

                with open(destination_filename, 'w') as destination_file:
                    destination_file.write(source_contents)

            print(f"File '{source_filename}' copied to '{destination_filename}'")
    except FileNotFoundError:
            print(f"Error: File '{source_filename}' not found.")
    except Exception as e:
            print(f"An error occurred: {e}")

#3. program head.py that takes a filename as command-line argument and prints the first 5 lines of it.
import sys

def print_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            for _ in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python head.py <Shr.txt>")
    else:
        filename = sys.argv[1]
        print_first_n_lines(filename, 5)