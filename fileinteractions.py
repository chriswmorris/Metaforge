#!/usr/bin/env python3
import os, sys
from definitions import ROOT_DIR
import json
import shutil
import colorama
from colorama import Fore, Back, Style


def stageset():

	#This fuction checks to make sure that the exifdata directory is set correctly
	#It creates folders that need to be there
	
	exifdatadir = ROOT_DIR + "/exifdata/"
	filtereddir = ROOT_DIR + "/exifdata/filtered/"
	hexhtmldir = ROOT_DIR + "/exifdata/hex_html/"
	htmldir = ROOT_DIR + "/exifdata/html/"
	jsondir = ROOT_DIR + "/exifdata/json/"
	statsdir = ROOT_DIR + "/exifdata/stats/"
	geolocationdir = ROOT_DIR + "/exifdata/stats/geolocations"
	softwaredir = ROOT_DIR + "/exifdata/stats/software"
	devicesdir = ROOT_DIR + "/exifdata/stats/devices"
	authorsdir = ROOT_DIR + "/exifdata/stats/authors"
	customdir = ROOT_DIR + "/exifdata/stats/custom"

	filetypedir = ['odp', 'png', 'mp3', 'dll', 'torrent', 'pptx', 'ods', 'zip', 'exe',
	 'xlsx', 'svg', 'pdf', 'mp4', 'html', 'docx', 'gif', 'wav', 'jpeg', 'mkv', 'all']

	if not os.path.exists(exifdatadir):
		os.mkdir(exifdatadir)

	if not os.path.exists(filtereddir):
		os.mkdir(filtereddir)

	if not os.path.exists(hexhtmldir):
		os.mkdir(hexhtmldir)

	if not os.path.exists(htmldir):
		os.mkdir(htmldir)

	if not os.path.exists(jsondir):
		os.mkdir(jsondir)

	if not os.path.exists(statsdir):
		os.mkdir(statsdir)

	if not os.path.exists(geolocationdir):
		os.mkdir(geolocationdir)

	if not os.path.exists(softwaredir):
		os.mkdir(softwaredir)

	if not os.path.exists(devicesdir):
		os.mkdir(devicesdir)

	if not os.path.exists(authorsdir):
		os.mkdir(authorsdir)

	if not os.path.exists(customdir):
		os.mkdir(customdir)

	for filetype in filetypedir:
		if not os.path.exists(jsondir + filetype):
			os.mkdir(jsondir + filetype)


#This function will check to see if the exifdata/ directory and the exifdata/json/ are empty
#if it isn't it will prompt the user to delete them or not
def checkdelete():
	jsonpath = ROOT_DIR + "/exifdata/json/"
	filteredjsonpath = ROOT_DIR + "/exifdata/filtered/" 
	jsonsubdirs = ['odp', 'png', 'mp3', 'dll', 'torrent', 'pptx', 'ods', 'zip', 'exe',
	 'xlsx', 'svg', 'pdf', 'mp4', 'html', 'docx', 'gif', 'wav', 'jpeg', 'mkv', 'all']

	 #FILTER DIRECTORY
	if not os.listdir(filteredjsonpath):
		pass
	else:
		print(Fore.RED + filteredjsonpath + " has files inside")
		print(Style.RESET_ALL)
		print(Style.BRIGHT + "Would you like to delete these files?")
		print("It is recommended, just save the files elsewhere")
		print(Style.RESET_ALL)
		filteredjsonanswer = input("y/n: ")
		if filteredjsonanswer == "y":
			for filename in os.listdir(filteredjsonpath):
				os.remove(filteredjsonpath + filename)

		else:
			print("Not going to delete anything in: " + jsonpath)
			print(Fore.RED +"This could cause errors!")
			print(Style.RESET_ALL)
			pass 

	#JSON FOLDERS
	os.chdir(jsonpath)
	files = [filename for filename in os.listdir('.') if os.path.isfile(filename)]
	if not os.listdir(jsonpath):
		pass
	if files == []:
		pass

	else:
		print()
		print(Fore.RED + " exifdata/json has files inside")
		print(Style.RESET_ALL)
		print(Style.BRIGHT + "Would you like to delete these files?")
		print("It is recommended, just save the files elsewhere")
		print(Style.RESET_ALL)
		jsonanswer = input("y/n: ")
		if jsonanswer == "y":
			for filename in files:
				os.remove(filename)
		else:
			print("Not going to delete anything in: " + jsonpath)
			print(Fore.RED +"This could cause errors!")
			print(Style.RESET_ALL)
			pass 

	#DIRECTORIES IN EXIFDATA/JSON/
	os.chdir(jsonpath)
	for subdir in jsonsubdirs:	
		if not os.listdir(subdir):
			pass	
		else:
			print()
			print(Fore.RED + "exifdata/json/" + subdir + " has files inside")
			filesinsubdir = os.listdir(subdir)
			print(Style.RESET_ALL)
			print(Style.BRIGHT + "Would you like to delete these files?")
			print("It is recommended, just save the files elsewhere")
			print(Style.RESET_ALL)
			subdirsanswer = input("y/n: ")
			if subdirsanswer == "y":
				for f in filesinsubdir:
					fstring = ''.join(f)
					os.remove(jsonpath +"/"+ subdir +"/"+ fstring)

			else:
				print("Not going to delete anything in: " + subdir)
				print(Fore.RED +"This could cause errors!")
				print(Style.RESET_ALL)
				pass


#This function sorts the json files into their respective folder based on file extension
def jsonsort():
	os.chdir(ROOT_DIR + "/exifdata/json/")
	jfiles = [filename for filename in os.listdir(".") if os.path.isfile(filename)]
	for filename in jfiles:
		os.chdir(ROOT_DIR + "/exifdata/json/")
		shutil.copy(filename, ROOT_DIR + "/exifdata/json/all")

		try:
			with open(filename) as jsonfile:
				pjsonfile = json.load(jsonfile)
				for p in pjsonfile:
					if p['File:FileTypeExtension'] == "jpg":
						dest = ROOT_DIR + "/exifdata/json/jpeg"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "png":
						dest = ROOT_DIR + "/exifdata/json/png"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "gif":
						dest = ROOT_DIR + "/exifdata/json/gif"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "dll":
						dest = ROOT_DIR + "/exifdata/json/dll"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "docx":
						dest = ROOT_DIR + "/exifdata/json/docx"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "exe":
						dest = ROOT_DIR + "/exifdata/json/exe"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "html":
						dest = ROOT_DIR + "/exifdata/json/html"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "mkv":
						dest = ROOT_DIR + "/exifdata/json/mkv"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "mp3":
						dest = ROOT_DIR + "/exifdata/json/mp3"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "mp4":
						dest = ROOT_DIR + "/exifdata/json/mp4"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "odp":
						dest = ROOT_DIR + "/exifdata/json/odp"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "ods":
						dest = ROOT_DIR + "/exifdata/json/ods"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "pdf":
						dest = ROOT_DIR + "/exifdata/json/pdf"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "pptx":
						dest = ROOT_DIR + "/exifdata/json/pptx"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "svg":
						dest = ROOT_DIR + "/exifdata/json/svg"
						shutil.move(filename, dest)
						pass
	
					elif p['File:FileTypeExtension'] == "torrent":
						dest = ROOT_DIR + "/exifdata/json/torrent"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "wav":
						dest = ROOT_DIR + "/exifdata/json/wav"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "xlsx":
						dest = ROOT_DIR + "/exifdata/json/xlsx"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "zip":
						dest = ROOT_DIR + "/exifdata/json/zip"
						shutil.move(filename, dest)
						pass

					# Legacy MS Office Filetypes go into their newer-type's folder

					elif p['File:FileTypeExtension'] == "doc":
						dest = ROOT_DIR + "exifdata/json/docx"
						shutil.move(filename, dest)
						pass

					elif p['File:FileTypeExtension'] == "xls":
						dest = ROOT_DIR + "exifdata/json/xlsx"
						shutil.move(filename, dest)
						pass		

					elif p['File:FileTypeExtension'] == "ppt":
						dest = ROOT_DIR + "exifdata/json/pptx"
						shutil.move(filename, dest)
						pass

		except:
			print("Filetype is not supported:" + filename)

