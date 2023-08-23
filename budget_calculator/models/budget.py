class Budget:
    def __init__(self, category, amount, user):
        self.category = category
        self.amount = amount
        self.user = user

    def __repr__(self):
        return f"Budget(category={self.category}, amount={self.amount}, user={self.user})"
