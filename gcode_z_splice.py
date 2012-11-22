import logging
import splicer
import argparse
import sys


logger = logging.getLogger(__name__)

if len(sys.argv) > 1:
	#Arguments have been passed, start to parse them

	#*************************************
	# command line argument parser
	parser = argparse.ArgumentParser(description='Splice a number of G-code files at given Z positions, optionally inserting intermediary transition files')
	parser.add_argument('-f', '--files', nargs='+', required=True, help='At least two G-code files which should be spliced together.')
	parser.add_argument('-z', '--zvalues', nargs='+', required=True, type=float, help='Z-value(s) where files should be spliced. Must be one fewer than files.')
	parser.add_argument('-t', '--transitionfiles', default=[], nargs='+',help='Optional file(s) containing G-code inserted at splicing point. If one transition file is supplied, it is used for all transitions.')
	parser.add_argument('-o', '--output', default='out.gcode', help='Name of output G-code file. Defaults to out.gcode.')
	parser.add_argument('-v', '--verbose' , action='store_true', help='Switch on debug logging.')
	args=parser.parse_args() #pass '-xyzZ'.split() for debugging
	# Reasonable test option:
	# python ./gcode_z_splice.py -f gcode_files/wavecube_coarse.gcode gcode_files/wavecube_fine.gcode gcode_files/wavecube_fine2.gcode -z 9 12.5 -t gcode_files/transition.gcode

	#Verify option/argument validity
	if len(args.files) == 1:
		parser.error('supply at least two files to splice')
	if len(args.files) is not (len(args.zvalues)+1):
		parser.error('there must be one fewer zvalues than files')
	if len(args.transitionfiles) not in [0,1,(len(args.files)-1)]:
		parser.error('There may be either one transition file or one fewer than files')

	# Initialisation
	if args.verbose is True:
		logging.basicConfig(level=logging.DEBUG)
	else:
		logging.basicConfig(level=logging.INFO) # DEBUG/INFO/WARNING/ERROR/CRITICAL

	logger.debug(args)

	#Main function
	logger.info('Start splicing process.')
	if splicer.splice_files(args.output, args.files, args.zvalues, args.transitionfiles) is not 0:
		logger.error('An error occurred during splicing!')
	logger.info('Finished!')

	#Cleanup
	logging.shutdown()

else:
	# No arguments have been passed. Start in GUI mode
	logging.basicConfig(level=logging.INFO)
	logger.warning('GUI mode. No arguments have been passed. Shutting down.')
	logging.shutdown()