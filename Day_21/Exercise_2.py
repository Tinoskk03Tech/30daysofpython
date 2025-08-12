class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}    # {'Salary': 3000, 'Bonus': 500}
        self.expenses = {}   # {'Rent': 1000, 'Groceries': 300}

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Name: {self.firstname} {self.lastname}")
        print("Incomes:", self.incomes)
        print("Expenses:", self.expenses)
        print("Total Income:", self.total_income())
        print("Total Expense:", self.total_expense())
        print("Balance:", self.account_balance())

# Sample usage
person = PersonAccount("Kossivi Tinè", "KOSSI")
person.add_income("Salary", 3000)
person.add_income("Freelance", 800)
person.add_expense("Rent", 1200)
person.add_expense("Food", 400)
person.account_info()