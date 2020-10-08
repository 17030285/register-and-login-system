import sqlite3
import BasicalInfo
import wx




class MyFrame(wx.Frame):
    def __init__(self, parent, id, title="INTERVIEW SYSTEM", pos=(100, 100), size=(400, 400)):

        frame = wx.Frame.__init__(self, parent, id, title="HR SYSTEM", pos=(500, 250), size=(400, 300))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel, label="Please enter your Username and password", pos=(80, 20))
        self.label_user = wx.StaticText(panel, label="Username:", pos=(35, 50))
        self.text_user = wx.TextCtrl(panel, pos=(100, 50), size=(235, 25), style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel, label="Password:", pos=(35, 90))
        self.text_password = wx.TextCtrl(panel, pos=(100, 90), size=(235, 25), style=wx.TE_PASSWORD)
        self.bt_confirm = wx.Button(panel, label='Login', pos=(105, 130))
        self.bt_resit = wx.Button(panel, label='resit', pos=(195, 130))
        self.bt_register = wx.Button(panel, label='Register', pos=(285, 130))

        self.bt_confirm.Bind(wx.EVT_BUTTON, self.OnclickLogin)
        self.bt_resit.Bind(wx.EVT_BUTTON, self.OnclickResit)
        self.bt_register.Bind(wx.EVT_BUTTON, self.OnclickRegister)

        self.Show()

    def OnclickLogin(self, event):
        conn = sqlite3.connect('F:\sqlitedb\studydb.db')
        cursor = conn.cursor()
        cursor.execute("SELECT user,password from user")
        message = ""
        username = self.text_user.GetValue()
        password = self.text_password.GetValue()
        tem = username
        if username == "" or password == "":
            message = 'Username or Password can not be empty'
        elif username != "" and password != "":
            for row in cursor:
                if username == row[0] and password == row[1]:
                    message="login successful"
                    break
                elif row[0] != username:
                    message = "Can not find this username"
                elif row[0] == username and row[1] != password:
                    message = 'The username and password do not match'
                    break

        wx.MessageBox(message)
        conn.close()

    def OnclickResit(self, event):
        self.text_password.SetValue("")
        self.text_user.SetValue("")

    def OnclickRegister(self, event):
        self.Close()
        BasicalInfo.open()


def reOpen():
    app = wx.App()
    t = MyFrame(parent=None, id=1)
    app.MainLoop()


def close(MyFrame):
    t = MyFrame.Close()


if __name__ == '__main__':
    app = wx.App()
    t = MyFrame(parent=None, id=1)
    app.MainLoop()
