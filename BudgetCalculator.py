import tkinter as tk
from tkinter import messagebox

class BudgetCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Calculator App")

        self.expenses = []
        self.budget = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        budget_label = tk.Label(self.root, text="Enter your budget:")
        budget_label.pack()

        budget_entry = tk.Entry(self.root, textvariable=self.budget)
        budget_entry.pack()

        set_budget_button = tk.Button(self.root, text="Set Budget", command=self.set_budget)
        set_budget_button.pack()

        expense_label = tk.Label(self.root, text="Enter expense description and amount:")
        expense_label.pack()

        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        add_expense_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        add_expense_button.pack()

        self.expense_list = tk.Listbox(self.root)
        self.expense_list.pack()

        edit_expense_button = tk.Button(self.root, text="Edit Expense", command=self.edit_expense)
        edit_expense_button.pack()

        delete_expense_button = tk.Button(self.root, text="Delete Expense", command=self.delete_expense)
        delete_expense_button.pack()

        show_summary_button = tk.Button(self.root, text="Show Budget Summary", command=self.show_budget_summary)
        show_summary_button.pack()

    def set_budget(self):
        try:
            budget_amount = self.budget.get()
            if budget_amount < 0:
                raise ValueError("Budget amount must be non-negative")
            self.budget_amount = budget_amount
            messagebox.showinfo("Success", f"Budget set to ${budget_amount:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_expense(self):
        description = self.description_entry.get()
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Expense amount must be positive")
            self.expenses.append((description, amount))
            self.expense_list.insert(tk.END, f"{description}: ${amount:.2f}")
            self.description_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Expense added successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def edit_expense(self):
        selected_index = self.expense_list.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Select an expense to edit.")
            return

        selected_index = selected_index[0]
        selected_expense = self.expenses[selected_index]

        new_description = self.description_entry.get()
        try:
            new_amount = float(self.amount_entry.get())
            if new_amount <= 0:
                raise ValueError("Expense amount must be positive")

            self.expenses[selected_index] = (new_description, new_amount)
            self.expense_list.delete(selected_index)
            self.expense_list.insert(selected_index, f"{new_description}: ${new_amount:.2f}")

            self.description_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Expense edited successfully")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_expense(self):
        selected_index = self.expense_list.curselection()
        if not selected_index:
            messagebox.showerror("Error", "Select an expense to delete.")
            return

        selected_index = selected_index[0]
        selected_expense = self.expenses[selected_index]

        self.expenses.pop(selected_index)
        self.expense_list.delete(selected_index)
        messagebox.showinfo("Success", "Expense deleted successfully")

    def show_budget_summary(self):
        total_expenses = sum(amount for _, amount in self.expenses)
        remaining_budget = self.budget_amount - total_expenses
        summary_text = (
            f"Total Budget: ${self.budget_amount:.2f}\n"
            f"Total Expenses: ${total_expenses:.2f}\n"
            f"Remaining Budget: ${remaining_budget:.2f}"
        )
        messagebox.showinfo("Budget Summary", summary_text)

def main():
    root = tk.Tk()
    app = BudgetCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
