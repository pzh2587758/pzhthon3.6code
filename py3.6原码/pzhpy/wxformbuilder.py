
# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun  5 2014)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class MyPanel1
###########################################################################

class MyPanel1 (wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(
            500, 300), style=wx.TAB_TRAVERSAL)

    def __del__(self):
        pass


###########################################################################
# Class MyDialog1
###########################################################################

class MyDialog1 (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                           pos=wx.DefaultPosition, size=wx.DefaultSize, style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


###########################################################################
# Class MyFrame2
###########################################################################

class MyFrame2 (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            813, 513), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_button1 = wx.Button(
            self, wx.ID_ANY, u"增", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(
            self, wx.ID_ANY, u"删", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(
            self, wx.ID_ANY, u"查", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button4 = wx.Button(
            self, wx.ID_ANY, u"改", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_listCtrl1 = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_ICON)
        self.m_listCtrl1.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWFRAME))

        gSizer1.Add(self.m_listCtrl1, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(
            self, wx.ID_ANY, u"运行", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(
            self, wx.ID_ANY, u"停止", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(
            self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()
        self.m_menubar1 = wx.MenuBar(0)
        self.m_menu1 = wx.Menu()
        self.m_menu11 = wx.Menu()
        self.m_menu1.AppendSubMenu(self.m_menu11, u"打开")

        self.m_menu21 = wx.Menu()
        self.m_menu1.AppendSubMenu(self.m_menu21, u"新建")

        self.m_menu31 = wx.Menu()
        self.m_menu1.AppendSubMenu(self.m_menu31, u"另存")

        self.m_menuItem5 = wx.MenuItem(
            self.m_menu1, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu1.AppendItem(self.m_menuItem5)

        self.m_menubar1.Append(self.m_menu1, u"文件")

        self.m_menu2 = wx.Menu()
        self.m_menuItem1 = wx.MenuItem(
            self.m_menu2, wx.ID_ANY, u"哈哈", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.AppendItem(self.m_menuItem1)

        self.m_menuItem2 = wx.MenuItem(
            self.m_menu2, wx.ID_ANY, u"呵呵", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu2.AppendItem(self.m_menuItem2)

        self.m_menubar1.Append(self.m_menu2, u"工具")

        self.m_menu3 = wx.Menu()
        self.m_menuItem3 = wx.MenuItem(
            self.m_menu3, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.AppendItem(self.m_menuItem3)

        self.m_menuItem4 = wx.MenuItem(
            self.m_menu3, wx.ID_ANY, u"版本", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu3.AppendItem(self.m_menuItem4)

        self.m_menubar1.Append(self.m_menu3, u"帮助")

        self.SetMenuBar(self.m_menubar1)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass

app = wx.App()

frame = MyFrame2(None)

frame.Show()

app.MainLoop()
