class Category:

    def __init__(self, budget_category):
        self.category = budget_category
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": (-1) * amount, "description": description})
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, destination_budget):
        if self.check_funds(amount):
            self.ledger.append(
                {"amount": (-1) * amount, "description": "Transfer to " + destination_budget.category})
            self.balance -= amount
            destination_budget.ledger.append(
                {"amount": amount, "description": "Transfer from " + self.category})
            destination_budget.balance += amount
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.balance

    def __repr__(self):
        header = "*"*((30-len(self.category))//2) + self.category + \
            "*" * ((30 - len(self.category)) // 2)
        body = ""
        for line in self.ledger:
            body += "\n{:23.23}{:>7.2f}".format(
                line['description'], line['amount'])
        body += "\nTotal: {:.2f}".format(self.balance)
        return header + body


def create_spend_chart(categories):
    percentages = {}
    withdrawals = {}
    total_withdrawals = 0

    for cat in categories:
        withdrawals[cat.category] = 0
        for w in cat.ledger:
            if w['amount'] < 0:
                withdrawals[cat.category] += abs(w['amount'])
                total_withdrawals += abs(w['amount'])

    for cat in categories:
        percentages[cat.category] = int(
            (withdrawals[cat.category] / total_withdrawals * 100)//10)*10

    table = "Percentage spent by category"
    for x in range(100, -10, -10):
        table += "\n{:>3}| ".format(x)
        for cat in categories:
            table += "o  " if percentages[cat.category] >= x else "   "

    max_len = max([len(x.category) for x in categories])
    table += "\n    " + "-" * 3 * len(categories) + "-"

    for x in range(max_len):
        table += "\n     "
        for cat in categories:
            table += "{}  ".format(cat.category[x]
                                   if x < len(cat.category) else " ")
    return table
