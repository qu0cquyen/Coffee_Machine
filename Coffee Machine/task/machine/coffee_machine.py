class CoffeeMachine:
    water = None
    milk = None
    coffee_beans = None
    disposable_cups = None
    money = None

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550

    def __repr__(self):
        return f"Water: {self.water} - Milk: {self.milk} - Coffee Beans: {self.coffee_beans} - " \
               f"Disposable Cups: {self.disposable_cups} - Money: {self.money}"

    def __str__(self):
        return f"""The Coffee Machine has:
        {self.water} of water
        {self.milk} of milk
        {self.coffee_beans} of coffee beans
        {self.disposable_cups} of disposable cups
        {self.money} of money
        """

    def check(self, w, m, cb):
        if self.water - w < 0:
            print("Sorry, not enough water")
            return 0
        elif self.milk - m < 0:
            print("Sorry, not enough milk")
            return 0
        elif self.coffee_beans - cb < 0:
            print("Sorry, not enough coffee beans")
            return 0
        elif self.disposable_cups < 0:
            print("Sorry, not enough disposable cups")
            return 0
        else:
            return 1

    def buy(self, w, m, cb, sub):
        if self.check(w, m, cb):
            self.water -= w
            self.milk -= m
            self.coffee_beans -= cb
            self.disposable_cups -= 1

            if sub == '1':
                self.money += 4
            elif sub == '2':
                self.money += 7
            else:
                self.money += 6

            print("I have enough resources, making you a coffee!")

    def fill(self, w, m, cb, dc):
        self.water += w
        self.milk += m
        self.coffee_beans += cb
        self.disposable_cups += dc

    def take(self):
        print("I gave you $" + str(self.money) + "\n")
        self.money = 0


if __name__ == "__main__":
    coffee_machine = CoffeeMachine()

    while True:
        option = input("Write action (buy, fill, take, remaining, exit): ")
        if option == "buy":
            sub_op = input("What do you want to buy? 1 - espresso, 2 - latte, "
                           "3 - cappuccino, back - to main menu: ")

            if sub_op == '1':  # Espresso
                coffee_machine.buy(250, 0, 16, sub_op)

            elif sub_op == '2':  # Latte
                coffee_machine.buy(350, 75, 20, sub_op)

            elif sub_op == '3':  # Cappuccino
                coffee_machine.buy(200, 100, 12, sub_op)
            else:
                continue

        elif option == "fill":
            water = int(input("How many ml of water do you want to add: "))
            milk = int(input("How many ml of milk do you want to add: "))
            coffee_beans = int(input("How many grams of coffee beans do you want to add: "))
            disposable_cups = int(input("How many disposable cups of coffee do you want to add: "))
            coffee_machine.fill(water, milk, coffee_beans, disposable_cups)

        elif option == "take":
            coffee_machine.take()

        elif option == "remaining":
            print(coffee_machine)

        elif option == "exit":
            break
