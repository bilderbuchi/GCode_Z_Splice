# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct 19 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

from templatesGCodePanel import GCodePanel
from templatesTransitionPanel import TransitionPanel
import wx
import wx.xrc

###########################################################################
## Class mainFrameGUI
###########################################################################

class mainFrameGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"G-code Z Splicer", pos = wx.DefaultPosition, size = wx.Size( 900,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		mainFrame_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainPanel_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow = wx.ScrolledWindow( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB|wx.HSCROLL )
		self.m_scrolledWindow.SetScrollRate( 5, 5 )
		scrolledWindow_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FirstGCodePanel = GCodePanel( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		scrolledWindow_sizer.Add( self.FirstGCodePanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline_column = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		scrolledWindow_sizer.Add( self.m_staticline_column, 0, wx.EXPAND, 5 )
		
		self.FirstTransitionPanel = TransitionPanel( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		scrolledWindow_sizer.Add( self.FirstTransitionPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline_column1 = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		scrolledWindow_sizer.Add( self.m_staticline_column1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.SecondGCodePanel = GCodePanel( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		scrolledWindow_sizer.Add( self.SecondGCodePanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_scrolledWindow.SetSizer( scrolledWindow_sizer )
		self.m_scrolledWindow.Layout()
		scrolledWindow_sizer.Fit( self.m_scrolledWindow )
		mainPanel_sizer.Add( self.m_scrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		mainPanel_sizer.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.addFileButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Add File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.addFileButton.Enable( False )
		
		bSizer19.Add( self.addFileButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.removeFileButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Remove File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.removeFileButton.Enable( False )
		
		bSizer19.Add( self.removeFileButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer19.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		mainPanel_sizer.Add( bSizer19, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		
		self.mainPanel.SetSizer( mainPanel_sizer )
		self.mainPanel.Layout()
		mainPanel_sizer.Fit( self.mainPanel )
		mainFrame_sizer.Add( self.mainPanel, 1, wx.EXPAND, 5 )
		
		self.m_staticline6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		mainFrame_sizer.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.BottomPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText1 = wx.StaticText( self.BottomPanel, wx.ID_ANY, u"Result file:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer5.Add( self.m_staticText1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.resultFilePicker = wx.FilePickerCtrl( self.BottomPanel, wx.ID_ANY, u"out.gcode", u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OVERWRITE_PROMPT|wx.FLP_SAVE|wx.FLP_USE_TEXTCTRL )
		bSizer5.Add( self.resultFilePicker, 1, wx.ALL, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.BottomPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer5.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.generate_button = wx.Button( self.BottomPanel, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.generate_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.quit_button = wx.Button( self.BottomPanel, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.quit_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.BottomPanel.SetSizer( bSizer5 )
		self.BottomPanel.Layout()
		bSizer5.Fit( self.BottomPanel )
		mainFrame_sizer.Add( self.BottomPanel, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( mainFrame_sizer )
		self.Layout()
		
		# Connect Events
		self.addFileButton.Bind( wx.EVT_BUTTON, self.OnAddFile )
		self.removeFileButton.Bind( wx.EVT_BUTTON, self.OnRemoveFile )
		self.resultFilePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnResultFileSelected )
		self.generate_button.Bind( wx.EVT_BUTTON, self.OnGenerate )
		self.quit_button.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnAddFile( self, event ):
		event.Skip()
	
	def OnRemoveFile( self, event ):
		event.Skip()
	
	def OnResultFileSelected( self, event ):
		event.Skip()
	
	def OnGenerate( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	

