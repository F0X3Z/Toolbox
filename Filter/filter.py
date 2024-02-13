import re

def filter_and_remove_duplicates(input_file, output_file):
    # Define a regex pattern to match the desired pattern
    pattern = re.compile(r'[^:\s]+:[^:\s]+$')

    # Use a set to keep track of processed lines
    processed_lines = set()

    with open(input_file, 'r', encoding='latin-1') as file:
        with open(output_file, 'w') as output:
            # Apply the regex pattern to each line of the text
            for line in file:
                match = re.search(pattern, line)
                if match:
                    filtered_line = match.group(0) + '\n'
                    # Check for duplicates and only append if not already processed
                    if filtered_line.strip() not in processed_lines:
                        processed_lines.add(filtered_line.strip())
                        output.write(filtered_line)

# Example usage
input_file_path = 'input.txt'
output_file_path = 'output.txt'

filter_and_remove_duplicates(input_file_path, output_file_path)
