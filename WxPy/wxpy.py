import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (700, 600))
        self.myGUI()

    def myGUI(self):
        menu_bar = wx.MenuBar()
        file_button = wx.Menu()
        
        save_item = file_button.Append(wx.ID_EXIT, 'Save File','Saving ...')
        load_item = file_button.Append(wx.ID_EXIT, 'Load File','Loading ...')
        exit_item = file_button.Append(wx.ID_EXIT, 'Exit','Exiting ...')
        #TODO: Figure out Load and Save (is this even necessary?)

        menu_bar.Append(file_button, 'File')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.Quit, exit_item)

    def Quit(self, e):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Accessible Google Colaboratory")
        self.frame.Show()

        return True

app = MyApp()
app.MainLoop()