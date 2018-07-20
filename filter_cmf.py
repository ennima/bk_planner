# -*- coding: utf-8 -*-

import os,sys
import pathlib
from datetime import datetime
import math
import time
from time import time as time_i

#Big Data libs
import pandas as pd

#Home Made Libs
sys.path.insert(0, "lib")
from bytemath import *

def load_spaceSniffer_list(sniffer_txt):
	#bk_planner1_spaceSniffer.mxl is a preset for export correct txt file
	with open(sniffer_txt) as file:
		data = file.readlines()
	return data

def cmf_only(sniffer_stream):
	cmf_list = []
	# print(len(sniffer_stream))
	for line in sniffer_stream:
		# print(line)
		if(".cmf" in line):
			# print(line)
			cmf_list.append(line)
	return cmf_list

def load_clips(csv):
	df = pd.read_csv('test_clip_list.csv')
	return df
	
def get_list_clips(df):
	clips = df.clipname.tolist()
	return clips

def get_clip_metadata(clip_name, cmf_list):
	##****************************************************
	#  Get Size and Path from data in spaceSniffer list
	##****************************************************
	clip_metadata = {}
	for cmf in cmf_list:
		if(clip_name in cmf):
			# print(cmf)
			break_cmf_line = cmf.split(" [")
			full_mam_path = break_cmf_line[0]
			size_human = break_cmf_line[1].replace("]","").strip()
			size_number_part = float(size_human[:-2])
			size_unit_part = size_human.replace(str(size_number_part),"").strip()
			size_bytes = unit_to_bytes(size_number_part,size_unit_part)
			clip_metadata = {"name":clip_name,"path":full_mam_path,"size":size_bytes,"size_human":size_human}
			# print(clip_metadata)
			break
		else:
			clip_metadata = False

	return clip_metadata

	
def make_metadata_list(list_clips, cmfs):
	## **************************************
	#  Entrega 2 listas, una con la metadata(list)
	#  otra con los clips no encontrados(error)
	## **************************************
	metadata_list = []
	metadata_list_error = []
	metadata_lists = {"list":metadata_list,"error":metadata_list_error}
	for item in list_clips:
		clip = get_clip_metadata(item, cmfs)
		if(clip != False):
			metadata_list.append(clip)
		else:
			metadata_list_error.append(item)
	return metadata_lists


def portion(total, part):
	## ***********************************************
	#  Return portion that represent part from 100%
	## ***********************************************
	return (part * 100)/total

def run():

	## Load CSV of clips from ms excel
	list_clips = get_list_clips(load_clips("bk_planner1_sample_list.csv"))

	stream = load_spaceSniffer_list("bk_planner1_sample_list.txt")
	total_lines = len(stream)
	
	cmfs = cmf_only(stream)
	total_cmfs = len(cmfs)
	
	print(total_cmfs)

	metadata_list = make_metadata_list(list_clips, cmfs)
	total_metadata_clips = len(metadata_list["list"])
	print(total_metadata_clips)
	print(metadata_list)

	print("Represents: "+str(portion(total_cmfs,total_metadata_clips))+"% from "+str(total_cmfs)+" clips")

if __name__ == '__main__':
    run()