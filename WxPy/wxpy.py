from ahk import AHK
from ahk.window import Window
ahk = AHK()
win = ahk.win_get(title='Accessible Google Colaboratory')  # by title
import wx
import threading
import win32api
import win32con
import win32gui
import os
import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()


hotkeys = {}
hotkeys[wx.WXK_F1] = lambda: ao_output.output("Save file.", True)
hotkeys[wx.WXK_F2] = lambda: ao_output.output("Load file.", True)

hk_actions = {}
hk_actions[wx.WXK_F1] = lambda: win.send("{F1}")
hk_actions[wx.WXK_F1] = lambda: win.send("{F2}")

###############################################################################
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (700, 600))
        self.myGUI()
        #self.setTransparent(4)

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
ao_output.output("Welcome to Accessible Google Colaboratory!", True)
app.MainLoop()