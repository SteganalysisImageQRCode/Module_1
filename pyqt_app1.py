from PyQt5 import QtWidgets, QtGui, QtCore

import sys
from PyQt5.QtWidgets import QApplication, QWidget,QMessageBox, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
import random
import string

font_but = QtGui.QFont()
font_but.setFamily("Segoe UI Symbol")
font_but.setPointSize(10)
font_but.setWeight(95)


class PushBut1(QtWidgets.QPushButton):
    def __init__(self, parent=None):
        super(PushBut1, self).__init__(parent)
        self.setMouseTracking(True)
        self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,0,0,1); border-style: solid;"
                           "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")

    def enterEvent(self, event):
        if self.isEnabled() is True:
            self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,230,255,255);"
                               "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,230,255,255);")
        if self.isEnabled() is False:
            self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
                               "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")

    def leaveEvent(self, event):
        self.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,255,100); color: rgba(0,190,255,255); border-style: solid;"
                           "border-radius: 3px; border-width: 0.5px; border-color: rgba(127,127,255,255);")


class PyQtApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowTitle("Steganalysis Application")
        self.setWindowIcon(QtGui.QIcon("Path/to/Your/image/file.png"))
        self.setMinimumWidth(resolution.width() / 3)
        self.setMinimumHeight(resolution.height() / 2)
        self.setStyleSheet("QWidget {background-color: rgba(255,255,255,1);} QScrollBar:horizontal {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);} QScrollBar:vertical {width: 1px; height: 1px;"
                           "background-color: rgba(0,41,59,255);}")
        self.textf = QtWidgets.QTextEdit(self)
        self.textf.setPlaceholderText("Select files...")
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(0,255,255,100); color: rgba(0,190,255,255);"
                                 "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        #self.textbox.setText('choose a file')
        
        self.but1 = PushBut1(self)
        self.but1.setText("Attach files")
        self.but1.setFixedWidth(94)
        self.but1.setFont(font_but)
        self.but2 = PushBut1(self)
        self.but2.setText("Encrypt")
        self.but2.setFixedWidth(94)
        self.but2.setFont(font_but)
        self.but3 = PushBut1(self)
        self.but3.setText("Cancel")
        self.but3.setFixedWidth(94)
        self.but3.setFont(font_but)
    
        self.lb1 = QtWidgets.QLabel(self)
        self.lb1.setFixedWidth(72)
        self.lb1.setFixedHeight(74)
        self.grid1 = QtWidgets.QGridLayout()
        self.grid1.addWidget(self.textf, 0, 0, 14, 13)
        self.grid1.addWidget(self.but1, 0, 14, 1, 1)
        self.grid1.addWidget(self.but2, 1, 14, 1,2)
        self.grid1.addWidget(self.but3, 2, 14, 1, 1)
        
        self.grid1.addWidget(self.lb1, 12, 14, 1, 1)
        self.grid1.setContentsMargins(7, 7, 7, 7)
        self.setLayout(self.grid1)
        self.but1.clicked.connect(self.on_but1)
        self.but2.clicked.connect(self.on_but2)
        self.but3.clicked.connect(self.on_but3)
    
    def on_but1(self, main_window):
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,217,100); color: rgba(0,0,0,1);"
                                 "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()",options=options)
        t = filename[0]
        self.textbox.setText(t)

    
        
        
    def on_but2(self, main_window):
        self.textf.setStyleSheet("margin: 1px; padding: 7px; background-color: rgba(1,255,217,100); color: rgba(128,0,0,1);"
                                 "border-style: solid; border-radius: 3px; border-width: 0.5px; border-color: rgba(0,140,255,255);")
        QMessageBox.about(self, "Secret Key is generated", "1S2B7M2")
        self.show()
        
    def  on_but3(self):
        self.close()
        QApplication.quit()
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
    myapp = PyQtApp()
    myapp.setWindowOpacity(0.95)
    myapp.show()
    myapp.move(resolution.center() - myapp.rect().center())
    sys.exit(app.exec_())
else:
    desktop = QtWidgets.QApplication.desktop()
    resolution = desktop.availableGeometry()
