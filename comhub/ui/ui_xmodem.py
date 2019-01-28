from PyQt4 import QtCore, QtGui

try:
    _from_utf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _from_utf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


# noinspection PyArgumentList
class UiDialogXmodem(object):
    def __init__(self):
        self.gridLayout_central = None
        self.label_proc = None
        self.progress_bar = None
        self.buttonBox = None
        self.label_cmd = None
        self.lineEdit_cmd = None
        self.label_timeout = None
        self.lineEdit_timeout = None
        self.label_image = None
        self.lineEdit_image = None
        self.pushButton_image = None
        self.groupBox_envs = None
        self.gridLayout_file = None
        self.label_error = None
        self.label_total = None
        self.label_success = None
        self.groupBox_proc = None
        self.gridLayout_proc = None
        self.pushButton_start = None

    def setup_ui(self, dialog):
        dialog.setObjectName(_from_utf8("DialogXmodem"))
        dialog.setWindowModality(QtCore.Qt.NonModal)
        dialog.resize(400, 300)
        dialog.setMinimumSize(QtCore.QSize(400, 300))
        dialog.setMaximumSize(QtCore.QSize(400, 300))
        dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowMinimizeButtonHint |
                              QtCore.Qt.WindowMaximizeButtonHint)

        self.gridLayout_central = QtGui.QGridLayout(dialog)
        self.gridLayout_central.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_central.setObjectName("gridLayoutCentral")

        self.groupBox_envs = QtGui.QGroupBox(dialog)
        self.groupBox_envs.setObjectName(_from_utf8("groupBox_envs"))
        self.gridLayout_central.addWidget(self.groupBox_envs, 0, 0, 5, 1)

        self.gridLayout_file = QtGui.QGridLayout(self.groupBox_envs)
        self.gridLayout_file.setContentsMargins(12, 0, 12, 6)

        self.label_image = QtGui.QLabel(dialog)
        self.label_image.setObjectName(_from_utf8("label_image"))
        self.gridLayout_file.addWidget(self.label_image, 1, 0, 1, 1)

        self.lineEdit_image = QtGui.QLineEdit(dialog)
        self.lineEdit_image.setObjectName(_from_utf8("lineEdit_image"))
        self.gridLayout_file.addWidget(self.lineEdit_image, 2, 0, 1, 5)

        self.pushButton_image = QtGui.QPushButton(dialog)
        self.pushButton_image.setObjectName(_from_utf8("pushButton_image"))
        self.gridLayout_file.addWidget(self.pushButton_image, 2, 5, 1, 1)

        self.label_cmd = QtGui.QLabel(dialog)
        self.label_cmd.setObjectName(_from_utf8("label_cmd"))
        self.gridLayout_file.addWidget(self.label_cmd, 3, 0, 1, 3)

        self.label_timeout = QtGui.QLabel(dialog)
        self.label_timeout.setObjectName(_from_utf8("label_timeout"))
        self.gridLayout_file.addWidget(self.label_timeout, 3, 3, 1, 3)

        self.lineEdit_cmd = QtGui.QLineEdit(dialog)
        self.lineEdit_cmd.setObjectName(_from_utf8("lineEdit_cmd"))
        self.gridLayout_file.addWidget(self.lineEdit_cmd, 4, 0, 1, 3)

        self.lineEdit_timeout = QtGui.QLineEdit(dialog)
        self.lineEdit_timeout.setObjectName(_from_utf8("lineEdit_timeout"))
        self.lineEdit_timeout.setInputMask("9999")
        self.gridLayout_file.addWidget(self.lineEdit_timeout, 4, 3, 1, 3)

        self.groupBox_proc = QtGui.QGroupBox(dialog)
        self.groupBox_proc.setObjectName(_from_utf8("groupBox_proc"))
        self.gridLayout_central.addWidget(self.groupBox_proc, 5, 0, 4, 1)

        self.gridLayout_proc = QtGui.QGridLayout(self.groupBox_proc)
        self.gridLayout_proc.setContentsMargins(12, 0, 12, 6)

        self.label_proc = QtGui.QLabel(dialog)
        self.label_proc.setObjectName(_from_utf8("label_proc"))
        self.gridLayout_proc.addWidget(self.label_proc, 1, 0, 1, 1)

        self.progress_bar = QtGui.QProgressBar(dialog)
        self.progress_bar.setObjectName(_from_utf8("processBar"))
        self.gridLayout_proc.addWidget(self.progress_bar, 2, 0, 1, 3)

        self.label_total = QtGui.QLabel(dialog)
        self.label_total.setObjectName(_from_utf8("label_total"))
        self.gridLayout_proc.addWidget(self.label_total, 3, 0, 1, 1)

        self.label_success = QtGui.QLabel(dialog)
        self.label_success.setObjectName(_from_utf8("label_success"))
        self.gridLayout_proc.addWidget(self.label_success, 3, 1, 1, 1)

        self.label_error = QtGui.QLabel(dialog)
        self.label_error.setObjectName(_from_utf8("label_error"))
        self.gridLayout_proc.addWidget(self.label_error, 3, 2, 1, 1)

        self.pushButton_start = QtGui.QPushButton(dialog)
        self.pushButton_start.setObjectName(_from_utf8("pushButton_start"))

        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.addButton(self.pushButton_start, QtGui.QDialogButtonBox.AcceptRole)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_from_utf8("buttonBox"))
        self.gridLayout_central.addWidget(self.buttonBox)

        self.retranslate_ui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Xmodem Send", None))
        self.groupBox_envs.setTitle(_translate("dialog", "Setup:", None))
        self.label_image.setText(_translate("dialog", "Image:", None))
        self.label_cmd.setText(_translate("dialog", "Command:", None))
        self.label_timeout.setText(_translate("dialog", "Timeout(ms):", None))

        self.groupBox_proc.setTitle(_translate("dialog", "Status:", None))
        self.label_proc.setText(_translate("dialog", "Progress:", None))
        self.pushButton_image.setText(_translate("dialog", "Open", None))
        self.pushButton_start.setText(_translate("dialog", "Start", None))
        self.label_total.setText(_translate("dialog", "Total: 0", None))
        self.label_error.setText(_translate("dialog", "Error: 0", None))
        self.label_success.setText(_translate("dialog", "Success: 0", None))
