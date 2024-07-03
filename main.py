import math
#ex1

class GGD:
    
    def getString(self):
        self.string = input()
    
    def printString(self):
        print(self.string.upper())

str_manip = GGD()
str_manip.getString()
str_manip.printString()

#ex2

class S:
    def __init__(self):
        pass
    
    def a(self):
        return 0

class Sq(S):
    def __init__(self, l):
        super().__init__()
        self.l = l
    
    def a(self):
        return self.l * self.l

if __name__ == "__main__":
    s = S()
    print(f"A of S: {s.a()}")
    
    sq = Sq(4)
    print(f"A of Sq: {sq.a()}")

#ex3

class R(S):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        return self.l * self.w

#ex4

class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Point({self.x}, {self.y})")
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#ex5

class Bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit of ${amount} made. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds. Available balance: ${self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrawal of ${amount} made. New balance: ${self.balance}")
        else:
            print("Withdrawal amount must be positive.")

# account = Bank("Daniel", 10000)


# account.deposit(133)
# account.withdraw(324)
# account.withdraw(42)
# account.deposit(1900)
# account.withdraw(176)


# print(f"Final balance: ${account.balance}")