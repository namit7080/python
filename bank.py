class User():
    # Hold the user detail
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender


    # show detail
    def show_details(self):
        print("Detail of User")
        print("")
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Gender: ",self.gender)

#user
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        left = self.balance - amount
        if left >= 0:
            print("Take ", amount)
            self.balance = left
        else:
            print("Insufficient")

    def view(self):
        print("Current amount is ", self.balance)

namit = Bank("Namit", 20, "Male")
namit.deposit(1000)
namit.deposit(1000)
namit.withdraw(20001)
namit.view()



