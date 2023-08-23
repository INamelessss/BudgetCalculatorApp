import sys
from PyQt5.QtWidgets import QListWidget, QAbstractItemView


class ExpenseList(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._expenses = []
        self._current_user = None

    def load(self):
        self._expenses = []
        for expense in self._model.expenses():
            if expense.user == self._current_user:
                self._expenses.append(expense)

        self.update()

    def set_current_user(self, user):
        self._current_user = user
        self.load()

    def update(self):
        self.clear()
        for expense in self._expenses:
            self.addItem(expense.to_string())

        self.sortItems(Qt.DescendingOrder)

    def mouseDoubleClickEvent(self, event):
        index = self.indexAt(event.pos())
        if index.isValid():
            expense = self._expenses[index.row()]
            dialog = EditExpenseDialog(self.parent())
            dialog.set_expense(expense)
            if dialog.exec_():
                self.load()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            index = self.currentRow()
            if index >= 0:
                expense = self._expenses[index]
                self._model.delete_expense(expense)
                self.load()
