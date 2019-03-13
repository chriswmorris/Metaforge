#!/usr/bin/env python3


#=====================================================
#
# Metaforge
#
#=====================================================
#
#
#@version	1.3 (Pretty Reports Edition)
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
	print(Fore.WHITE + "An OSINT Metadata analyzing tool that filters through tags and creates reports")
	print("Version 1.3")
	print(Style.RESET_ALL)
	print(Fore.GREEN + "Authors: Chris Morris & Collin Mockbee")
	print("github.com/chriswmorris/Metaforge")
	print()
	print("=========================================================")
	print(Style.RESET_ALL)
	print(Fore.RED + "Remember to place the files you wish to analyze in this directory!")
	print(Style.BRIGHT +"-->  "+ ROOT_DIR + "/media  <--")
	print(Style.RESET_ALL)
	input("Press [ENTER] to continue")
	print()
	
def condchecking():
	print("=======================Step 1: Condition Checking =======================")
	print()
	print("Need to check to make sure that the program will run correctly...")
	print()
	input("Press [ENTER] to continue")

	try:
		stageset()
		checkdelete()
		print()
		print(Fore.GREEN + "Done. Everything looks correct")
		print(Style.RESET_ALL)

	except IOError as er:
		errno,strerror = er.args
		print(Fore.RED + "I/O error({0}): {1}".format(errno,strerror))
		print(Style.RESET_ALL)


	except:
		 print(Fore.RED + "Error:", sys.exc_info()[0])
		 print(Style.RESET_ALL)

def projectcreation():
	print("=========================Step 2: Project Creation=========================")
	#userproj is either defined by user or 6 random digits
	#This will create the file structure for the user's project

	randominput = ''.join(random.choice(string.ascii_lowercase 
		+ string.digits) for _ in range(6))

	print()
	print()
	print("Enter a name for your project. It will also be the name of the directory.")
	print("(If you would like a random name, leave it blank and press enter)")
	print()
	userproj = input("Project Name--> ") 
	print()

	if not userproj:
		userproj = "proj_" + randominput
	try:
		os.makedirs(ROOT_DIR +"/User_Projects/"+ userproj, exist_ok=True)
		projectdir = ROOT_DIR + "/User_Projects/" + userproj 
		print(Style.BRIGHT + "Your project is named: " + userproj)
		print(Style.RESET_ALL)
		print(Fore.GREEN + "Successfully created project folder!")
		print(Style.RESET_ALL)

	except:
		print(Fore.RED + "ERROR: ", sys.exc_info()[0])
		sys.exit("Quitting. You need a project folder")
		print(Style.RESET_ALL)

	return projectdir

def exifrun():
	print("=======================Step 3: Running the Exiftool=======================")
	print()
	#Runs exiftool on media/ directory to exifdata/ then runs
	#jsonsort to sort the json into designated folders

	print("This is going to run the exiftool on all of the media you defined here:")
	print(Fore.BLUE + ROOT_DIR + "/media")
	print(Style.RESET_ALL)
	print("It could take a while depending how many files you placed.")
	print()
	input("Press [ENTER] to continue")
	try:
		print()
		exifJSON()
	except:
		print(Fore.RED + "Exiftool to JSON failed")
		print("ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)
		pass

	try:
		exifHTML()
	except:
		print(Fore.RED +"Exiftool to HTML failed")
		print("ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)
		pass

	try:
		exifHTMLDump()
	except:
		print(Fore.RED +"Exiftool to Hexadecimal HTML failed")
		print("ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)
		pass
	print()


def filtering():
	print("=============================Step 4: Filtering=============================")
	print()
	#This will...
	#1) Sort the JSON into their respective folder
	#2) Filter out the "unimportant tags"

	jsondir = ROOT_DIR + "/exifdata/json/"
	jsonsubdirs = ['odp', 'png', 'mp3', 'dll', 'torrent', 'pptx', 'ods', 'odt,' 'zip', 'exe',
	 'xlsx', 'svg', 'pdf', 'mp4', 'html', 'docx', 'gif', 'wav', 'jpeg', 'mkv']

	print("Now going to sort the JSON into their respective (original) filetype folder")
	print()
	input("Press [ENTER] to continue")
	print()
	try:
		jsonsort()
		print(Fore.GREEN + "Sorting Successful in exifdata/json/")
		print(Style.RESET_ALL)

	except IOError as sorter:
		errno,strerror = sorter.args
		print(Fore.RED + "I/O error({0}): {1}".format(errno,strerror))
		print(Style.RESET_ALL)

	except:
		print(Fore.RED + "ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)

	print("Starting Filtering Process...")

	try:
		filterexec()
		print(Fore.GREEN + "Filtering Successful!")
		print(Style.RESET_ALL)

	except IOError as filterer:
		errno,strerror = filterer.args
		print(Fore.RED + "I/O error({0}): {1}".format(errno,strerror))
		print(Style.RESET_ALL)


	except:
		print(Fore.RED +"ERROR:", sys.exc_info()[0])
		print(Style.RESET_ALL)


def makereport(PROJ_DIR):
	print("=========================Step 5: Make Report=========================")
	print()
	print("This will make the HTML reports and set up the User Project directory")
	print()
	input("Press [ENTER] to continue")
	print()

	def copyfolders(src,dest):
		try:
			shutil.copytree(src,dest)
		except OSERROR as exc:
			if exc.errno == errno.ENOTDIR:
				shutil.copy(src,dest)
			else:
				raise

	#Make HTML Reports			
	try:
		statshtml()
	except:
		print(Fore.RED + "ERROR: could not run stat html report", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		filtershtml()
	except:
		print(Fore.RED + "ERROR: could not run filter html report", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		rawmetahtml()	
	except:
		print(Fore.RED + "ERROR: could not run rawmetahtml report", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		hexmetahtml()
	except:
		print(Fore.RED + "ERROR: could not run hexmetahtml report", sys.exc_info()[0])
		print(Style.RESET_ALL)



	#Moving folders to project dir
	try:
		print("Copying exifdata to project directory")
		copyfolders(ROOT_DIR + "/exifdata/" , PROJ_DIR + "/exifdata/")
	except:
		print(Fore.RED + "ERROR: could not copy exifdata to project dir: ", sys.exc_info()[0])
		print(Style.RESET_ALL)
	try:
		print("Placing Template_Data into project dir...")
		copyfolders(ROOT_DIR + "/Template_Data/", PROJ_DIR + "/Template_Data/")
	except:
		print(Fore.RED + "ERROR: Failed to copy Template_Data: ",sys.exc_info()[0])
		print(Style.RESET_ALL)


	#Placing reports from ROOT_DIR to PROJ_DIR
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



	#Removing exifdata/ since it exsists in PROJ_DIR 	
	try:
		shutil.rmtree(ROOT_DIR + "/exifdata/")
	except:
		print(Fore.RED + "ERROR: Failed to remove /exifdata/ dir: ",sys.exc_info()[0])
		print(Style.RESET_ALL)


	#Setting up exifdata dir for next run
	try:
		print("Setting up exifdata directory...")
		stageset()

	except:
		print(Fore.RED + "Could not run the stageset function-- ", sys.exc_info()[0])
		print(Style.RESET_ALL)

	print()
	print(Fore.GREEN + "FINISHED!")
	print(Style.RESET_ALL)
	print(Style.BRIGHT + "Project Folder is here:")
	print(Style.RESET_ALL)
	print(Back.WHITE+ Fore.BLACK+ PROJ_DIR)
	print(Style.RESET_ALL)
	print(Style.BRIGHT+ "To view the Report, click on the index.html file")
	print(Style.RESET_ALL)
	print("===============================================================")
	print()
	sys.exit(0)

def main():
	credits()
	condchecking()
	PROJ_DIR = projectcreation()
	exifrun()
	filtering()
	makereport(PROJ_DIR)


if __name__ == '__main__':
	main()
	
