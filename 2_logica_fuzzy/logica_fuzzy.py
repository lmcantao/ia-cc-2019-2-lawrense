import sys, desfuzzyfication
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox
from PySide2.QtCore import QFile

def on_hello_pushbutton_clicked():
    #result = desfuzzyfication.get_desfuzzyfication(moneySpinBox.value(), peopleSpinBox.value())
    #result = risco.get_risco(moneySpinBox.value(), peopleSpinBox.value())
    #print(result, '\n')
    resultLabel.setText(desfuzzyfication.get_desfuzzyfication(moneySpinBox.value(), peopleSpinBox.value()))

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("logicafuzzy.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    moneyLabel = window.findChild(QLabel, 'moneyLabel')

    peopleLabel = window.findChild(QLabel, 'peopleLabel')

    riskLabel = window.findChild(QLabel, 'riskLabel')

    resultLabel = window.findChild(QLabel, 'resultLabel')

    moneySpinBox = window.findChild(QSpinBox, 'moneySpinBox')

    peopleSpinBox = window.findChild(QSpinBox, 'peopleSpinBox')

    calculatePushButton = window.findChild(QPushButton, 'calculatePushButton')
    calculatePushButton.clicked.connect(on_hello_pushbutton_clicked)

    window.show()

    sys.exit(app.exec_())