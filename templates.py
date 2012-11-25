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
## Class GCodePanel
###########################################################################

class GCodePanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		GCodePanel_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"G-code file templ", wx.DefaultPosition, wx.DefaultSize, 0 )
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
		
		self.fileDisplay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.fileDisplay.SetMaxLength( 0 ) 
		GCodePanel_sizer.Add( self.fileDisplay, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( GCodePanel_sizer )
		self.Layout()
		GCodePanel_sizer.Fit( self )
		
		# Connect Events
		self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileSelected )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileSelected( self, event ):
		event.Skip()
	

###########################################################################
## Class TransitionPanel
###########################################################################

class TransitionPanel ( wx.Panel ):
	
	def __init__( self, parent ):
		wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.TAB_TRAVERSAL )
		
		TransitionPanel_sizer = wx.BoxSizer( wx.VERTICAL )
		
		self.title = wx.StaticText( self, wx.ID_ANY, u"Transition file template", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.title.Wrap( -1 )
		TransitionPanel_sizer.Add( self.title, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.useTransition_checkbox = wx.CheckBox( self, wx.ID_ANY, u"Use transition file", wx.DefaultPosition, wx.DefaultSize, 0 )
		TransitionPanel_sizer.Add( self.useTransition_checkbox, 0, wx.ALL, 5 )
		
		self.filePicker = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.filePicker.Enable( False )
		
		TransitionPanel_sizer.Add( self.filePicker, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.fileDisplay = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		self.fileDisplay.SetMaxLength( 0 ) 
		self.fileDisplay.Enable( False )
		
		TransitionPanel_sizer.Add( self.fileDisplay, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( TransitionPanel_sizer )
		self.Layout()
		TransitionPanel_sizer.Fit( self )
		
		# Connect Events
		self.useTransition_checkbox.Bind( wx.EVT_CHECKBOX, self.OnCheckBox )
		self.filePicker.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileSelected )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnCheckBox( self, event ):
		event.Skip()
	
	def OnFileSelected( self, event ):
		event.Skip()
	

