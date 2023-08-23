import sys
from PyQt5.QtWidgets import QApplication

from ui.budget_calculator import BudgetCalculator


def main():
    """
    El punto de entrada principal del proyecto.
    """

    # Crea la aplicación.
    app = QApplication(sys.argv)

    # Crea la aplicación de la calculadora de presupuesto.
    budget_calculator_app = BudgetCalculator()

    # Muestra la aplicación.
    budget_calculator_app.show()

    # Inicia la aplicación.
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
