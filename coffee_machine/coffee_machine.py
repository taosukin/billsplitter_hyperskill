class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "choosing an action"

    def process_input(self, user_input):
        if self.state == "choosing an action":
            if user_input == "buy":
                self.state = "choosing a type of coffee"
            elif user_input == "fill":
                self.state = "filling water"
            elif user_input == "take":
                self.take_money()
            elif user_input == "remaining":
                self.print_state()
            elif user_input == "exit":
                return False
        elif self.state == "choosing a type of coffee":
            if user_input == "1":
                self.make_coffee(250, 0, 16, 4)
            elif user_input == "2":
                self.make_coffee(350, 75, 20, 7)
            elif user_input == "3":
                self.make_coffee(200, 100, 12, 6)
            elif user_input == "back":
                self.state = "choosing an action"
        elif self.state == "filling water":
            self.water += int(user_input)
            self.state = "filling milk"
        elif self.state == "filling milk":
            self.milk += int(user_input)
            self.state = "filling coffee beans"
        elif self.state == "filling coffee beans":
            self.coffee_beans += int(user_input)
            self.state = "filling disposable cups"
        elif self.state == "filling disposable cups":
            self.disposable_cups += int(user_input)
            self.state = "choosing an action"
        return True

    def make_coffee(self, water, milk, coffee_beans, cost):
        if self.water < water:
            print("Sorry, not enough water!")
            self.state = "choosing an action"
        elif self.milk < milk:
            print("Sorry, not enough milk!")
            self.state = "choosing an action"
        elif self.coffee_beans < coffee_beans:
            print("Sorry, not enough coffee beans!")
            self.state = "choosing an action"
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            self.state = "choosing an action"
        else:
            print("I have enough resources, making you a coffee!")
            self.disposable_cups -= 1
            self.water -= water
            self.milk -= milk
            self.coffee_beans -= coffee_beans
            self.money += cost
            self.state = "choosing an action"

    def take_money(self):
        print("I gave you $" + str(self.money))
        self.money = 0

    def print_state(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.coffee_beans) + " of coffee beans")
        print(str(self.disposable_cups) + " of disposable cups")
        print("$" + str(self.money) + " of money")


def main():
    coffee_machine = CoffeeMachine()
    while True:
        if coffee_machine.state == "choosing an action":
            print("Write action (buy, fill, take, remaining, exit):")
        elif coffee_machine.state == "choosing a type of coffee":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        elif coffee_machine.state == "filling water":
            print("Write how many ml of water do you want to add:")
        elif coffee_machine.state == "filling milk":
            print("Write how many ml of milk do you want to add:")
        elif coffee_machine.state == "filling coffee beans":
            print("Write how many grams of coffee beans do you want to add:")
        elif coffee_machine.state == "filling disposable cups":
            print("Write how many disposable cups of coffee do you want to add:")
        user_input = input()
        if not coffee_machine.process_input(user_input):
            break


main()