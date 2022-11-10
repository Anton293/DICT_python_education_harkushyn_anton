"""coffee machine"""
import time


class CoffeeMachine:
    """class coffee machine"""
    def __init__(self, money, water, milk, coffee, caps):
        """init coffee machine"""
        self.money = money
        self.available = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
            "caps": caps
        }
        self.full_cap = (
            {"water": 250, "milk": 0, "coffee": 16, "caps": 1, "cost": 4},
            {"water": 350, "milk": 75, "coffee": 20, "caps": 1, "cost": 7},
            {"water": 200, "milk": 100, "coffee": 12, "caps": 1, "cost": 6}
        )
        self.stages_drink = (
            "Starting to make a coffee",
            "Grinding coffee beans",
            "Boiling water",
            "Mixing boiled water with crushed coffee beans",
            "Pouring coffee into the cup",
            "Pouring some milk into the cup",
            "Coffee is ready!"
        )
        self.plus_string = ('ml of water', 'ml of milk', 'grams of coffee beans', 'disposable cups')

    def buy(self, number_caps: int, type_coffee: int) -> None:
        """buy: 1 - espresso, 2 - latte, 3 - cappuccino"""
        for ingredient in self.available:
            need_ingredient = self.available[ingredient] - self.full_cap[type_coffee - 1][ingredient] * number_caps * 1
            if need_ingredient <= 0:
                print(f"Sorry, not enough {ingredient}!")
                return
        for i, ingredient in enumerate(self.available):
            self.available[ingredient] -= self.full_cap[type_coffee-1][ingredient] * number_caps * 1
        self.money += self.full_cap[type_coffee-1]['cost']
        for stage in self.stages_drink:
            print(stage)
            time.sleep(1)
        time.sleep(1)
        print("I have enough resources, making you a coffee!")

    def fill(self):
        """add components in the coffee machine"""
        for i, ingredient in enumerate(self.available):
            while True:
                try:
                    self.available[ingredient] += int(input(f"Write how many {self.plus_string[i]} do you want to add:"))
                except ValueError:
                    print(f"Sorry, input value {ingredient} error!")
                    continue
                break

    def take(self):
        """withdraw all cash"""
        print(f"I gave you {self.money}")
        self.money -= self.money

    def remaining(self):
        """status of the machine"""
        print("The coffee machine has:")
        for i, ingredient in enumerate(self.available):
            print(f"{self.available[ingredient]} {self.plus_string[i]}")
        print(f"{self.money} of money")


def main_menu(coffeemachine):
    """menu coffee machine"""
    while True:
        print("\nWrite action (buy, fill, take, remaining, exit):")
        choice = input(">").strip().lower()
        match choice:
            case "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
                choice_coffee = input(">")
                if choice_coffee == "back":
                    main_menu(coffeemachine)
                    break
                try:
                    coffeemachine.buy(1, int(choice_coffee))
                except:
                    print(f"Error: the selected product number [{choice_coffee}] is not in the system, choose another one")
            case "fill":
                coffeemachine.fill()
            case "take":
                coffeemachine.take()
            case "remaining":
                coffeemachine.remaining()
            case "exit":
                return
            case _:
                print("Invalid input!")


if __name__ == "__main__":
    main_menu(CoffeeMachine(550, 400, 540, 120, 9))
