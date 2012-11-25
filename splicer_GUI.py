import splicer_GUI_FB
from templatesGCodePanel import GCodePanel
from templatesTransitionPanel import TransitionPanel
import wx
import wx.xrc

# Logic implementation file for the GUI
class MyFrame( splicer_GUI_FB.mainFrameGUI ):
	def __init__( self, parent ):
		splicer_GUI_FB.mainFrameGUI.__init__( self, parent )
		self.FirstGCodePanel.title.SetLabel('G-code file 1')
		self.FirstGCodePanel.z_from.SetValue('0')
		self.FirstGCodePanel.z_from.Enable(False)
		self.FirstTransitionPanel.title.SetLabel('Transition file 1')
		self.SecondGCodePanel.title.SetLabel('G-code file 2')

		# self.GCodePanel2 = wx.Panel( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		# self.title = wx.StaticText( self.GCodePanel2, wx.ID_ANY, u"G-code file 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		# self.m_scrolledWindow.GetSizer().Add( self.GCodePanel2, 0, wx.ALL|wx.EXPAND, 5 )

		# # Construct GUI manually and dynamically from self-defined classes
		# self.panel1 = GCodePanelTemplate(self.m_scrolledWindow)
		# self.panel1.title.SetLabel('templated Gcodefile 2')
		# self.m_scrolledWindow.GetSizer().Add( self.panel1, 0, wx.ALL|wx.EXPAND, 5 )

		# self.m_staticline_column = wx.StaticLine( self.m_scrolledWindow, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL )
		# self.m_scrolledWindow.GetSizer().Add( self.m_staticline_column, 0, wx.EXPAND, 5 )

		# self.panel2 = TransitionPanel(self.m_scrolledWindow)
		# self.panel2.title.SetLabel('templated Transitionfile 2')
		# self.m_scrolledWindow.GetSizer().Add( self.panel2, 0, wx.ALL|wx.EXPAND, 5 )
	
	# Handlers for mainFrameGUI events.
	def OnAddFile( self, event ):
		# TODO: Implement OnAddFile
		pass
	
	def OnRemoveFile( self, event ):
		# TODO: Implement OnRemoveFile
		pass

	def OnGenerate( self, event ):
		print('Dummytext: Generating files')
	
	def OnClose( self, event ):
		print('Closing GUI')
		self.Close()
