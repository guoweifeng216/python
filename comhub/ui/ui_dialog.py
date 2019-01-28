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
class UiDialogSerial(object):
    def __init__(self):
        self.gridLayout_central = None
        self.groupBox_basics = None
        self.gridLayout_basics = None
        self.label_port = None
        self.comboBox_port = None
        self.label_baudrate = None
        self.comboBox_baudrate = None
        self.label_dataBits = None
        self.comboBox_dataBits = None
        self.label_stopBits = None
        self.comboBox_stopBits = None
        self.label_parity = None
        self.comboBox_parity = None
        self.label_flowControl = None
        self.comboBox_flowControl = None
        self.groupBox_text = None
        self.label_linePrefix = None
        self.comboBox_linePrefix = None
        self.label_logPath = None
        self.lineEdit_logPath = None
        self.label_logSize = None
        self.lineEdit_logSize = None
        self.buttonBox = None
        self.gridLayout_text = None
        self.label_textLine = None
        self.lineEdit_textLine = None

    def setup_ui(self, dialog):
        dialog.setObjectName(_from_utf8("DialogSerial"))
        dialog.setWindowModality(QtCore.Qt.NonModal)
        dialog.resize(480, 400)
        dialog.setMinimumSize(QtCore.QSize(480, 400))
        dialog.setMaximumSize(QtCore.QSize(480, 400))
        # dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))

        self.gridLayout_central = QtGui.QGridLayout(dialog)
        self.gridLayout_central.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_central.setObjectName("gridLayoutCentral")

        self.groupBox_basics = QtGui.QGroupBox(dialog)
        self.groupBox_basics.setObjectName(_from_utf8("groupBox_basics"))
        self.gridLayout_central.addWidget(self.groupBox_basics, 0, 0, 7, 1)

        self.gridLayout_basics = QtGui.QGridLayout(self.groupBox_basics)
        self.gridLayout_basics.setContentsMargins(30, 0, 30, 6)

        self.label_port = QtGui.QLabel(self.groupBox_basics)
        self.label_port.setObjectName(_from_utf8("label_port"))
        self.gridLayout_basics.addWidget(self.label_port, 1, 0, 1, 1)

        self.comboBox_port = QtGui.QComboBox(self.groupBox_basics)
        self.comboBox_port.setEditable(True)
        self.comboBox_port.setObjectName(_from_utf8("comboBox_port"))
        self.gridLayout_basics.addWidget(self.comboBox_port, 1, 1, 1, 2)

        self.label_baudrate = QtGui.QLabel(self.groupBox_basics)
        self.label_baudrate.setObjectName(_from_utf8("label_baudrate"))
        self.gridLayout_basics.addWidget(self.label_baudrate, 2, 0, 1, 1)

        self.comboBox_baudrate = QtGui.QComboBox(self.groupBox_basics)
        self.comboBox_baudrate.setEditable(True)
        self.comboBox_baudrate.setObjectName(_from_utf8("comboBox_baudrate"))
        self.gridLayout_basics.addWidget(self.comboBox_baudrate, 2, 1, 1, 2)

        self.label_dataBits = QtGui.QLabel(self.groupBox_basics)
        self.label_dataBits.setObjectName(_from_utf8("label_dataBits"))
        self.gridLayout_basics.addWidget(self.label_dataBits, 3, 0, 1, 1)

        self.comboBox_dataBits = QtGui.QComboBox(self.groupBox_basics)
        self.comboBox_dataBits.setObjectName(_from_utf8("comboBox_dataBits"))
        self.gridLayout_basics.addWidget(self.comboBox_dataBits, 3, 1, 1, 2)

        self.label_stopBits = QtGui.QLabel(self.groupBox_basics)
        self.label_stopBits.setObjectName(_from_utf8("label_stopBits"))
        self.gridLayout_basics.addWidget(self.label_stopBits, 4, 0, 1, 1)

        self.comboBox_stopBits = QtGui.QComboBox(self.groupBox_basics)
        self.comboBox_stopBits.setObjectName(_from_utf8("comboBox_stopBits"))
        self.gridLayout_basics.addWidget(self.comboBox_stopBits, 4, 1, 1, 2)

        self.label_parity = QtGui.QLabel(self.groupBox_basics)
        self.label_parity.setObjectName(_from_utf8("label_parity"))
        self.gridLayout_basics.addWidget(self.label_parity, 5, 0, 1, 1)

        self.comboBox_parity = QtGui.QComboBox(self.groupBox_basics)
        self.comboBox_parity.setObjectName(_from_utf8("comboBox_parity"))
        self.gridLayout_basics.addWidget(self.comboBox_parity, 5, 1, 1, 2)

        self.label_flowControl = QtGui.QLabel(self.groupBox_basics)
        self.label_flowControl.setObjectName(_from_utf8("label_flowControl"))
        self.gridLayout_basics.addWidget(self.label_flowControl, 6, 0, 1, 1)

        self.comboBox_flowControl = QtGui.QComboBox(self.groupBox_basics)
        self.comboBox_flowControl.setObjectName(_from_utf8("comboBox_flowControl"))
        self.gridLayout_basics.addWidget(self.comboBox_flowControl, 6, 1, 1, 2)

        self.groupBox_text = QtGui.QGroupBox(dialog)
        self.groupBox_text.setObjectName(_from_utf8("groupBox_text"))
        self.gridLayout_central.addWidget(self.groupBox_text, 8, 0, 4, 1)

        self.gridLayout_text = QtGui.QGridLayout(self.groupBox_text)
        self.gridLayout_text.setContentsMargins(30, 0, 30, 6)

        self.label_textLine = QtGui.QLabel(self.groupBox_text)
        self.label_textLine.setObjectName(_from_utf8("label_textLine"))
        self.gridLayout_text.addWidget(self.label_textLine, 1, 0, 1, 1)

        self.lineEdit_textLine = QtGui.QLineEdit(self.groupBox_text)
        self.lineEdit_textLine.setInputMask("999999")
        self.lineEdit_textLine.setMaxLength(5)
        self.lineEdit_textLine.setObjectName(_from_utf8("lineEdit_textLine"))
        self.gridLayout_text.addWidget(self.lineEdit_textLine, 1, 1, 1, 2)

        self.label_linePrefix = QtGui.QLabel(self.groupBox_text)
        self.label_linePrefix.setObjectName(_from_utf8("label_linePrefix"))
        self.gridLayout_text.addWidget(self.label_linePrefix, 2, 0, 1, 1)

        self.comboBox_linePrefix = QtGui.QComboBox(self.groupBox_text)
        self.comboBox_linePrefix.setObjectName(_from_utf8("comboBox_linePrefix"))
        self.gridLayout_text.addWidget(self.comboBox_linePrefix, 2, 1, 1, 2)

        self.label_logPath = QtGui.QLabel(self.groupBox_text)
        self.label_logPath.setObjectName(_from_utf8("label_logPath"))
        self.gridLayout_text.addWidget(self.label_logPath, 3, 0, 1, 1)

        self.lineEdit_logPath = QtGui.QLineEdit(self.groupBox_text)
        self.lineEdit_logPath.setObjectName(_from_utf8("lineEdit_logPath"))
        self.gridLayout_text.addWidget(self.lineEdit_logPath, 3, 1, 1, 2)

        self.label_logSize = QtGui.QLabel(self.groupBox_text)
        self.label_logSize.setObjectName(_from_utf8("label_logSize"))
        self.gridLayout_text.addWidget(self.label_logSize, 4, 0, 1, 1)

        self.lineEdit_logSize = QtGui.QLineEdit(self.groupBox_text)
        self.lineEdit_logSize.setInputMask("999.999")
        self.lineEdit_logSize.setMaxLength(6)
        self.lineEdit_logSize.setObjectName(_from_utf8("lineEdit_logSize"))
        self.gridLayout_text.addWidget(self.lineEdit_logSize, 4, 1, 1, 2)

        self.buttonBox = QtGui.QDialogButtonBox(dialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_from_utf8("buttonBox"))
        self.gridLayout_central.addWidget(self.buttonBox)

        self.retranslate_ui(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslate_ui(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Serial Port Configuration", None))
        self.groupBox_basics.setTitle(_translate("dialog", "Serial", None))
        self.label_port.setText(_translate("dialog", "Port:", None))
        self.label_baudrate.setText(_translate("dialog", "Baud Rate:", None))
        self.label_parity.setText(_translate("dialog", "Parity:", None))
        self.label_dataBits.setText(_translate("dialog", "Data Bits:", None))
        self.label_stopBits.setText(_translate("dialog", "Stop Bits:", None))
        self.label_flowControl.setText(_translate("dialog", "Flow Control:", None))

        self.groupBox_text.setTitle(_translate("dialog", "Common", None))
        self.label_textLine.setText(_translate("dialog", "Text Max Line:", None))
        self.label_linePrefix.setText(_translate("dialog", "Line Prefix:", None))
        self.label_logPath.setText(_translate("dialog", "Log Path:", None))
        self.label_logSize.setText(_translate("dialog", "Log Max Size(MB):", None))
