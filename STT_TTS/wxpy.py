import wx
import os
import os
from gtts import gTTS
import pyttsx3
import accessible_output2.outputs.auto
ao_output = accessible_output2.outputs.auto.Auto()
import sys
from text_to_speech import SpeechToText

###############################################################################
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size = (700, 600))
        self.myGUI()
        panel = wx.Panel(self)

        self.btn = wx.Button(panel,-1,"Enter voice command: ", pos =(200, 250), size = (300,40))
        self.btn.Bind(wx.EVT_BUTTON, self.OnClicked)


    def myGUI(self):
        menu_bar = wx.MenuBar()
        file_button = wx.Menu()
        
        #save_item = file_button.Append(wx.ID_EXIT, 'Save File','Saving ...')
        #load_item = file_button.Append(wx.ID_EXIT, 'Load File','Loading ...')
        exit_item = file_button.Append(wx.ID_EXIT, 'Exit','Exiting ...')

        menu_bar.Append(file_button, 'File')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.Quit, exit_item)

    def Quit(self, e):
        self.Close()

    def OnClicked(self, event): 
        btn = event.GetEventObject().GetLabel() 
        print(("Speech to Text button pressed successfully."),btn)
        SpeechToText()

    def OnToggle(self,event): 
      state = event.GetEventObject().GetValue()

class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Accessible Google Colaboratory")
        self.frame.Show()

        return True

app = MyApp()
app.MainLoop()
