import wx #wx is a library which you need use Anaconda to do download it but i think it is a good GUI library
import sqlite3 #it is used to link with the sqlite3 database,which we have already builded
import loginPanel #state the login module



class userDetailCollection(wx.Frame):
    def __init__(self, parent, id):# this is the constructor function to build the register interface
        list1 = ["Male", "Female", "SECRET"]# create a list to transfor the gender to a list box
        frame = wx.Frame.__init__(self, parent, id, title="Set basical detail", pos=(500, 250), size=(1000,1000))#initialize the main form
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="Basical data for new employee", pos=(200, 20))
        self.text_username=wx.TextCtrl(panel,  pos=(500, 50),size=(235,25),style=wx.TE_LEFT)
        self.text_password = wx.TextCtrl(panel, pos=(500, 90), size=(235, 25),style=wx.TE_PASSWORD)
        self.label_username = wx.StaticText(panel, label="Username:", pos=(420, 50))
        self.label_password = wx.StaticText(panel, label="Password:", pos=(420, 90))
        self.label_name = wx.StaticText(panel, label="Name:", pos=(50, 50))
        self.text_Name = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_gender = wx.StaticText(panel, label="Gender:", pos=(50, 90))
        self.check_gender = wx.ListBox(panel, -1, choices=list1, style=wx.LB_SINGLE, pos=(100, 90), size=(150, 50))
        self.label_age = wx.StaticText(panel, label="age:", pos=(50, 160))
        self.text_age = wx.TextCtrl(panel, pos=(100, 160), size=(235, 25), style=wx.TE_LEFT)
        self.label_department = wx.StaticText(panel, label="department:", pos=(30, 200))
        self.text_department = wx.TextCtrl(panel, pos=(100, 200), size=(235, 25), style=wx.TE_LEFT)
        self.label_address = wx.StaticText(panel, label="address:", pos=(40, 240))
        self.text_address = wx.TextCtrl(panel, pos=(100, 240), size=(235, 25), style=wx.TE_LEFT)
        self.label_dob = wx.StaticText(panel, label="DOB:", pos=(50, 280))
        self.text_dob = wx.TextCtrl(panel, pos=(100, 280), size=(235, 25), style=wx.TE_LEFT)
        self.bt_submit = wx.Button(panel, label='Submit', pos=(105, 320))
        self.bt_cancel = wx.Button(panel, label='Cancel', pos=(195, 320))
        self.bt_resit = wx.Button(panel, label='Resit', pos=(285, 320))
        self.bt_submit.Bind(wx.EVT_BUTTON, self.OnclickSubmit)
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.OnclickCancel)
        self.bt_resit.Bind(wx.EVT_BUTTON, self.OnclickResit)
        self.check_gender.Bind(wx.EVT_LISTBOX, self.OnclickSubmit, id=34)

    def OnclickCancel(self, event):
        self.Close()

    def OnclickResit(self, event):
        self.text_age.SetValue("")
        self.text_dob.SetValue("")
        self.text_Name.SetValue("")
        self.text_apartment.SetValue("")
        self.text_address.SetValue("")

    def OnclickSubmit(self, event):
        conn = sqlite3.connect('F:\sqlitedb\studydb.db')  # connect database(this database i created in localhost in future can build a server to manage the database)
        cursor = conn.cursor()  # Create a cursor, the cursor is a Class and have some function to contral the database
        username=self.text_username.GetValue()
        password=self.text_password.GetValue()
        name = self.text_Name.GetValue()
        gender = self.check_gender.GetStringSelection()
        age = int(self.text_age.GetValue())
        department = self.text_department.GetValue()
        address = self.text_address.GetValue()
        dob = self.text_dob.GetValue()
        if username == "" or password == "" or name=="" or gender=="" or age=="" or department=="" or address=="" or dob=="":
            message = "Can not process empty"
        else:
            try:
                cursor.execute("INSERT INTO userDetail(userNum,Name,Gender,Age,department,Address,DOB) VALUES('%s','%s','%s','%d','%s','%s',%s);" % (username, name, gender, age, department, address, dob))
                cursor.execute("INSERT INTO user(user,password) VALUES('%s','%s');" % (username, password))
            except:
                message = "error"
            else:
                conn.commit()
                cursor.close()
                conn.close()
                self.Close()
                message = "successful"
                loginPanel.reOpen()
            wx.MessageBox(message)


def open():
    app = wx.App()
    t = userDetailCollection(parent=None, id=34)
    t.Show()
    app.MainLoop()


if __name__ == '__main__':
    app = wx.App()
    t = userDetailCollection(parent=None, id=34)
    t.Show()
    app.MainLoop()