import sys
from PyQt5.QtWidgets import QDialog, QLineEdit, QDateEdit


class FilterExpensesDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Filtrar gastos")

        self.category_edit = QLineEdit()
        self.date_from_edit = QDateEdit()
        self.date_to_edit = QDateEdit()

        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow("Categoría:", self.category_edit)
        form_layout.addRow("Fecha desde:", self.date_from_edit)
        form_layout.addRow("Fecha hasta:", self.date_to_edit)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.ok_button)
        main_layout.addWidget(self.cancel_button)
        self.setLayout(main_layout)

        self.ok_button.clicked.connect(self._on_ok_clicked)
        self.cancel_button.clicked.connect(self._on_cancel_clicked)

    def _on_ok_clicked(self):

        category = self.category_edit.text()
        date_from = self.date_from_edit.date()
        date_to = self.date_to_edit.date()

        filter = ExpenseFilter(category, date_from, date_to)

        self.close()

        self.parent().filter_expenses(filter)

    def _on_cancel_clicked(self):

        self.close()
