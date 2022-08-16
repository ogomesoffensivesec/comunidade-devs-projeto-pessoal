from PyQt5 import QtCore, QtGui, QtWidgets
import cadastro
from PyQt5.QtWidgets import QMessageBox


class Ui_tela_registro(object):
    def setupUi(self, tela_registro):
        tela_registro.setObjectName("tela_registro")
        tela_registro.resize(491, 643)
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(14)
        tela_registro.setFont(font)
        tela_registro.setStyleSheet("background-color: #313866;\n"
                                    "\n"
                                    "")
        self.centralwidget = QtWidgets.QWidget(tela_registro)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_finalizarcadastro = QtWidgets.QPushButton(self.centralwidget)
        self.btn_finalizarcadastro.setGeometry(QtCore.QRect(130, 550, 251, 51))
        self.btn_finalizarcadastro.setStyleSheet("QPushButton{\n"
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
        self.btn_finalizarcadastro.setObjectName("btn_finalizarcadastro")
        self.input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_name.setGeometry(QtCore.QRect(40, 120, 401, 41))
        self.input_name.setStyleSheet("QLineEdit{\n"
                                      "    border:none;\n"
                                      "    color: white;\n"
                                      "    background-color: #964EC2;\n"
                                      "    padding: 10px;\n"
                                      "    border-radius: 20px;\n"
                                      "}\n"
                                      "QLineEdit:hover{\n"
                                      "\n"
                                      "    border: 2px solid  #FF7BBF;\n"
                                      "    }\n"
                                      "\n"
                                      "QLineEdit:focus{\n"
                                      "\n"
                                      "    border: 2px solid   #964EC2;\n"
                                      "    color: #313866;\n"
                                      "    background-color:white;\n"
                                      "\n"
                                      "}\n"
                                      "")
        self.input_name.setText("")
        self.input_name.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.input_name.setClearButtonEnabled(False)
        self.input_name.setObjectName("input_name")
        self.input_email = QtWidgets.QLineEdit(self.centralwidget)
        self.input_email.setGeometry(QtCore.QRect(40, 190, 401, 41))
        self.input_email.setStyleSheet("QLineEdit{\n"
                                       "    border:none;\n"
                                       "    color: white;\n"
                                       "    background-color: #964EC2;\n"
                                       "    padding: 10px;\n"
                                       "    border-radius: 20px;\n"
                                       "}\n"
                                       "QLineEdit:hover{\n"
                                       "\n"
                                       "    border: 2px solid  #FF7BBF;\n"
                                       "    }\n"
                                       "\n"
                                       "QLineEdit:focus{\n"
                                       "\n"
                                       "    border: 2px solid   #964EC2;\n"
                                       "    color: #313866;\n"
                                       "    background-color:white;\n"
                                       "\n"
                                       "}\n"
                                       "")
        self.input_email.setText("")
        self.input_email.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.input_email.setClearButtonEnabled(False)
        self.input_email.setObjectName("input_email")
        self.input_confirmpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.input_confirmpassword.setGeometry(QtCore.QRect(40, 400, 401, 41))
        self.input_confirmpassword.setStyleSheet("QLineEdit{\n"
                                                 "    border:none;\n"
                                                 "    color: white;\n"
                                                 "    background-color: #964EC2;\n"
                                                 "    padding: 10px;\n"
                                                 "    border-radius: 20px;\n"
                                                 "}\n"
                                                 "QLineEdit:hover{\n"
                                                 "\n"
                                                 "    border: 2px solid  #FF7BBF;\n"
                                                 "    }\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "\n"
                                                 "    border: 2px solid   #964EC2;\n"
                                                 "    color: #313866;\n"
                                                 "    background-color:white;\n"
                                                 "\n"
                                                 "}\n"
                                                 "")
        self.input_confirmpassword.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.input_confirmpassword.setText("")
        self.input_confirmpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_confirmpassword.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.input_confirmpassword.setReadOnly(False)
        self.input_confirmpassword.setClearButtonEnabled(False)
        self.input_confirmpassword.setObjectName("input_confirmpassword")
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(40, 330, 401, 41))
        self.input_password.setStyleSheet("QLineEdit{\n"
                                          "    border:none;\n"
                                          "    color: white;\n"
                                          "    background-color: #964EC2;\n"
                                          "    padding: 10px;\n"
                                          "    border-radius: 20px;\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "\n"
                                          "    border: 2px solid  #FF7BBF;\n"
                                          "    }\n"
                                          "\n"
                                          "QLineEdit:focus{\n"
                                          "\n"
                                          "    border: 2px solid   #964EC2;\n"
                                          "    color: #313866;\n"
                                          "    background-color:white;\n"
                                          "\n"
                                          "}\n"
                                          "")
        self.input_password.setInputMethodHints(
            QtCore.Qt.ImhHiddenText | QtCore.Qt.ImhNoAutoUppercase | QtCore.Qt.ImhNoPredictiveText | QtCore.Qt.ImhSensitiveData)
        self.input_password.setText("")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.input_password.setReadOnly(False)
        self.input_password.setClearButtonEnabled(False)
        self.input_password.setObjectName("input_password")
        self.input_telefone = QtWidgets.QLineEdit(self.centralwidget)
        self.input_telefone.setGeometry(QtCore.QRect(40, 260, 401, 41))
        self.input_telefone.setStyleSheet("QLineEdit{\n"
                                          "    border:none;\n"
                                          "    color: white;\n"
                                          "    background-color: #964EC2;\n"
                                          "    padding: 10px;\n"
                                          "    border-radius: 20px;\n"
                                          "}\n"
                                          "QLineEdit:hover{\n"
                                          "\n"
                                          "    border: 2px solid  #FF7BBF;\n"
                                          "    }\n"
                                          "\n"
                                          "QLineEdit:focus{\n"
                                          "\n"
                                          "    border: 2px solid   #964EC2;\n"
                                          "    color: #313866;\n"
                                          "    background-color:white;\n"
                                          "\n"
                                          "}\n"
                                          "")
        self.input_telefone.setText("")
        self.input_telefone.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.input_telefone.setClearButtonEnabled(False)
        self.input_telefone.setObjectName("input_telefone")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Gotham Black")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 470, 401, 40))
        self.comboBox.setStyleSheet("QComboBox{\n"
                                    "    border:none;\n"
                                    "    color: white;\n"
                                    "    background-color: #964EC2;\n"
                                    "    padding: 10px;\n"
                                    "    border-radius: 20px;\n"
                                    "}\n"
                                    "QLineEdit:hover{\n"
                                    "\n"
                                    "    border: 2px solid  #FF7BBF;\n"
                                    "    }\n"
                                    "\n"
                                    "QLineEdit:focus{\n"
                                    "\n"
                                    "    border: 2px solid   #964EC2;\n"
                                    "    color: #313866;\n"
                                    "    background-color:white;\n"
                                    "\n"
                                    "}\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        tela_registro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tela_registro)
        self.statusbar.setObjectName("statusbar")
        tela_registro.setStatusBar(self.statusbar)

        self.retranslateUi(tela_registro)
        QtCore.QMetaObject.connectSlotsByName(tela_registro)
        self.btn_finalizarcadastro.clicked.connect(self.function_cadastro)

    def function_cadastro(self):
        name = str(self.input_name.text())
        email = str(self.input_email.text())
        tel = str(self.input_telefone.text())
        passwd = str(self.input_password.text())
        confirmpasswd = str(self.input_confirmpassword.text())
        combo = self.comboBox.currentText()
        validation_pass = cadastro.validarpass(passwd, confirmpasswd)
        validation_email = cadastro.validate_email(email)
        if (validation_pass == False):
            msg = QMessageBox()
            msg.setIcon(msg.Information)
            msg.setWindowTitle('Erro')
            msg.setText('As senhas não coincidem!')
            msg.exec()
        elif (validation_email == False):
            msg = QMessageBox()
            msg.setIcon(msg.Information)
            msg.setWindowTitle('Erro!')
            msg.setText('E-mail inválido!')
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(msg.Information)
            msg.setWindowTitle('Sucesso')
            msg.setText('Cadastro realizado com sucesso')
            msg.exec()

    def retranslateUi(self, tela_registro):
        _translate = QtCore.QCoreApplication.translate
        tela_registro.setWindowTitle(_translate("tela_registro", "Registro"))
        self.btn_finalizarcadastro.setText(
            _translate("tela_registro", "Concluir cadastro"))
        self.input_name.setPlaceholderText(_translate(
            "tela_registro", "Como podemos te chamar?"))
        self.input_email.setPlaceholderText(
            _translate("tela_registro", "Digite o seu email"))
        self.input_confirmpassword.setPlaceholderText(
            _translate("tela_registro", "Repita a senha"))
        self.input_password.setPlaceholderText(
            _translate("tela_registro", "Digite uma senha"))
        self.input_telefone.setPlaceholderText(
            _translate("tela_registro", "Telefone"))
        self.label.setText(_translate(
            "tela_registro", "Bem-Vindo (a) ao time Academy Dev\'s"))
        self.comboBox.setItemText(0, _translate(
            "tela_registro", "Não sei nada sobre desenvolvimento de softwares"))
        self.comboBox.setItemText(1, _translate(
            "tela_registro", "Tenho um conhecimento básico"))
        self.comboBox.setItemText(2, _translate(
            "tela_registro", "Consigo desenvolver pequenos projetos"))
        self.comboBox.setItemText(3, _translate(
            "tela_registro", "Consigo desenvolver projetos reais"))
        self.comboBox.setItemText(
            4, _translate("tela_registro", "Sou Master!"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCadastro = QtWidgets.QMainWindow()
    ui = Ui_tela_registro()
    ui.setupUi(TelaCadastro)
    TelaCadastro.show()
    sys.exit(app.exec_())
