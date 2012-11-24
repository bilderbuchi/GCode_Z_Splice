# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct 19 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrameGUI
###########################################################################

class mainFrameGUI ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"G-code Z Splicer", pos = wx.DefaultPosition, size = wx.Size( 700,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		mainFrame_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.mainPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		mainPanel_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_scrolledWindow = wx.ScrolledWindow( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.ALWAYS_SHOW_SB|wx.HSCROLL )
		self.m_scrolledWindow.SetScrollRate( 5, 5 )
		scrolledWindow_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FirstGCodePanel = GCodePanelTemplate(self.m_scrolledWindow)
		self.FirstGCodePanel.title.SetLabel('G-code file 1')
		self.FirstGCodePanel.z_from.SetValue('0')
		scrolledWindow_sizer.Add( self.FirstGCodePanel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline_column = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		scrolledWindow_sizer.Add( self.m_staticline_column, 0, wx.EXPAND, 5 )
		
		self.FirstTransitionPanel = TransitionPanelTemplate(self.m_scrolledWindow)
		self.FirstTransitionPanel.title.SetLabel('Transition file 1')
		scrolledWindow_sizer.Add( self.FirstTransitionPanel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline_column1 = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		scrolledWindow_sizer.Add( self.m_staticline_column1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.SecondGCodePanel = GCodePanelTemplate(self.m_scrolledWindow)
		self.SecondGCodePanel.title.SetLabel('G-code file 2')
		scrolledWindow_sizer.Add( self.SecondGCodePanel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline_column11 = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		scrolledWindow_sizer.Add( self.m_staticline_column11, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_scrolledWindow.SetSizer( scrolledWindow_sizer )
		self.m_scrolledWindow.Layout()
		scrolledWindow_sizer.Fit( self.m_scrolledWindow )
		mainPanel_sizer.Add( self.m_scrolledWindow, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline9 = wx.StaticLine( self.mainPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		mainPanel_sizer.Add( self.m_staticline9, 0, wx.EXPAND |wx.ALL, 5 )
		
		bSizer19 = wx.BoxSizer( wx.VERTICAL )
		
		self.addFileButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Add File", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.addFileButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.removeFileButton = wx.Button( self.mainPanel, wx.ID_ANY, u"Remove File", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.removeFileButton.Enable( False )
		
		bSizer19.Add( self.removeFileButton, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer19.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.generate_button = wx.Button( self.mainPanel, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.generate_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.quit_button = wx.Button( self.mainPanel, wx.ID_ANY, u"Quit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer19.Add( self.quit_button, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		mainPanel_sizer.Add( bSizer19, 0, wx.ALIGN_RIGHT|wx.EXPAND, 5 )
		
		
		self.mainPanel.SetSizer( mainPanel_sizer )
		self.mainPanel.Layout()
		mainPanel_sizer.Fit( self.mainPanel )
		mainFrame_sizer.Add( self.mainPanel, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( mainFrame_sizer )
		self.Layout()
		
		# Connect Events
		self.generate_button.Bind( wx.EVT_BUTTON, self.OnGenerate )
		self.quit_button.Bind( wx.EVT_BUTTON, self.OnClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnGenerate( self, event ):
		event.Skip()
	
	def OnClose( self, event ):
		event.Skip()
	

###########################################################################
## Class GCodePanelTemplate
###########################################################################

class GCodePanelTemplate ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		GCodePanel_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"G-code file 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		GCodePanel_sizer.Add( self.title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		Zrange_sizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Z range from", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		Zrange_sizer.Add( self.m_staticText2, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.z_from = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.z_from.SetMaxLength( 0 ) 
		self.z_from.SetMinSize( wx.Size( 40,-1 ) )
		
		Zrange_sizer.Add( self.z_from, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"to", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		Zrange_sizer.Add( self.m_staticText3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.z_to = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.z_to.SetMaxLength( 0 ) 
		self.z_to.SetMinSize( wx.Size( 40,-1 ) )
		
		Zrange_sizer.Add( self.z_to, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		GCodePanel_sizer.Add( Zrange_sizer, 0, wx.EXPAND, 5 )
		
		self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		GCodePanel_sizer.Add( self.filePicker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.fileDisplay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileDisplay.SetMaxLength( 0 ) 
		GCodePanel_sizer.Add( self.fileDisplay, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( GCodePanel_sizer )
		self.Layout()
		GCodePanel_sizer.Fit( self )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class TransitionPanelTemplate
###########################################################################

class TransitionPanelTemplate ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		TransitionPanel_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Transition file 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		TransitionPanel_sizer.Add( self.title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.useTransition_checkbox = wx.CheckBox( self, wx.ID_ANY, u"Use transition file", wx.DefaultPosition, wx.DefaultSize, 0 )
		TransitionPanel_sizer.Add( self.useTransition_checkbox, 0, wx.ALL, 5 )
		
		self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		TransitionPanel_sizer.Add( self.filePicker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.fileDisplay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fileDisplay.SetMaxLength( 0 ) 
		TransitionPanel_sizer.Add( self.fileDisplay, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( TransitionPanel_sizer )
		self.Layout()
		TransitionPanel_sizer.Fit( self )
	
	def __del__( self ):
		pass
	

