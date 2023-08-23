import sys
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit


class UserProfileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Perfil de usuario")

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()

        self.name_label = QLabel("Nombre:")
        self.email_label = QLabel("Email:")

        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow(self.name_label, self.name_edit)
        form_layout.addRow(self.email_label, self.email_edit)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.ok_button)
        main_layout.addWidget(self.cancel_button)
        self.setLayout(main_layout)

        self.ok_button.clicked.connect(self._on_ok_clicked)
        self.cancel_button.clicked.connect(self._on_cancel_clicked)

    def _on_ok_clicked(self):

        name = self.name_edit.text()
        email = self.email_edit.text()

        user = self.parent().current_user
        user.name = name
        user.email = email
        user.save()

        self.close()

    def _on_cancel_clicked(self):

        self.close()
