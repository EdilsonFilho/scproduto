from PyQt5 import uic
from PyQt5 import QtWidgets
import sys

def funcao_principal():
    print("teste")


app=QtWidgets.QApplication([])
formulario=uic.loadVi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()