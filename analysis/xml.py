#! /usr/bin/env python3
# coding: utf-8
import os


def lauch_analysis(data_file):
	directory = os.path.dirname(os.path.dirname(__file__))
	path_to_file = os.path.join(directory, 'data', data_file)

	with open(path_to_file,"r") as f:
		preview = f.readline()
		print("tu lis meme les xml maintenant!{}".format(preview))



if __name__ == '__main__':
	lauch_analysis("SyceronBrut.xml")