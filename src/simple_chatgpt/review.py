from .ask import ask
from git import Git

import sys

review_prompt ='Please review and give short feedback for the code below. Also please give examples of better code if needed.\n\n'

def get_lines_from_file(file_name, start_line=None, end_line=None):
    """
    Retrieve lines from a file within a specified range.

    Args:
        file_name (str): The name of the file to read.
        start_line (int, optional): The starting line number. Default is None.
        end_line (int, optional): The ending line number. Default is None.

    Returns:
        list: The lines from the file within the specified range.

    Raises:
        FileNotFoundError: If the specified file is not found.
        PermissionError: If there is a permission denied error when attempting to read the file.
    """
    lines = []

    try:
        with open(file_name, "r") as file:
            for i, line in enumerate(file, start=1):
                if start_line and end_line:
                    if i >= start_line and i <= end_line:
                        lines.append(line)
                    elif i > end_line:
                        break
                else:
                    lines.append(line)
    except FileNotFoundError:
        raise FileNotFoundError("File not found: {}".format(file_name))
    except PermissionError:
        raise PermissionError("Permission denied when reading file: {}".format(file_name))

    return lines

def format_lines(lines):
    """
    Format a list of lines into a single string.

    Args:
        lines (list): The lines to format.

    Returns:
        str: The formatted lines as a single string.
    """
    return "".join(lines)

def parse_file_name(file_name):
    """
    Parse the file name and line range from a given input.

    Args:
        file_name (str): The input string containing the file name and line range.

    Returns:
        tuple: A tuple containing the file name, start line number, and end line number.

    Raises:
        ValueError: If the input string is not in the correct format.
    """
    parts = file_name.split(":")
    if len(parts) == 0:
        raise ValueError("Invalid input format")
    
    file_name = parts[0]
    start_line = None
    end_line = None
    
    if len(parts) > 1:
        line_range = parts[1].split("-")
        if len(line_range) == 1:
            start_line_str = end_line_str = line_range[0]
            
        elif len(line_range) == 2:
            start_line_str = line_range[0]
            end_line_str = line_range[1]
        
        else:
            raise ValueError("invalid line range")

        try:
            start_line = int(start_line_str)
            end_line = int(end_line_str)
        except ValueError:
            raise ValueError("Invalid line number")
        
    return file_name, start_line, end_line


def review(input_file_name):
    """
    Reviews the content of a file.
    
    Args:
        input_file_name (str): The name of the file to review.
    
    Returns:
        str: The reviewed content of the file.
    """
    if not input_file_name:
        return 'Need a file name to review'
    
    filename, start_line, end_line = parse_file_name(input_file_name)
    lines = get_lines_from_file(filename, start_line, end_line)
    content = format_lines(lines)
    return ask(f"{review_prompt}{content}")

def review_from_git_staged():
    """
    Reviews the content of a file that has been staged in git.
    
    Returns:
        str: The reviewed content of the file.
    """
    git = Git()
    diff = git.diff('--staged')
    prompt = "Please review and give short feedback for the diff below. Give examples if needed.\n\n"
    return ask(f"{prompt}{diff}")

def main():
    if len(sys.argv) < 2:
        print(review_from_git_staged())
        sys.exit(0)
    filename = sys.argv[1]
    print(review(filename))

if __name__ == "__main__":
    main()

