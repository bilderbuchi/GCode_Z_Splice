# Module with utility functions for the gcode_z_splice

import logging

logger = logging.getLogger(__name__)

def split_at_z(gcode_string,zsplit):
	"""Read string containing gcode, return two sections split at zsplit.

	Takes care of gcode preamble by starting checks only after ';LAYER:0' comment
	First section for contents where Z < zsplit, second section for all layers where Z>=zsplit.

	If used to get a middle section between two z values, first hack off the second section at the higher z,
	then hack off the first section at the lower z.

	TODO: Fix that layer name comment will be split away from its gcode section.
	"""

	line_list=gcode_string.splitlines(True)
	firstsection=''
	secondsection=''
	zvalue=None
	reached_zsplit=False
	reached_layer0=False

	for line in line_list:
		logger.debug('line: ' + line[0:-1])
		if ';LAYER:0' in line:
			reached_layer0=True

		if (reached_layer0 is True) and ('Z' in line.split(';')[0]): # only check non-comment part, after layer 0.
			words=line.split(';')[0] # get rid of semicolon comments
			words=words.split() #split on whitespace
			for w in words:
				if w[0] is 'Z':
					zvalue=float(w[1:])

			if zvalue is not None:
				logger.debug('found z value ' + str(zvalue))
			if zvalue>=zsplit:
				reached_zsplit=True

		if reached_zsplit is False:
			firstsection+=line
		else:
			secondsection+=line

	if reached_layer0 is not True:
		logger.warning('Did not reach Layer 0. Is this a valid gcode file?')
	if reached_zsplit is not True:
		logger.warning('Did not reach z split value ' + str(zsplit) + '!')

	return firstsection, secondsection

# *****************************************************************************
def splice_files(result_filepath, list_of_gcode_filepaths, list_of_zvalues, list_of_transition_filepaths = []):
	"""Splice a list of files into a result file according to z split values.

	Take a list of gcode file paths, zvalues, and optional transition file paths, 
	splice them together and save into a result file."""

	logger.info('Starting to splice')

	# Check validity of supplied params
	if len(list_of_gcode_filepaths)-1 is not len(list_of_zvalues):
		logger.error('Number of gcode files (' + str(len(list_of_gcode_filepaths)) + 
					  ') is not correct for number of Z values (' + str(len(list_of_zvalues)) + ')')
		return 1

	nr_transition_files=len(list_of_transition_filepaths)
	if nr_transition_files is 0:
		logger.info('No transition files given')
	elif nr_transition_files is 1:
		logger.info('Single transition file given')
	elif nr_transition_files is (len(list_of_gcode_filepaths)-1):
		logger.info(str(nr_transition_files) + ' transition files given')
	else:
		logger.error('Invalid number of transition files given')
		return 1

	list_of_zvalues.sort()

	# Initialization
	gcode_files = []
	gcode_contents = []
	transition_files = []
	transition_contents = []

	for g in list_of_gcode_filepaths:
		# TODO: error checking!
		gcode_files.append(open(g,'r'))
		gcode_contents.append(gcode_files[-1].read())

	for t in list_of_transition_filepaths:
		# TODO: error checking!
		transition_files.append(open(t,'r'))
		transition_contents.append(transition_files[-1].read())	

	result_file = open(result_filepath,'w')

	logger.debug('Length of gcode file list' + str(len(gcode_contents)))
	logger.debug('Number of z split values' + str(len(list_of_zvalues)))
	logger.debug('Length of transition file list' + str(len(transition_contents)))

	# Go through the gcode strings, splice them out, and write them into the result file
	for index, item in enumerate(gcode_contents):
		# First file
		if index == 0:
			result_file.write(split_at_z(item,list_of_zvalues[index])[0]) #write first part of first file
			logger.info('Finished writing first file')
			if nr_transition_files is not 0:
				result_file.write(transition_contents[0])
				logger.info('Finished writing transition file 1')
			continue
		# Last file
		elif index == len(gcode_contents)-1:
			result_file.write(split_at_z(item,list_of_zvalues[-1])[1])
			logger.info('Finished writing last file')
			continue
		# Middle files
		else:
			dummy=split_at_z(item,list_of_zvalues[index])[0] # discard file contents above zval[index]
			dummy=split_at_z(dummy,list_of_zvalues[index-1])[1] # discard file contents below zval[index-1]
			result_file.write(dummy)
			logger.info('Finished writing file ' + str(index+1))
			if nr_transition_files is not 0:
				result_file.write(transition_contents[min(index,nr_transition_files-1)]) # select appropriate transition file if only one is given
				logger.info('Finished writing transition file ' + str(min(index,nr_transition_files-1)+1))

	# Cleanup
	for g in gcode_files:
		g.close()
	for t in transition_files:
		t.close()
	result_file.close()
	logger.info('Finished splicing')
	return 0

# *****************************************************************************