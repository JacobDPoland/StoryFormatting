import pyperclip

def read_file_into_string(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:  # Open the file with UTF-8 encoding
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        print("File not found.")
        return None
    except Exception as e:
        print("Error:", e)
        return None

def replace_newline_with_space(input_string):
    return input_string.replace("\n", " ")

def copy_to_clipboard(text):
    try:
        pyperclip.copy(text)
        print("Copied to clipboard:", text)
    except Exception as e:
        print("Error copying to clipboard:", e)

def main():
    input_string = read_file_into_string("input.txt")

    if input_string is not None:
        modified_string = replace_newline_with_space(input_string)
        copy_to_clipboard(modified_string)


if __name__ == "__main__":
    main()
