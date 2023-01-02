from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-100, -20, 1161, 151))
        self.frame.setStyleSheet("background-color: rgb(58, 117, 87);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 50, 561, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(840, 100, 55, 61))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.input_ip_address = QtWidgets.QLineEdit(self.centralwidget)
        self.input_ip_address.setGeometry(QtCore.QRect(40, 160, 241, 41))
        self.input_ip_address.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_ip_address.setInputMask("")
        self.input_ip_address.setText("")
        self.input_ip_address.setAlignment(QtCore.Qt.AlignCenter)
        self.input_ip_address.setObjectName("input_ip_address")
        self.input_fileaddress = QtWidgets.QLineEdit(self.centralwidget)
        self.input_fileaddress.setGeometry(QtCore.QRect(40, 310, 241, 41))
        self.input_fileaddress.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_fileaddress.setInputMask("")
        self.input_fileaddress.setText("")
        self.input_fileaddress.setAlignment(QtCore.Qt.AlignCenter)
        self.input_fileaddress.setObjectName("input_fileaddress")
        self.input_login = QtWidgets.QLineEdit(self.centralwidget)
        self.input_login.setGeometry(QtCore.QRect(40, 410, 241, 41))
        self.input_login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_login.setInputMask("")
        self.input_login.setText("")
        self.input_login.setAlignment(QtCore.Qt.AlignCenter)
        self.input_login.setObjectName("input_login")
        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setGeometry(QtCore.QRect(40, 460, 241, 41))
        self.input_password.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_password.setInputMask("")
        self.input_password.setText("")
        self.input_password.setAlignment(QtCore.Qt.AlignCenter)
        self.input_password.setObjectName("input_password")
        self.enter_ip_address = QtWidgets.QPushButton(self.centralwidget)
        self.enter_ip_address.setGeometry(QtCore.QRect(40, 210, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enter_ip_address.setFont(font)
        self.enter_ip_address.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.enter_ip_address.setAutoDefault(False)
        self.enter_ip_address.setDefault(False)
        self.enter_ip_address.setObjectName("enter_ip_address")
        self.enter_fileaddress = QtWidgets.QPushButton(self.centralwidget)
        self.enter_fileaddress.setGeometry(QtCore.QRect(40, 360, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enter_fileaddress.setFont(font)
        self.enter_fileaddress.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.enter_fileaddress.setObjectName("enter_fileaddress")
        self.enter_autorization_DIB = QtWidgets.QPushButton(self.centralwidget)
        self.enter_autorization_DIB.setGeometry(QtCore.QRect(40, 510, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enter_autorization_DIB.setFont(font)
        self.enter_autorization_DIB.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.enter_autorization_DIB.setObjectName("enter_autorization_DIB")
        self.enter_autorization_RNKO = QtWidgets.QPushButton(self.centralwidget)
        self.enter_autorization_RNKO.setGeometry(QtCore.QRect(40, 560, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enter_autorization_RNKO.setFont(font)
        self.enter_autorization_RNKO.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.enter_autorization_RNKO.setObjectName("enter_autorization_RNKO")
        self.download_policies = QtWidgets.QPushButton(self.centralwidget)
        self.download_policies.setGeometry(QtCore.QRect(320, 210, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.download_policies.setFont(font)
        self.download_policies.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.download_policies.setObjectName("download_policies")
        self.download_tasks = QtWidgets.QPushButton(self.centralwidget)
        self.download_tasks.setGeometry(QtCore.QRect(320, 360, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.download_tasks.setFont(font)
        self.download_tasks.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.download_tasks.setObjectName("download_tasks")
        self.download_policies_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.download_policies_from_file.setGeometry(QtCore.QRect(320, 410, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.download_policies_from_file.setFont(font)
        self.download_policies_from_file.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.download_policies_from_file.setObjectName("download_policies_from_file")
        self.download_tasks_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.download_tasks_from_file.setGeometry(QtCore.QRect(320, 460, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.download_tasks_from_file.setFont(font)
        self.download_tasks_from_file.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.download_tasks_from_file.setObjectName("download_tasks_from_file")
        self.dowload_profiles_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.dowload_profiles_from_file.setGeometry(QtCore.QRect(320, 510, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dowload_profiles_from_file.setFont(font)
        self.dowload_profiles_from_file.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.dowload_profiles_from_file.setObjectName("dowload_profiles_from_file")
        self.run_script_for_tasks = QtWidgets.QPushButton(self.centralwidget)
        self.run_script_for_tasks.setGeometry(QtCore.QRect(630, 360, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.run_script_for_tasks.setFont(font)
        self.run_script_for_tasks.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.run_script_for_tasks.setObjectName("run_script_for_tasks")
        self.run_script_for_policies = QtWidgets.QPushButton(self.centralwidget)
        self.run_script_for_policies.setGeometry(QtCore.QRect(630, 310, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.run_script_for_policies.setFont(font)
        self.run_script_for_policies.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.run_script_for_policies.setObjectName("run_script_for_policies")
        self.dowload_settings_from_file = QtWidgets.QPushButton(self.centralwidget)
        self.dowload_settings_from_file.setGeometry(QtCore.QRect(320, 560, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dowload_settings_from_file.setFont(font)
        self.dowload_settings_from_file.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.dowload_settings_from_file.setObjectName("dowload_settings_from_file")
        self.run_scripts_for_profiles = QtWidgets.QPushButton(self.centralwidget)
        self.run_scripts_for_profiles.setGeometry(QtCore.QRect(630, 410, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.run_scripts_for_profiles.setFont(font)
        self.run_scripts_for_profiles.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.run_scripts_for_profiles.setObjectName("run_scripts_for_profiles")
        self.enter_ip_address_2 = QtWidgets.QPushButton(self.centralwidget)
        self.enter_ip_address_2.setGeometry(QtCore.QRect(40, 260, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.enter_ip_address_2.setFont(font)
        self.enter_ip_address_2.setStyleSheet("QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(69, 138, 102);\n"
"    border-radius : 15;\n"
"}\n"
"\n"
"QPushButton: pressed {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(55, 111, 82);\n"
"    border-radius : 15;\n"
"}")
        self.enter_ip_address_2.setObjectName("enter_ip_address_2")
        self.input_last_digit = QtWidgets.QLineEdit(self.centralwidget)
        self.input_last_digit.setGeometry(QtCore.QRect(320, 160, 281, 41))
        self.input_last_digit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_last_digit.setInputMask("")
        self.input_last_digit.setText("")
        self.input_last_digit.setAlignment(QtCore.Qt.AlignCenter)
        self.input_last_digit.setObjectName("input_last_digit")
        self.input_first_digit_task = QtWidgets.QLineEdit(self.centralwidget)
        self.input_first_digit_task.setGeometry(QtCore.QRect(320, 260, 281, 41))
        self.input_first_digit_task.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_first_digit_task.setInputMask("")
        self.input_first_digit_task.setText("")
        self.input_first_digit_task.setAlignment(QtCore.Qt.AlignCenter)
        self.input_first_digit_task.setObjectName("input_first_digit_task")
        self.input_last_digit_task = QtWidgets.QLineEdit(self.centralwidget)
        self.input_last_digit_task.setGeometry(QtCore.QRect(320, 310, 281, 41))
        self.input_last_digit_task.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(78, 156, 116);\n"
"border-radius: 15;\n"
"color: rgb(0, 0, 0);")
        self.input_last_digit_task.setInputMask("")
        self.input_last_digit_task.setText("")
        self.input_last_digit_task.setAlignment(QtCore.Qt.AlignCenter)
        self.input_last_digit_task.setObjectName("input_last_digit_task")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(610, 0, 291, 281))
        self.frame_2.setStyleSheet("background-color: rgb(58, 117, 87);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 271, 261))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("convert.jpg"))
        self.label_7.setObjectName("label_7")
        self.author = QtWidgets.QLabel(self.centralwidget)
        self.author.setGeometry(QtCore.QRect(640, 580, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.author.setFont(font)
        self.author.setStyleSheet("color: rgb(255, 255, 255);")
        self.author.setAlignment(QtCore.Qt.AlignCenter)
        self.author.setObjectName("author")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kaspersky Security Center Analyzer"))
        self.label.setText(_translate("MainWindow", "Kaspersky Security Center Analyzer"))
        self.enter_ip_address.setText(_translate("MainWindow", "Подключиться к серверу"))
        self.enter_fileaddress.setText(_translate("MainWindow", "Ввод"))
        self.enter_autorization_DIB.setText(_translate("MainWindow", "Авторизоваться-DIB"))
        self.enter_autorization_RNKO.setText(_translate("MainWindow", "Авторизоваться-RNKO"))
        self.download_policies.setText(_translate("MainWindow", "Собрать данные из раздела \"Политики\""))
        self.download_tasks.setText(_translate("MainWindow", "Собрать данные из раздела \"Задачи\""))
        self.download_policies_from_file.setText(_translate("MainWindow", "Загрузить словарь политик из файла"))
        self.download_tasks_from_file.setText(_translate("MainWindow", "Загрузить словарь задач из файла"))
        self.dowload_profiles_from_file.setText(_translate("MainWindow", "Загрузить словарь профилей из файла"))
        self.run_script_for_tasks.setText(_translate("MainWindow", "Запуск скрипта для задач"))
        self.run_script_for_policies.setText(_translate("MainWindow", "Запуск скрипта для политик"))
        self.dowload_settings_from_file.setText(_translate("MainWindow", "Загрузить словарь настроек из файла"))
        self.run_scripts_for_profiles.setText(_translate("MainWindow", "Запуск скрипта для профилей"))
        self.enter_ip_address_2.setText(_translate("MainWindow", "Отключиться от сервера"))
        self.author.setText(_translate("MainWindow", "author by Bibikov Daniil"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
