import splicer_GUI_FB
from templatesGCodePanel import GCodePanel
from templatesTransitionPanel import TransitionPanel
import wx
import wx.xrc

import logging
import splicer

logger = logging.getLogger(__name__)

# Logic implementation file for the GUI
class MyFrame( splicer_GUI_FB.mainFrameGUI ):
	def __init__( self, parent ):

		#GCode Splicer init code


		splicer_GUI_FB.mainFrameGUI.__init__( self, parent )
		self.FirstGCodePanel.title.SetLabel('G-code file 1')
		self.FirstGCodePanel.z_from.SetValue('0')
		self.FirstGCodePanel.z_from.Enable(False)
		self.FirstTransitionPanel.title.SetLabel('Transition file 1')
		self.SecondGCodePanel.title.SetLabel('G-code file 2')
		self.SecondGCodePanel.z_from.Enable(False)		
		self.SecondGCodePanel.z_to.Enable(False)

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
		logger.info('Generating files')

		output=self.resultFilePicker.GetPath()
		logger.info('Output file: ' + output)
		g_files=[]
		z_values=[]
		t_files=[]

		for c in self.m_scrolledWindow.GetSizer().GetChildren():
			pass

			# TODO: implement scan over panels
			# TODO: make sure this is independent of order
			widget = c.GetWindow()
			if type(widget) is GCodePanel:
				logger.info('Found GCode panel ' + widget.title.GetLabel())

				path=widget.filePicker.GetPath()
				if path:
					logger.debug('path: ' + path + '.')
					g_files.append(path)

				zval=widget.z_to.GetValue()
				if path and zval:
					logger.info('Found Z value')
					logger.debug(zval)
					z_values.append(float(zval))

			elif type(widget) is TransitionPanel:
				logger.info('Found transition panel ' + widget.title.GetLabel())
				path=widget.filePicker.GetPath()
				if path and widget.useTransition_checkbox.IsChecked():
					logger.debug('path: ' + path +'.')
					t_files.append(path)	

		logger.info(g_files)
		logger.info(z_values)
		logger.info(t_files)


		if splicer.splice_files(output, g_files, z_values, t_files) is not 0:
			logger.error('An error occurred during splicing!')
		logger.info('Finished splicing!')

	
	def OnClose( self, event ):
		logger.info('Closing GUI')
		self.Close()

	def OnResultFileSelected( self, event ):
		# TODO: Implement OnResultFileSelected
		pass	
