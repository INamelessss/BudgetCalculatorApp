from datetime import datetime

class Expense:
    def __init__(self, amount, category, date, user):
        self.amount = amount
        self.category = category
        self.date = date
        self.user = user

    def __repr__(self):
        return f"Expense(amount={self.amount}, category={self.category}, date={self.date}, user={self.user})"
