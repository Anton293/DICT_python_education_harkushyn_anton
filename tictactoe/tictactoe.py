"""tictactoe game"""
data_game = {
    "player": 0,
    "canvas": [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
}


class DataWrite:
    """ class"""
    def __init__(self):
        """input_value class constructor"""
        self.xy = []

    def value_in_arr(self, cvs: list, xy: str):
        """input x and y"""
        try:
            self.xy = xy.split(" ")
            coordinates_x = int(self.xy[0])-1
            coordinates_y = int(self.xy[1])-1
            DataWrite().choice_player(cvs, coordinates_x, coordinates_y)
        except (TypeError, ValueError):
            print("You should enter numbers!")
            return

    @staticmethod
    def choice_player(cvs: list, x: int, y: int):
        """check if player"""
        if x > 3 or y > 3:
            print("Coordinates should be from 1 to 3!")
        elif data_game['player'] == 0 and cvs[x][y] == 2:
            cvs[x][y] = 1
            data_game['player'] = 1
        elif cvs[x][y] == 2:
            cvs[x][y] = 0
            data_game['player'] = 0
        else:
            print('This cell is occupied! Choose another one!')


def auto_replace(arr: object):
    """auto_replace function"""
    return str(arr).replace("0", "'O'").replace("1", "'X'").replace("2", "'-'")


def analyze_canvas(cvs: list):
    """analyze canvas, HEAD"""
    analyze_instructions = [
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]],
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]]
    ]
    for i, _ in enumerate(analyze_instructions):
        for case_player in range(2):
            check_coincidence = 0
            for analyze_str in analyze_instructions[i]:
                if cvs[analyze_str[0]][analyze_str[1]] == case_player:
                    check_coincidence += 1
                    if check_coincidence >= 3:
                        print(f"{auto_replace(case_player)} wins")
                        return False
    return True


class Canvas:
    """canvas output, class"""
    def __init__(self, cvs: list):
        """canvas constructor"""
        self.cvs = cvs

    def table(self):
        """main function"""
        for i, _ in enumerate(self.cvs):
            line = " |"
            for value in self.cvs[i]:
                line += f" {value} "
            print(f"{line}|")

    def output(self):
        """"output canvas"""
        self.cvs = eval(auto_replace(self.cvs))
        long_str = len(self.cvs[0]) * 3
        print(f" +{'-'*long_str}+")
        Canvas(self.cvs).table()
        print(f" +{'-'*long_str}+")


def main():
    """start game"""
    while True:
        return_analyze = analyze_canvas(data_game['canvas'])
        Canvas(data_game['canvas']).output()
        if return_analyze:
            DataWrite().value_in_arr(data_game['canvas'], input("Enter the coordinates:"))
        else:
            break


if __name__ == "__main__":
    main()
