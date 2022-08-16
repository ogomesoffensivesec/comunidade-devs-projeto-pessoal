from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
import tela_registro


class Ui_tela_principal(object):

    def setupUi(self, tela_principal):
        tela_principal.setObjectName("tela_principal")
        tela_principal.resize(392, 237)
        tela_principal.setStyleSheet("background-color: #313866;\n"
                                     "\n"
                                     "")
        self.centralwidget = QtWidgets.QWidget(tela_principal)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_registro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_registro.setGeometry(QtCore.QRect(40, 80, 311, 51))
        self.btn_registro.setStyleSheet("QPushButton{\n"
                                        "    border:none;\n"
                                        "    color: white;\n"
                                        "    background-color: #964EC2;\n"
                                        "    padding: 10px;\n"
                                        "    border-radius: 20px;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "    border: 2px solid  #FF7BBF;\n"
                                        "    }\n"
                                        "")
        self.btn_registro.setObjectName("btn_registro")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(40, 150, 311, 51))
        self.btn_login.setStyleSheet("QPushButton{\n"
                                     "    border:none;\n"
                                     "    color: white;\n"
                                     "    background-color: #964EC2;\n"
                                     "    padding: 10px;\n"
                                     "    border-radius: 20px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "\n"
                                     "    border: 2px solid  #FF7BBF;\n"
                                     "    }\n"
                                     "")
        self.btn_login.setObjectName("btn_login")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 20, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        tela_principal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tela_principal)
        self.statusbar.setObjectName("statusbar")
        tela_principal.setStatusBar(self.statusbar)

        self.retranslateUi(tela_principal)
        QtCore.QMetaObject.connectSlotsByName(tela_principal)
        self.btn_registro.clicked.connect(self.showTelaRegistro)


    def retranslateUi(self, tela_principal):
        _translate = QtCore.QCoreApplication.translate
        tela_principal.setWindowTitle(
            _translate("tela_principal", "Academy Devs"))
        self.btn_registro.setText(_translate(
            "tela_principal", "Ainda não sou membro!"))
        self.btn_login.setText(_translate("tela_principal", "Já sou membro!"))
        self.label.setText(_translate("tela_principal", "Academy Dev"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Principal = QtWidgets.QMainWindow()
    ui = Ui_tela_principal()
    ui.setupUi(Principal)
    Principal.show()
    sys.exit(app.exec_())
