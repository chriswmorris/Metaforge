#!/usr/bin/env python3

import pyexifinfo as exif
import os, sys
import subprocess
import json
from os.path import basename
from definitions import ROOT_DIR
import shutil
from progress.bar import Bar

#This is the exiftool processor, it runs exiftool and puts the outputs in either 
#html, json or XML depending on which function is called. Exiftool needs to be installed for this
#to work.


#exiftool in JSON			
def exifJSON():
	print("Running exiftool to JSON")
	os.chdir(ROOT_DIR + "/media/")
	mediadir = os.listdir()
	mediafiles = len(mediadir)
	jsonbar = Bar('Processing', max=mediafiles)
	for i in range(mediafiles):
		for filename in os.listdir("."):
			exifoutputjson = exif.get_json(filename)
			#basejson = os.path.basename(filename)
			os.chdir(ROOT_DIR + "/exifdata/json")
			#Prints output to json file
			print(json.dumps(exifoutputjson, sort_keys=True, indent=0, separators=(',', ': ')), 
				file= open(filename + ".json","w"))
			#print(json.dumps(exifoutputjson, sort_keys=True, indent=0, separators=(',', ': ')), 
			#	file= open(os.path.splitext(basejson)[0]+".json","w"))

			jsonbar.next()
			os.chdir(ROOT_DIR + "/media")	
		break
	jsonbar.finish()

#exiftool in HTML
def exifHTML():
	print("Running exiftool to HTML")
	os.chdir(ROOT_DIR + "/media/")
	mediadir = os.listdir()
	mediafiles = len(mediadir)
	htmlbar = Bar('Processing', max=mediafiles)
	for i in range(mediafiles):
		for filename in os.listdir("."):
			#Prints output to HTML
			#basehtml = os.path.basename(filename)
			exifoutputhtml = exif.command_line(['exiftool', '-h', filename])
			os.chdir(ROOT_DIR + "/exifdata/html")
			#print(exifoutputhtml,file = open(os.path.splitext(basehtml)[0]+ ".html", "w"))
			print(exifoutputhtml,file = open(filename + ".html","w"))
			htmlbar.next()
			os.chdir(ROOT_DIR + "/media")
		break
	htmlbar.finish()

#exiftool hex dump to html
def exifHTMLDump():
	print("Running exiftool to HTML Dump")
	os.chdir(ROOT_DIR + "/media/")
	mediadir = os.listdir()
	mediafiles = len(mediadir)
	os.chdir(ROOT_DIR + "/media/")
	htmldumpbar = Bar('Processing', max=mediafiles)
	for i in range(mediafiles):
		for filename in os.listdir("."):
			#basehtmldump = os.path.basename(filename)
			exifoutputhtmldump = exif.command_line(['exiftool', '-htmlDump', filename])
			os.chdir(ROOT_DIR + "/exifdata/hex_html")	
			#htmldumpfile = open(os.path.splitext(basehtmldump)[0] + ".html", 'wb')
			htmldumpfile = open(filename + ".html", 'wb')
			htmldumpfile.write(exifoutputhtmldump)
			htmldumpfile.close()
			htmldumpbar.next()
			os.chdir(ROOT_DIR + "/media")
		break
	htmldumpbar.finish()	
