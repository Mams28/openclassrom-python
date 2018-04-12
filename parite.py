#! /usr/bin/env python3
# coding: utf-8
import argparse
import analysis.csv as c_an
import analysis.xml as x_an
#import pdb

def parseargs():
	parser = argparse.ArgumentParser()

	parser.add_argument("-e", "--extension", help="""type file analysis: xml or csv ?""")

	parser.add_argument("-d","--datafile",help="""CSV file containing pieces of information about the members of parliament""")
    
	
	return parser.parse_args()


	
	

def main():
	args = parseargs()
	datafile = args.datafile
	#import pdb; pdb.set_trace()
	if args.extension == "xml":
		x_an.lauch_analysis(datafile)
	elif args.extension == "csv":
		c_an.lauch_analysis(datafile)
		
if __name__ == "__main__":
    main()