import splicer_GUI_FB
import wx
import wx.xrc

# Logic implementation file for the GUI
class MyFrame( splicer_GUI_FB.mainFrameGUI ):
	def __init__( self, parent ):
		splicer_GUI_FB.mainFrameGUI.__init__( self, parent )

		# self.GCodePanel2 = wx.Panel( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# self.title = wx.StaticText( self.GCodePanel2, wx.ID_ANY, u"G-code file 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.m_scrolledWindow.GetSizer().Add( self.GCodePanel2, 0, wx.ALL|wx.EXPAND, 5 )

		# # Construct GUI manually and dynamically from self-defined classes
		# self.panel1 = GCodePanelTemplate(self.m_scrolledWindow)
		# self.panel1.title.SetLabel('templated Gcodefile 2')
		# self.m_scrolledWindow.GetSizer().Add( self.panel1, 0, wx.ALL|wx.EXPAND, 5 )

		# self.m_staticline_column = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		# self.m_scrolledWindow.GetSizer().Add( self.m_staticline_column, 0, wx.EXPAND, 5 )

		# self.panel2 = TransitionPanelTemplate(self.m_scrolledWindow)
		# self.panel2.title.SetLabel('templated Transitionfile 2')
		# self.m_scrolledWindow.GetSizer().Add( self.panel2, 0, wx.ALL|wx.EXPAND, 5 )

		print('bla')

	def OnGenerate( self, event ):
		print('Dummytext: Generating files')
	
	def OnClose( self, event ):
		self.Close()

# Implementing GCodePanelTemplate
class GCodePanelTemplate( splicer_GUI_FB.GCodePanelTemplate ):
	def __init__( self, parent ):
		splicer_GUI_FB.GCodePanelTemplate.__init__( self, parent )

		# Implementing TransitionPanelTemplate
class TransitionPanelTemplate( splicer_GUI_FB.TransitionPanelTemplate ):
	def __init__( self, parent ):
		splicer_GUI_FB.TransitionPanelTemplate.__init__( self, parent )