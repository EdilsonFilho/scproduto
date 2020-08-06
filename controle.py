from PyQt5 import QtWidgets, uic
import sys

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    
    print("Codigo:",linha1)
    print("Descricao",linha2)
    print("Preço:",linha3)

    if formulario.radioButton.isChecked():
        print("Categoria ceral")
    elif formulario.radioButton_2.isChecked():
        print("Categoria Grão ")
    else:             
        print("Categoria Pó")


app=QtWidgets.QApplication([])
formulario= uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()