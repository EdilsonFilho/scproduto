from PyQt5 import QtWidgets, uic
import sys

def funcao_principal():
    print("teste")


app=QtWidgets.QApplication([])
formulario= uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()