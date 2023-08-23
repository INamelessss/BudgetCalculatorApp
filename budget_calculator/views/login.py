import sys
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton


class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Iniciar sesión")

        self.username_edit = QLineEdit()
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")

        main_layout = QVBoxLayout()
        form_layout = QFormLayout()
        form_layout.addRow("Usuario:", self.username_edit)
        form_layout.addRow("Contraseña:", self.password_edit)
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.ok_button)
        main_layout.addWidget(self.cancel_button)
        self.setLayout(main_layout)

        self.ok_button.clicked.connect(self._on_ok_clicked)
        self.cancel_button.clicked.connect(self._on_cancel_clicked)

    def _on_ok_clicked(self):

        username = self.username_edit.text()
        password = self.password_edit.text()

        user = User.authenticate(username, password)
        if user is None:
            QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos.")
            return

        self.parent().current_user = user

        self.close()

    def _on_cancel_clicked(self):

        self.close()
