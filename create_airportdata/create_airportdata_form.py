import sys
import os
import datetime
import traceback
import adsb_mainForm
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = adsb_mainForm.Ui_MainWindow()
        self.ui.setupUi(self)
        #装载更多控件
        url = os.getcwd() + '/tt.html'
        self.browser = QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))
        self.ui.horizontalLayout_3.addWidget(self.browser)
        self.ui.tabWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tabWidget.customContextMenuRequested.connect(self.custom_right_menu)
        self.time_label= QLabel('')
        self.statusBar().addPermanentWidget(self.time_label,stretch=1)
        timer_a = QTimer(self)
        timer_a.timeout.connect(self.update_time)
        timer_a.start()

    def update_time(self):
        current_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.time_label.setText(current_Time)

    def custom_right_menu(self, pos):
        try:
            menu = QMenu()
            opt1 = menu.addAction("+")
            opt2 = menu.addAction("-")
            action = menu.exec_(self.ui.tabWidget.mapToGlobal(pos))
            if action == opt1:
                print(1)
                return
            elif action == opt2:
                print(2)
                return
            else:
                return
        except:
            traceback.print_exc()
if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
