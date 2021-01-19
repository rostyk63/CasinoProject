import random


class User:
    def __init__(self, name, money):
        self.name = name
        if money < 0:
            self.money = 0
        else:
            self.money = int(money)

    def __str__(self):
        return f'Username: {self.name}, money: {self.money} UAH'

    def play(self, money):
        for num, casino in enumerate(all_casinos_list):
            print(num, '-', casino.getName)
        key = input('Enter your casino index: ')
        for num, machine in enumerate(all_casinos_list[int(key)].getMachineList):
            print(num, '-', machine.get_money())
        machine_key = input('Enter your machine index: ')
        all_casinos_list[int(key)].getMachineList[machine_key].play(money)


class SuperAdmin(User):
    def __init__(self, name, money):
        User.__init__(self, name, money)
        self._casino_list = []

    def __str__(self):
        return super().__str__()

    def create_casino(self):
        casino = Casino(input('Enter your casino name: '))
        self._casino_list.append(casino)
        all_casinos_list.append(casino)

    def create_game_machine(self):
        for num, casino in enumerate(self._casino_list):
            print(num, '-', casino.getName)
        key = int(input('Enter your casino index: '))
        if key > len(self._casino_list) or key < 0:
            print('Error')
            return 0
        else:
            new_game_machine = GameMachine(int(input('Enter number of money in your machine: ')))
            self._casino_list[int(key)].add_machine_to_casino(new_game_machine)
            all_casinos_list[int(key)].add_machine_to_casino(new_game_machine)

    def collect_money(self):
        for num, casino in enumerate(self._casino_list):
            print(num, '-', casino.getName)
        key = int(input('Enter your casino index: '))
        if key > len(self._casino_list) or key < 0:
            print('Error')
            return 0
        else:
            for num, machine in enumerate(self._casino_list[int(key)].getMachineList):
                print(num, '-', machine.get_money())
            machine_key = int(input('Enter your machine index to remove: '))
            if machine_key > len(self._casino_list[int(key)].getMachineList) or machine_key < 0:
                print('Error')
                return 0
            else:
                money = self._casino_list[int(key)].getMachineList[machine_key].get_money()
                self._casino_list[int(key)].getMachineList[machine_key].set_money(0)
                all_casinos_list[int(key)].getMachineList[machine_key].set_money(0)
                return money

    def add_money(self):
        for num, casino in enumerate(self._casino_list):
            print(num, '-', casino.getName)
        key = int(input('Enter your casino index: '))
        if key > len(self._casino_list) or key < 0:
            print('Error')
            return 0
        else:
            for num, machine in enumerate(self._casino_list[int(key)].getMachineList):
                print(num, '-', machine.get_money())
            machine_key = int(input('Enter your machine index to remove: '))
            if machine_key > len(self._casino_list[int(key)].getMachineList) or machine_key < 0:
                print('Error')
                return 0
            else:
                money = self._casino_list[int(key)].getMachineList[machine_key].get_money()
                number = int(input('Enter amount of money to add: '))
                self._casino_list[int(key)].getMachineList[machine_key].set_money(money + number)
                all_casinos_list[int(key)].getMachineList[machine_key].set_money(money + number)

    def remove_game_machine(self):
        for num, casino in enumerate(self._casino_list):
            print(num, '-', casino.getName)
        key = int(input('Enter your casino index: '))
        if key > len(self._casino_list) or key < 0:
            print('Error')
            return 0
        else:
            for num, machine in enumerate(self._casino_list[int(key)].getMachineList):
                print(num, '-', machine.get_money())
            machine_key = int(input('Enter your machine index to remove: '))
            if machine_key > len(self._casino_list[int(key)].getMachineList) or machine_key < 0:
                print('Error')
                return 0
            else:
                self._casino_list[key].getMachineList.remove(machine_key)
                all_casinos_list[key].getMachineList.remove(machine_key)


class GameMachine:
    def __init__(self, number):
        if number < 0:
            self._number = 0
        else:
            self._number = int(number)

    @property
    def get_money(self):
        return self._number

    def set_money(self, number):
        self._number = number

    def take_money(self, number):
        self._number = self._number - number

    def put_money(self, number):
        self._number = self._number + number

    def play(self, number):
        numeric = random.randint(100, 999)
        numeric = str(numeric)
        print(numeric)
        if numeric[:1] == numeric[1:2] or numeric[1:2] == numeric[2:3] or numeric[:1] == numeric[2:3]:
            self._number = self._number - number
            return number * 2
        elif numeric[:1] == numeric[1:2] and numeric[1:2] == numeric[2:3] and numeric[:1] == numeric[2:3]:
            self._number = self._number - number
            return number * 3
        else:
            self._number = self._number + number


class Casino:
    def __init__(self, name):
        self._name = name
        self._machine_list = []

    @property
    def getName(self):
        return self._name

    @property
    def getMoney(self):
        sum = 0
        for i in range(self.getMachineCount):
            m = self._machine_list[i]
            sum = sum + m.get_money()
        return sum

    @property
    def getMachineCount(self):
        return len(self._machine_list)

    @property
    def getMachineList(self):
        return self._machine_list

    def add_machine_to_casino(self, machine: GameMachine):
        self._machine_list.append(machine)


all_casinos_list = []