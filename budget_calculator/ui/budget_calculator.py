import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from views.expense_list import ExpenseList
from views.filter_expenses import FilterExpensesDialog
from views.graph_expenses import graph_expenses
from views.login import LoginDialog
from views.register import RegisterDialog
from views.user_profile import UserProfileDialog


class BudgetCalculator(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de presupuesto")

        self._model = BudgetCalculator()

        self._expense_list = ExpenseList(self, self._model)
        self.setCentralWidget(self._expense_list)

        self._add_menus()

        self._initialize()

    def _add_menus(self):

        file_menu = self.menuBar().addMenu("Archivo")
        file_menu.addAction("Nuevo", self._on_new_action)
        file_menu.addAction("Guardar", self._on_save_action)
        file_menu.addAction("Cerrar", self._on_close_action)

        edit_menu = self.menuBar().addMenu("Edición")
        edit_menu.addAction("Editar gasto", self._on_edit_expense_action)
        edit_menu.addAction("Eliminar gasto", self._on_delete_expense_action)

        view_menu = self.menuBar().addMenu("Ver")
        view_menu.addAction("Lista de gastos", self._on_expense_list_action)
        view_menu.addAction("Filtro de gastos", self._on_filter_expenses_action)
        view_menu.addAction("Gráfico de gastos", self._on_graph_expenses_action)

        user_menu = self.menuBar().addMenu("Usuario")
        user_menu.addAction("Iniciar sesión", self._on_login_action)
        user_menu.addAction("Registrarse", self._on_register_action)
        user_menu.addAction("Perfil de usuario", self._on_user_profile_action)

    def _initialize(self):
        self._model.load()

        self._expense_list.setFocus()

    def _on_new_action(self):
        expense_dialog = ExpenseDialog(self)
        if expense_dialog.exec_():
            expense = Expense(
                expense_dialog.amount(), expense_dialog.category(), expense_dialog.date(),
                self._model.current_user()
            )

            self._model.add_expense(expense)

            self._expense_list.update()

    def _on_save_action(self):

        self._model.save()

    def _on_close_action(self):

        if QMessageBox.question(
            self, "Cerrar", "¿Desea guardar los datos antes de cerrar?", QMessageBox.Yes | QMessageBox.No
        ) == QMessageBox.Yes:
            self._model.save()

        self.close()
