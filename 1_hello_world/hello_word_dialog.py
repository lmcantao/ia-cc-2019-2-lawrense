import sys
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog)

# Subclassing the QDialog class
# Here we are creating our dialog called Form
class Form(QDialog):

    # Constructor of our class
    def __init__(self, parent=None):
        # Calling the constructor of QDialog class
        super(Form, self).__init__(parent)

        # Create widgets
        self.edit = QLineEdit("Escreva seu nome aqui!")
        self.button = QPushButton("Mostrar Cumprimentos")

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        # Set dialog layout
        self.setLayout(layout)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)

    # Create and show the form
    form = Form()
    form.show()

    # Run the main Qt loop
    sys.exit(app.exec_())