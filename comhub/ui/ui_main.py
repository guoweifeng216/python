import os
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject
from PyQt4.QtGui import QTextCursor, QKeySequence, QIcon, QCursor

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


class Class(object):
    pass


class Tab(QObject):
    def __init__(self, obj, name, envs):
        super(Tab, self).__init__()

        self.obj = obj
        self.envs = envs
        self.name = name
        self.widget = self.obj.tab_widget

        self.tab = None
        self.text = None

        self.log_path = ""
        self.log_size = ""
        self.text_line = "Line: {}".format(envs["TEXTMAXLINE"])
        self.hub_port = "Port: {}".format(envs["PORT"])
        self.conn_cnt = "Connect: 0"

    def add_tab(self):
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab_{}".format(self.name))

        layout = QtGui.QGridLayout(self.tab)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.setObjectName("gridLayout_tab")

        self.text = QtGui.QPlainTextEdit(self.tab)
        self.text.setObjectName("plainTextEdit_{}".format(self.name))
        self.text.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.text.setMaximumBlockCount(self.envs["TEXTMAXLINE"])
        self.text.setAcceptDrops(False)
        self.text.setCursorWidth(1)
        self.text.selectionChanged.connect(self.select_text)
        layout.addWidget(self.text, 0, 0, 1, 1)

        self.widget.addTab(self.tab, self.name)
        self.set_focus()

    def remove_tab(self):
        self.widget.removeTab(self.widget.indexOf(self.tab))
        self.tab = None
        self.text = None

    def update_status_size(self, size):
        if self.widget.indexOf(self.tab) == self.widget.currentIndex():
            self.log_size = "Size: {} MB".format(size)
            self.obj.status_size.setText(self.log_size)

    def update_status_path(self, path):
        if self.widget.indexOf(self.tab) == self.widget.currentIndex():
            self.log_path = "Log: {}".format(path)
            self.obj.status_path.setText(self.log_path)

    def update_status_count(self, count):
        if self.widget.indexOf(self.tab) == self.widget.currentIndex():
            self.conn_cnt = "Connect: {}".format(count)
            self.obj.status_count.setText(self.conn_cnt)

    def update_status(self):
        self.obj.status_size.setText(self.log_size)
        self.obj.status_path.setText(self.log_path)
        self.obj.status_port.setText(self.hub_port)
        self.obj.status_line.setText(self.text_line)
        self.obj.status_count.setText(self.conn_cnt)

    def install_event_filter(self, func):
        self.text.installEventFilter(func)

    def select_text(self):
        self.text.copy()

    def set_focus(self):
        self.widget.setCurrentWidget(self.tab)
        self.text.setFocus()

    def append(self, data):
        self.text.moveCursor(QTextCursor.End)
        self.text.insertPlainText(data)
        self.text.moveCursor(QTextCursor.End)

    def backspace(self, count=1):
        self.text.moveCursor(QTextCursor.End)
        cursor = self.text.textCursor()
        for _ in range(count):
            cursor.deletePreviousChar()
        self.text.setTextCursor(cursor)


# noinspection PyArgumentList
class UiMainWindow(object):
    def __init__(self):
        self.window = None
        self.widget = dict()
        self.central_widget = None
        self.gridLayout_central = None
        self.tab_widget = None
        self.menu_bar = None
        self.menu_file = None
        self.menu_edit = None
        self.menu_trans = None
        self.status_bar = None
        self.action_open = None
        self.action_close = None
        self.action_resize = None
        self.action_reload = None
        self.action_trans = None
        self.status_path = None
        self.status_size = None
        self.status_port = None
        self.status_line = None
        self.status_count = None
        self.action_switchTab = None

    def setup_ui(self, window):
        self.window = window
        window.setObjectName("MainWindow")
        window.resize(960, 720)
        window.setWindowIcon(QIcon(os.path.join("icon", "main.png")))
        # window.setStyleSheet(_from_utf8('font-family: "DejaVu Sans Mono";'))

        self.central_widget = QtGui.QWidget(window)
        self.central_widget.setObjectName("centralWidget")
        self.gridLayout_central = QtGui.QGridLayout(self.central_widget)
        self.gridLayout_central.setContentsMargins(2, 1, 0, 0)
        self.gridLayout_central.setObjectName("gridLayoutCentral")
        self.gridLayout_central.setSpacing(0)
        self.tab_widget = QtGui.QTabWidget(self.central_widget)
        self.tab_widget.setEnabled(True)
        self.tab_widget.setObjectName("tabWidget")
        self.tab_widget.currentChanged.connect(self.update_status)
        self.gridLayout_central.addWidget(self.tab_widget, 0, 0, 1, 1)
        window.setCentralWidget(self.central_widget)

        self.menu_bar = QtGui.QMenuBar(window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menu_bar.setObjectName("menuBar")
        window.setMenuBar(self.menu_bar)

        self.menu_file = QtGui.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menuFile")

        self.menu_edit = QtGui.QMenu(self.menu_bar)
        self.menu_edit.setObjectName("menuEdit")

        self.menu_trans = QtGui.QMenu(self.menu_bar)
        self.menu_trans.setObjectName("menuTrans")

        self.status_bar = QtGui.QStatusBar(window)
        self.status_bar.setObjectName("statusBar")
        window.setStatusBar(self.status_bar)

        self.status_path = QtGui.QLabel(self.status_bar)
        self.status_path.setObjectName("statusPath")
        self.status_bar.addWidget(self.status_path)

        self.status_port = QtGui.QLabel(self.status_bar)
        self.status_port.setObjectName("statusPort")
        self.status_bar.addPermanentWidget(self.status_port)

        self.status_line = QtGui.QLabel(self.status_bar)
        self.status_line.setObjectName("statusLine")
        self.status_bar.addPermanentWidget(self.status_line)

        self.status_count = QtGui.QLabel(self.status_bar)
        self.status_count.setObjectName("statusCount")
        self.status_bar.addPermanentWidget(self.status_count)

        self.status_size = QtGui.QLabel(self.status_bar)
        self.status_size.setObjectName("statusSize")
        self.status_bar.addPermanentWidget(self.status_size)

        self.action_open = QtGui.QAction(window)
        self.action_open.setObjectName("actionOpen")
        self.action_open.setShortcut(QKeySequence.Open)
        self.action_close = QtGui.QAction(window)
        self.action_close.setObjectName("actionClose")
        self.action_close.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_W)
        self.action_resize = QtGui.QAction(window)
        self.action_resize.setObjectName("actionResize")
        self.action_resize.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_R)
        self.action_resize.triggered.connect(self.resize)
        self.action_reload = QtGui.QAction(window)
        self.action_reload.setObjectName("actionReload")
        self.action_reload.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_L)
        self.action_switchTab = QtGui.QAction(window)
        self.action_switchTab.setObjectName("actionSwitchTab")
        self.action_switchTab.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_Tab)
        self.action_switchTab.triggered.connect(self.switch_tab)
        self.action_trans = QtGui.QAction(window)
        self.action_trans.setObjectName("actionTrans")
        self.action_trans.setShortcut(QtCore.Qt.CTRL + QtCore.Qt.Key_T)

        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_close)
        self.menu_file.addAction(self.action_resize)
        self.menu_file.addAction(self.action_reload)
        self.menu_edit.addAction(self.action_switchTab)
        self.menu_trans.addAction(self.action_trans)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_edit.menuAction())
        self.menu_bar.addAction(self.menu_trans.menuAction())

        self.retranslate_ui(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslate_ui(self, window):
        window.setWindowTitle(_translate("MainWindow", "ComHub", None))
        self.menu_file.setTitle(_translate("MainWindow", "File(&F)", None))
        self.menu_edit.setTitle(_translate("MainWindow", "Edit(&E)", None))
        self.menu_trans.setTitle(_translate("MainWindow", "Trans(&T)", None))
        self.action_open.setText(_translate("MainWindow", "Open(O)", None))
        self.action_close.setText(_translate("MainWindow", "Close(W)", None))
        self.action_resize.setText(_translate("MainWindow", "Resize(R)", None))
        self.action_reload.setText(_translate("MainWindow", "Reload(L)", None))
        self.action_switchTab.setText(_translate("MainWindow", "Switch Tab(Tab)", None))
        self.action_trans.setText(_translate("MainWindow", "Xmodem Send(T)", None))

    def resize(self):
        self.window.resize(960, 720)

    def add_tab(self, name, envs):
        self.widget[name] = Tab(self, name, envs)
        self.widget[name].add_tab()
        return self.widget[name]

    def remove_tab(self, name):
        self.widget[name].remove_tab()
        del self.widget[name]

    def get_tab_name(self, index):
        return str(self.tab_widget.tabText(index))

    def get_tab_cur_name(self):
        return str(self.tab_widget.tabText(self.tab_widget.currentIndex()))

    def update_status(self, index):
        if index != -1:
            name = self.get_tab_name(index)
            self.widget[name].update_status()
        else:
            self.status_size.setText("")
            self.status_path.setText("")
            self.status_port.setText("")
            self.status_line.setText("")
            self.status_count.setText("")

    def switch_tab(self):
        for i in range(self.tab_widget.currentIndex() + 1, self.tab_widget.count()):
            self.tab_widget.setCurrentIndex(i)
            break
        else:
            self.tab_widget.setCurrentIndex(0)
