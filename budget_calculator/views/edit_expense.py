import sys
from PyQt5.QtWidgets import QDialog, QLineEdit, QDateEdit, QMessageBox


class EditExpenseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Editar gasto")

        self.amount_edit = QLineEdit()
        self.category_edit = QLineEdit()
        self.date_edit = QDateEdit()

        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow("Monto:", self.amount_edit)
        form_layout.addRow("Categoría:", self.category_edit)
        form_layout.addRow("Fecha:", self.date_edit)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.ok_button)
        main_layout.addWidget(self.cancel_button)
        self.setLayout(main_layout)

        self.ok_button.clicked.connect(self._on_ok_clicked)
        self.cancel_button.clicked.connect(self._on_cancel_clicked)

    def _on_ok_clicked(self):

        amount = float(self.amount_edit.text())
        category = self.category_edit.text()
        date = self.date_edit.date()

        expense = Expense(
            amount, category, date, self.parent().current_user()
        )

        self.parent().model().update_expense(expense)

        self.close()

    def _on_cancel_clicked(self):

        self.close()
