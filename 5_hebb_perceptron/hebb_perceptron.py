import sys

from Hebb import Hebb
from Perceptron import Perceptron

from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction, QSpinBox, QPlainTextEdit, QComboBox
from PySide2.QtCore import QFile

def testaBotao():
    w1.setText("0")
    w2.setText("0")
    wb.setText("0")

    texto = entrada.toPlainText()
    saidas = saida.toPlainText()

    saidasSplit = saidas.split('\n')

    print(saidasSplit)

    saidasInt = []
    for i in range(len(saidasSplit)):
        saidasInt.append(int(saidasSplit[i]))

    print(saidasInt)

    textoSplit1 = texto.split('\n')
    print(textoSplit1)
    qtdText = len(textoSplit1)
    qtdList = 0

    for i in range(len(textoSplit1[0])):
        if textoSplit1[0][i] != " ":
            qtdList = qtdList + 1

    print(qtdList)

    textoSplit2 = ""
    for i in range(qtdText):
        if i == qtdText - 1:
            textoSplit2 = textoSplit2 + textoSplit1[i]
        else:
            textoSplit2 = textoSplit2 + textoSplit1[i] + " "

    print(textoSplit2)

    textoSplit3 = textoSplit2.split()

    print(textoSplit3)

    inputs = []
    lista = []
    controle = 0
    for i in range(len(textoSplit3)):
        lista.append(int(textoSplit3[i]))
        controle = controle + 1
        if (controle == qtdList):
            inputs.append(lista)
            lista = []
            controle = 0

    print(inputs)


    if (funcao.currentText() == "Hebb"):
        hebb = Hebb()
        resp = hebb.learn(inputs, saidasInt)
        w1.setText(str(resp[0]))
        w2.setText(str(resp[1]))
        wb.setText(str(resp[2]))
        epoca.setText('')
        epocaText.setText('')
    else:
        perceptron = Perceptron()
        (resp, epocas) = perceptron.learn(inputs, saidasInt)
        w1.setText(str(resp[0]))
        w2.setText(str(resp[1]))
        wb.setText(str(resp[2]))
        epoca.setText(str(epocas))
        epocaText.setText("Épocas")





if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)

    ui_file = QFile("hebb_perceptron.ui")
    ui_file.open(QFile.ReadOnly)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    entrada = window.findChild(QPlainTextEdit, "entradas")

    saida = window.findChild(QPlainTextEdit, "saidas")

    funcao = window.findChild(QComboBox, "comboBox")

    w1 = window.findChild(QLabel, "w1")
    w2 = window.findChild(QLabel, "w2")
    wb = window.findChild(QLabel, "wb")
    epoca = window.findChild(QLabel, "epocas")
    epocaText = window.findChild(QLabel, "epocaText")

    treino = window.findChild(QPushButton, "treino")
    treino.clicked.connect(testaBotao)

    window.show()

    sys.exit(app.exec_())