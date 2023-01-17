"""Markdown"""
ERROR = "\033[31m{}\033[0m"


class DataProgram(object):
    """save session data program"""
    def __init__(self):
        self.text = ""


data = DataProgram()


def help_program():
    """info command in program"""
    print("""• plain — звичайний текст без форматування
• bold/italic — напівжирний/курсив
• inline-code — вбудований код
• link — посилання
• header — Заголовок
• unordered-list — невпорядкований список
• ordered-list — упорядкований список
• new-line — перехід на новий рядок.

Special commands: !help !done
""")


def save_program_data():
    """save data in file: OUTPUT.md"""
    with open("OUTPUT.md", "w") as f:
        f.write(data.text)


class Command(object):
    """map function"""
    def __init__(self, command: str):
        self.command = command

    def check(self, item: str) -> bool:
        if item[0] == self.command:
            return "True"
        else:
            return "False"


#####################################################################
#                               markdown                            #
#####################################################################


def header_markdown() -> str:
    """headers 1-6 (markdown)"""
    txt = input("Text: ")
    print("The level should be within the range of 1 to 6.")
    type_header = int(input("level:"))
    return " "+("#"*type_header) + "" + txt


def link_markdown() -> str:
    """link (markdown)"""
    input_name = input("Name: ")
    input_url = input("Url: ")
    return f" [{input_name}]({input_url}) "


def list_markdown(prefix: str) -> str:
    """lists (markdown)"""
    input_count_raw = int(input("Count raw: "))
    arr_value_list = ""
    for i in range(input_count_raw):
        arr_value_list += f"\n\t{prefix} "+input(f"RAW #{i+1}: ")
    return arr_value_list+"\n"


#####################################################################
#                        command markdown end                       #
#####################################################################


def main():
    """head function start program"""
    command_format = [
        ("plain", "{} "),
        ("bold", "**{}**"),
        ("italic", "*{}*"),
        ("header", "header_markdown()"),
        ("link", "link_markdown()"),
        ("inline-code", "```{}```"),
        ("ordered-list", "list_markdown('-')"),
        ("unordered-list", "list_markdown('*')"),
        ("new-line", "# {}")
    ]

    while True:
        print("Choose a formatter:")
        input_command_user = input("> ")
        if input_command_user == "!help":
            help_program()
            continue
        elif input_command_user == "!down":
            save_program_data()
            exit()
        try:
            index_choice_command = list(map(Command(input_command_user).check, command_format)).index("True")
            format_text = command_format[index_choice_command][1]
            if "(" in list(format_text):
                data.text += eval(format_text)
            else:
                text_user = input("Text: ")
                result = format_text.format(text_user)
                data.text += " "+result
            print(data.text)
        except ValueError:
            print(ERROR.format("Unknown formatting type or command! Using: !help\n"))


if __name__ == '__main__':
    main()
