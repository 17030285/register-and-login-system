from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import sys
import g1



conn = sqlite3.connect('F:\sqlitedb\studydb.db')
cursor = conn.cursor()


class tabwidgetDemo(QTabWidget):
    def __init__(self):
        super(tabwidgetDemo,self).__init__()

        self.setWindowTitle("Vacation Management")
        self.resize(800,300)

        #创建用于显示控件的窗口
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
       
        self.addTab(self.tab1,"Offical Holiday")
        self.addTab(self.tab2, "Entitlement")
        self.addTab(self.tab3, "Application")
       

        self.tab1UI()  #初始化第一个选项卡显示页面
        self.tab2UI()
        self.tab3UI()

    #第一个选项卡的页面设置
    def tab1UI(self):
        layout=QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址",QLineEdit())
        self.setTabText(0,"Offical Holiday")  #设置第一个选项卡的标题为联系方式
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout1=QFormLayout()
        sex=QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout1.addRow(QLabel("性别"),sex)
        layout1.addRow("生日",QLineEdit())
        self.setTabText(1,"Entitlement")
        self.tab2.setLayout(layout1)

    def tab3UI(self):
        
        layout1=QHBoxLayout()
        okButton = QPushButton("SUBMIT")
        layout1.addStretch(1)       
        layout1.addWidget(okButton)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 25)
        cal.clicked[QDate].connect(self.showDate)

        self.lib2=QLabel(self)
        date2=g1.get_value('user')
        self.lib2.setText(date2)
        self.lib2.move(130,290)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        VBOX=QVBoxLayout()
        VBOX.addStretch(1)
        VBOX.addLayout(layout1)

        okButton.clicked[bool].connect(self.btnClicked)

        self.setTabText(2,"Apply")
        self.tab3.setLayout(VBOX)
    
        
    def btnClicked(self):
       reply= QMessageBox.information(self,'Information',"%s" %g1.get_value('user'))
        
    def showDate(self, date):
       self.lbl.setText(date.toString())
        
        
        

    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        

def open():
    app=QApplication(sys.argv)
    p=tabwidgetDemo()
    p.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    open()