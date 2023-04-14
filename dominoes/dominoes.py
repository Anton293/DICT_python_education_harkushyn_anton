import random
import re


class StartGame(object):
    """creating conditions for the game"""

    def create_list_bones(self) -> list:
        """Create domino bones"""
        arr = []

        for i in range(7):
            for j in range(i, 7):
                arr.append([i, j])
        
        return arr
    
    
    def start_bone(self, bones: str) -> int:
        """check for matching numbers bones"""
        bones.sort()
        
        for i, item in enumerate(bones):
            if item[0] == item[1]:
                return i
        
        return -1
    
    def start(self):
        """random player's first turn from [0,0] to [6,6]"""
        self.status = random.choice(["user", "computer"])

        if self.status == "computer" and (choise_bone_id := self.start_bone(self.computer)) != -1:
            self.board.append(self.computer[choise_bone_id])
            del self.computer[choise_bone_id]

        elif self.status == "user" and (choise_bone_id := self.start_bone(self.user)) != -1:
            self.board.append(self.user[choise_bone_id])
            del self.user[choise_bone_id]
        
        else:
            self.initialization()
            self.start()
        
    
    def initialization(self) -> None:
        """create and set variable values"""
        self.list_bones = self.create_list_bones()
        random.shuffle(self.list_bones)
        self.user = self.add_bones_user(7)
        self.computer = self.add_bones_user(7)


class Interfaсe(object):
    """interfaсe game"""

    def draw_bones_board(self, bones: list) -> str:
        if len(bones) > 6:
            return f"{[i for i in bones[:3]]} ... {[i for i in bones[-3:]]}".replace("]", "").replace("[", "")
        return str(bones)

    def draw(self):
        """Draw the game board and print out user and computer pieces."""
        print("="*70)
        print(f"Stock size: {len(self.list_bones)}")
        print(f"Computer pieces: {len(self.computer)}\n")
        print(f"{self.draw_bones_board(self.board)}")
        print(f"\nYour pieces:")
        print(*[f"{i+1}:{bone}" for i, bone in enumerate(self.user)], sep="\n")

    def step(self) -> int:
        """Handle a single user turn."""
        input_command_user = input("Status: It's your turn to make a move. Enter your command.\n>")
        
        try:
            if int(input_command_user.replace("-", "")) > len(self.user):
                print("Invalid input. Please try again.")
                return -1

            if input_command_user == "0":
                self.user += self.add_bones_user(1)
                print("You pass")

            elif not re.match("-", input_command_user) is None:
                #left
                command_id = int(input_command_user.replace("-", ""))
                if self.left_add_bone(command_id) == -1:
                    print("Illegal move. Please try again.")
                    return -1
                
            else:
                #right
                command_id = int(input_command_user)
                if self.right_add_bone(command_id) == -1:
                    print("Illegal move. Please try again.")
                    return -1
            
        except (ValueError, IndexError):
            print("Illegal move. Please try again.")
            return -1

        self.draw()
        input("Status: Computer is about to make a move. Press Enter to continue...")
        self.brain_bot()
        self.draw()
            

    
class ProcessGame(object):
    """Class that handles the game mechanics."""

    def check_finish(self) -> None:
        """Check if the game is finished."""
        if self.board[0][0] == self.board[-1][1]:
            if len(re.findall(str(self.board[0][0]), str(self.board))) == 8:
                print("Status: The game is over. It's a draw!")
        
        elif len(self.user) == 0:
            print("Status: The game is over. You won!")
        elif len(self.computer) == 0:
            print("Status: The game is over. The computer won!")

    def left_add_bone(self, user_bone_id: int) -> bool:
        """Add a bone to the left side of the board."""
        revert_bone = self.user[user_bone_id - 1][::-1]
        bone = self.user[user_bone_id - 1]
        
        if self.board[0][0] == revert_bone[1]:
            self.board.insert(0, revert_bone)
            del self.user[user_bone_id-1]
            return 1

        elif self.board[0][0] == bone[1]:
            self.board.insert(0, bone)
            del self.user[user_bone_id-1]
            return 1
        
        else:
            return 0
    
    def right_add_bone(self, user_bone_id: int) -> bool:
        """Add a bone to the right side of the board."""
        
        revert_bone = self.user[user_bone_id - 1][::-1]
        bone = self.user[user_bone_id - 1]
        
        if self.board[-1][1] == revert_bone[0]:
            self.board.append(revert_bone)
            del self.user[user_bone_id-1]
            return 1
        
        elif self.board[-1][1] == bone[0]:
            self.board.append(bone)
            del self.user[user_bone_id-1]
            return 1

        else:
            return 0
        

    def status_revert(self) -> None:
        """edit status"""
        if self.status == "computer":
            self.status = "user"
        else:
            self.status = "computer"
    
    def check_add_bone(self, i: int, bone: list) -> bool:
        """Check bone before adding to board"""
        if self.board[0][0] == bone[1]:
            self.board.insert(0, bone)
            del self.computer[i]
            return 1

        elif self.board[-1][1] == bone[0]:
            self.board.append(bone)
            del self.computer[i]
            return 1
        
        return 0
        
    def brain_bot(self) -> None:
        """Handles a single computer turn."""
        arr = {0: 5, 1: 3, 2: 3, 3: 1, 4: 3, 5: 3, 6: 0}
        self.computer.sort(key=lambda item: arr[item[0]] + arr[item[1]])
        self.computer.reverse()

        for i, bone in enumerate(self.computer):
            revert_bone = self.computer[i][::-1]
            bone = self.computer[i]

            if self.check_add_bone(i, revert_bone) != 0:
                return 1
            
            if self.check_add_bone(i, bone) != 0:
                return 1
            
        self.computer += self.add_bones_user(1)
        return -1

    def add_bones_user(self, number: int = 7) -> list:
        """
        Adds random bones to the user's hand.

        Args:
            number (int): The number of bones to add. Defaults to 7.

        Returns:
            list: A list of the bones added to the user's hand.

        If there are not enough bones to add, returns -1.
        """

        if len(self.list_bones)-number >= 0:
            get_random_bones = random.sample(self.list_bones, number)
            for item in get_random_bones:
                i = self.list_bones.index(item)
                del self.list_bones[i]
            
            return get_random_bones
        return -1


class FunctionGame(Interfaсe, StartGame, ProcessGame):

    def __init__(self) -> None:
        """
        Initializes a new instance of the FunctionGame class.

        Attributes:
            board (list): The game board, initially empty.
            user (list): The user's hand, initially empty.
            computer (list): The computer's hand, initially empty.
            list_bones (list): The list of all available bones.
            status (str): The status of the game, initially empty.
        """
        self.board: list = []
        self.user: list = []
        self.computer: list = []
        self.list_bones: list = []
        self.status: str = ""
        

def main():
    game = FunctionGame()
    game.initialization()
    game.start()

    game.draw()
    if game.status == "user":
        input("Status: Computer is about to make a move. Press Enter to continue...")
        game.brain_bot()
        game.draw()

    while True:

        if game.step() == -1:
            continue


if __name__ == '__main__':
    main()
