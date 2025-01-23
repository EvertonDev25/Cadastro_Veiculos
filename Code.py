from PyQt5 import uic, QtWidgets
import mysql.connector

def funcao_principal():
    l1 = formulario.lineEdit.text()
    l2 = formulario.lineEdit_2.text()
    l3 = formulario.lineEdit_3.text()

    print('Dias alugados:{}dias'.format(l1))
    print('Km Rodados:{}km'.format(l2))
    print('Modelo/Veículo: {}'.format(l3))


    conexao = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "cadastro",
    )


    cursor = conexao.cursor()

    comando = "INSERT INTO loja (DiasAlugados, KmRodados, ModeloVeículo) VALUES (%s, %s, %s)"
    values = (l1,l2,l3)
    cursor.execute(comando,values)
    conexao.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("")
    formulario.lineEdit_3.setText("")
    cursor.close()
    conexao.close()


app = QtWidgets.QApplication([])
formulario = uic.loadUi('formulario.ui')
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
