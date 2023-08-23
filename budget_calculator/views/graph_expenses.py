import matplotlib.pyplot as plt

def graph_expenses(expenses):
    expenses_by_category = {}
    for expense in expenses:
        category = expense.category()
        if category not in expenses_by_category:
            expenses_by_category[category] = 0
        expenses_by_category[category] += expense.amount()

    data = [(category, amount) for category, amount in expenses_by_category.items()]

    data.sort()

    plt.bar([d[0] for d in data], [d[1] for d in data])

    plt.title("Gastos por categoría")

    plt.xlabel("Categoría")

    plt.ylabel("Monto")

    plt.show()
