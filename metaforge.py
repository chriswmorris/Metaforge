#!/usr/bin/env python3


#=====================================================
#
# Metaforge
#
#=====================================================
#
#
#@version	1.0
#@link		https://github.com/chriswmorris/Metaforge
#@authors	Chris Morris & Collin Mockbee

import os, sys
import errno
import subprocess
import string
import random
import shutil
import colorama
from colorama import Fore, Back, Style
from definitions import ROOT_DIR
from fileinteractions import stageset, checkdelete, jsonsort
from exiftool import exifJSON, exifHTML, exifHTMLDump
from filter import filterexec
from markups import filtershtml, rawmetahtml, hexmetahtml, statshtml 
from shutil import copyfile

def credits():
	print("")
	print("")
	print("███╗   ███╗███████╗████████╗ █████╗ ███████╗ ██████╗ ██████╗  ██████╗ ███████╗")
	print("████╗ ████║██╔════╝╚══██╔══╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝")
	print("██╔████╔██║█████╗     ██║   ███████║█████╗  ██║   ██║██████╔╝██║  ███╗█████╗  ")
	print("██║╚██╔╝██║██╔══╝     ██║   ██╔══██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝ ")
	print("██║ ╚═╝ ██║███████╗   ██║   ██║  ██║██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗")
	print("╚═╝     ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝")
	print("")
	print("")
	print(Style.BRIGHT+ Fore.BLUE + "Metaforge")
	print(Fore.WHITE + "A metadata analyzer that creates dynamic reports with a unique filter")
	print("Version 1.0")
	print(Style.RESET_ALL)
	print()
	print(Fore.GREEN + "Authors: Chris Morris & Collin Mockbee")
	print("github.com/chriswmorris/Metaforge")
	print()
	print("=========================================================")
	print(Style.RESET_ALL)
	print(Fore.RED + "Remember to place the files you wish to analyze in ")
	print("the /media directory!")
	print(Style.RESET_ALL)
	input("Press [ENTER] to continue")
	print()
	
def condchecking():
	print("=======================Step 1: Condition Checking =======================")
	print()
	print("Need to check to make sure that the program will run correctly...")
	print()
	print(Style.BRIGHT +"NOTE:") 
	print("1) There cannot be any json files in the exifdata/json/ directory or subdirectories")
	print("2) There cannot be any files in the exifdata/filtered directory")
	print(Style.RESET_ALL)
	input("Press [ENTER] to continue")

	try:
		stageset()
		checkdelete()
		print()
		print(Fore.GREEN + "Done. Everything looks correct")
		print(Style.RESET_ALL)

	except IOError as er:
		errno,strerror = er.args
		print("I/O error({0}): {1}".format(errno,strerror))

	except:
		 print("Error:", sys.exc_info()[0])

def projectcreation():
	print("=======================Step 2: Project Creation=======================")
	#userproj is either defined by user or 6 random digits
	#For now the user's report will have to be in ROOT_DIR + User_Projects + userproj, 
	#not in their personal dirs like ~/, for now
	#This will create the file structure for the user's project

	print()

	randominput = ''.join(random.choice(string.ascii_lowercase 
		+ string.digits) for _ in range(6))

	
	print()
	print("Enter a name for your project. It will also be the name of the directory.")
	userproj = input("(Press enter for a random name): ") 
	print()

	if not userproj:
		userproj = "proj_" + randominput
	try:
		os.makedirs(ROOT_DIR +"/User_Projects/"+ userproj, exist_ok=True)
		projectdir = ROOT_DIR + "/User_Projects/" + userproj 
		print(Style.BRIGHT + "Your project is in this directory: " + projectdir)
		print(Style.RESET_ALL)

	except:
		print("ERROR: ", sys.exc_info()[0])
		sys.exit("Quitting. You need a project folder")

		
	print()
	print(Fore.GREEN + "Successfully created project folder!")
	print(Style.RESET_ALL)
	print()
	return projectdir

def exifrun():
	print("=======================Step 3: Running the Exiftool=======================")
	print()
	#Runs exiftool on media/ directory to exifdata/ then runs
	#jsonsort to sort the json into designated folders

	print("This is going to run the exiftool on all of the media you defined. It could take a while...")
	input("Press [ENTER] to continue")
	try:
		print()
		exifJSON()
	except:
		print("Exiftool to JSON failed")
		print("ERROR:", sys.exc_info()[0])
		pass

	try:
		exifHTML()
	except:
		print("Exiftool to HTML failed")
		print("ERROR:", sys.exc_info()[0])
		pass

	try:
		exifHTMLDump()
	except:
		print("Exiftool to Hexadecimal HTML failed")
		print("ERROR:", sys.exc_info()[0])
		pass
	print()


def filtering():
	print("=======================Step 4: Filtering=======================")
	print()
	#This will...
	#1) Sort the JSON into their respective folder
	#2) Filter out the "unimportant tags"

	jsondir = ROOT_DIR + "/exifdata/json/"
	jsonsubdirs = ['odp', 'png', 'mp3', 'dll', 'torrent', 'pptx', 'ods', 'zip', 'exe',
	 'xlsx', 'svg', 'pdf', 'mp4', 'html', 'docx', 'gif', 'wav', 'jpeg', 'mkv']

	print("Now going to sort the JSON into their respective (original) filetype folder")
	try:
		jsonsort()
		print(Fore.GREEN + "Sorting Successful in exifdata/json/")
		print(Style.RESET_ALL)

	except IOError as sorter:
		errno,strerror = sorter.args
		print("I/O error({0}): {1}".format(errno,strerror))

	except:
		print("ERROR:", sys.exc_info()[0])

	print("Starting Filtering Process")

	try:
		filterexec()
		print(Fore.GREEN + "Filtering Successful!")
		print(Style.RESET_ALL)

	except IOError as filterer:
		errno,strerror = filterer.args
		print("I/O error({0}): {1}".format(errno,strerror))

	except:
		print("ERROR:", sys.exc_info()[0])


def makereport(PROJ_DIR):
	print("=======================Step 5: Make Report=======================")
	print()
	#This will...
	#1) Move exifdata to Project folder 
	#2) Create the three report pages in html
	#	i.  Index, filtered meta = index.html  | indexfilterHTML()
	#	ii. Raw Metadata = rawmeta.html  | rawmetaHTML()        
	#	iii. Hexadecimal view of metadata = rawmeta.html   |   hexmetaHTML()
	#3) Place the html into the project folder

	def copyfolders(src,dest):
		try:
			shutil.copytree(src,dest)
		except OSERROR as exc:
			if exc.errno == errno.ENOTDIR:
				shutil.copy(src,dest)
			else:
				raise


	try:
		#This didn't work in Test 1 (see Bug 2)
		statshtml()
	except:
		print("ERROR: could not run stat html report", sys.exc_info()[0])
	try:
		filtershtml()
	except:
		print("ERROR: could not run filter html report", sys.exc_info()[0])
	try:
		rawmetahtml()	
	except:
		print("ERROR: could not run rawmetahtml report", sys.exc_info()[0])
	try:
		hexmetahtml()
	except:
		print("ERROR: could not run hexmetahtml report", sys.exc_info()[0])

	try:
		print("Copying exifdata to project directory")
		copyfolders(ROOT_DIR + "/exifdata/" , PROJ_DIR + "/exifdata/")

	except:
		print("ERROR: could not run stat html report", sys.exc_info()[0])




# Improve error handling here
	
	
	try:
		print("Placing template_data into project dir...")
		copyfolders(ROOT_DIR + "/template_data/", PROJ_DIR + "/template_data/")
		
	except:
		print(Fore.RED + "ERROR: Failed to copy template_data",sys.exc_info()[0])
		print(Style.RESET_ALL)



	print("Placing reports into project dir...")

	try:
		copyfile(ROOT_DIR + "/" + "index.html", PROJ_DIR + "/index.html")
		os.remove(ROOT_DIR + "/" + "index.html")

	except:
		print(Fore.RED + "ERROR: Failed to copy index.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)
			
	try:
		copyfile(ROOT_DIR + "/" + "filters.html", PROJ_DIR + "/filters.html")
		os.remove(ROOT_DIR + "/" + "filters.html")
		
	except:
		print(Fore.RED + "ERROR: Failed to copy filters.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)
	

	try:
		copyfile(ROOT_DIR + "/" + "rawmeta.html", PROJ_DIR + "/rawmeta.html")
		os.remove(ROOT_DIR + "/" + "rawmeta.html")

	except:
		print(Fore.RED + "ERROR: Failed to copy rawmeta.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)


	try:
		copyfile(ROOT_DIR + "/" + "hexdump.html", PROJ_DIR + "/hexdump.html")
		os.remove(ROOT_DIR + "/" + "hexdump.html")
	except:
		print(Fore.RED + "ERROR: Failed to copy rawmeta.html-- ",sys.exc_info()[0])
		print(Style.RESET_ALL)
	
	
	try:
		shutil.rmtree(ROOT_DIR + "/exifdata/")
	except:
		print(Fore.RED + "ERROR: Failed to remove /exifdata/ dir",sys.exc_info()[0])
		print(Style.RESET_ALL)


	try:
		print("Setting up exifdata directory...")
		stageset()

	except:
		print(Fore.RED + "Could not run the stageset function-- ", sys.exc_info()[0])
		print(Style.RESET_ALL)


	print("===============================================================")
	print()
	print(Style.BRIGHT + "Project Folder is here:")
	print(Style.RESET_ALL)
	print(Back.WHITE+ Fore.BLACK+ PROJ_DIR)
	print(Style.RESET_ALL)
	print(Style.BRIGHT+ "To view the Report, click on the index.html file")
	print(Style.RESET_ALL)
	print("===============================================================")
	print()

def main():
	credits()
	condchecking()
	PROJ_DIR = projectcreation()
	exifrun()
	filtering()
	makereport(PROJ_DIR)


if __name__ == '__main__':
	main()
	
