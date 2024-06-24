#3. Reverse the content of file using Stack

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_file_content(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            content = f.readlines()

        stack = Stack()

        for line in content:
            stack.push(line)

        with open(output_file, 'w') as f:
            while not stack.is_empty():
                f.write(stack.pop())

        print("Content reversed and saved to", output_file)

    except FileNotFoundError:
        print("Input file not found.")

# Provide the input and output file names
    input_filename = "input.txt"
    output_filename = "reversed_output.txt"

    reverse_file_content(input_filename, output_filename)
