import re


def check_pattern(input_string_and_pattern):
    try:
        user_input = input_string_and_pattern.split("|")
        pattern = user_input[0]
        input_string = user_input[1]

        match = re.search(pattern, input_string)
        if match:
            return True
        else:
            return False
    except IndexError:
        return "error"


def main():
    while True:
        input_user = input("Input: ")
        print(f"Output: {check_pattern(input_user)}")


if __name__ == "__main__":
    main()