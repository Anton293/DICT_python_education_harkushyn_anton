"""matrixprocessing"""
import my_matrix_module as matrix


ERROR = "\033[31m{}\033[0m"


def check_input_size_matrix(number_matrix):
    """check input size of matrix nxn"""
    while True:
        try:
            res = input(f"Enter size of {number_matrix} matrix: >").strip().split(" ")
            return res[0], res[1]
        except (ValueError, TypeError, IndexError):
            print(ERROR.format("[error] matrix size"))
            continue


def check_input_matrix_row(matrix_weight):
    """check input row matrix"""
    while True:
        try:
            line_matrix = input("> ")
            line_arr = line_matrix.strip().split(" ")
            if len(line_arr) != int(matrix_weight):
                print(ERROR.format(f"[error] long line, ({','.join(line_arr)}!) -> {matrix_weight} item"))
                continue
            matrix_arr = [int(num) for num in line_arr]
            return matrix_arr
        except (ValueError, TypeError, IndexError):
            print(ERROR.format("[error] matrix line"))
            continue


def get_matrix_from_user(number_matrix: str) -> list:
    """head function check input"""
    matrix_height, matrix_weight = check_input_size_matrix(number_matrix)
    print(f"Enter {number_matrix} matrix [{matrix_height},{matrix_weight}]:")
    matrix_arr = []
    for i in range(int(matrix_height)):
        matrix_arr.append(check_input_matrix_row(matrix_weight))
    return matrix_arr


def title(arr, i):
    print(f"-----[{arr[i-1]}]-----")


def check_choice_user():
    arr = (
        "1. Add matrices",
        "2. Multiply matrix by a constant",
        "3. Multiply matrices",
        "4. Transpose matrix",
        "5. Calculate a determinant",
        "6. Inverse matrix",
        "0. Exit"
    )
    print(*arr, sep='\n')
    try:
        choice = int(input("Your choice: > "))
        title(arr, choice)
        if choice > 6:
            print(ERROR.format(f"[error] invalid index [{choice}]"))
            return False
        return choice

    except (ValueError, TypeError, IndexError):
        print(ERROR.format("[warning] Invalid input"))
        return False


def main():
    while True:
        choice = check_choice_user()
        if choice is False:
            continue
        res = []
        if choice == 1:
            a = get_matrix_from_user("first")
            b = get_matrix_from_user("second")
            res = matrix.addition(a, b)
        elif choice == 2:
            a = get_matrix_from_user("")
            const = input("Enter constant: >")
            res = matrix.multiplication_on_constant(a, int(const))
        elif choice == 3:
            a = get_matrix_from_user("first")
            b = get_matrix_from_user("second")
            res = matrix.multiplication(a, b)
        elif choice == 4:
            print("1. Main diagonal")
            print("2. Side diagonal")
            print("3. Vertical line")
            print("4. Horizontal line")
            choice_type_transpose = input("Your choice: >")
            a = get_matrix_from_user("")
            res = matrix.transpose(a, int(choice_type_transpose))
        elif choice == 5:
            a = get_matrix_from_user("")
            res = matrix.determinant(a)
        elif choice == 6:
            a = get_matrix_from_user("")
            res = matrix.inverse(a)
        elif choice == 0:
            exit()
        print("The result is:")
        matrix.visual(res)
        print("-"*15)


if __name__ == "__main__":
    main()
