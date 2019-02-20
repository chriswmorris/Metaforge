 #!/usr/bin/env python3

import os, os.path, sys
import dominate
import shutil
import subprocess
from dominate.tags import *
from dominate.util import raw
from definitions import ROOT_DIR
from os import listdir
from os.path import isfile, join

def statshtml():
# This will display stats about the files
# Some stats to include will be...
# 1) Number of file types (graph too) 
# 2) Geolocations with map (maybe?)
# 3) Filtered vs. unfiltered meta
# 4) File Size Graph?
# 5) Software
# 6) Device/manufact. model
# 7) Top 5 largest files
# Then Generate the html report
	

	# ADD CUSTOM TAGS HERE:
	# The best way to look for tags is to run exiftool -j -G <filename> 
	# FORMAT: add "" and a comma to separate them. Example: "Composite:GPSPosition","EXIF:GPSAltitude"
	# 
	# Leave the PLACEHOLDER there if there's only one tag
	# Delete "DELETE_ME" when entering in another tag
	# Delete the PLACEHOLDER and DELETE_ME when you have more than 1 tag

	customtags = ("PLACEHOLDER", "DELETE_ME")

	#################################################################################

	# FILETYPE CHART
	# Stats about the number of files in each supported filetype
	# Supported filetypes: dll, docx, exe, gif, html, jpeg, mkv, mp3, mp4, odp, ods, pdf, png, pptx, svg, torrent, wav, xlsx, zip
	jsonexifdir = (ROOT_DIR + "/exifdata/json/")
	statsdir = (ROOT_DIR + "/exifdata/stats/")
	jsondirs = ("dll", "docx", "exe", "gif", "html", "jpeg", "mkv", "mp3", "mp4", "odp", "ods", "pdf",
	 "png", "pptx", "svg", "torrent", "wav", "xlsx", "zip")


	try: 
		filetypestxt= open(statsdir + "filetypes.txt","w+")
		os.chdir(jsonexifdir)
		for dirs in jsondirs:
			filetypestxt.write(dirs + ": " )
			os.chdir(jsonexifdir + dirs)
			listfiles = os.listdir(".")
			numberoffiles = str(len(listfiles))
			filetypestxt.write(numberoffiles + "\n")

		os.chdir(jsonexifdir)
		unkfiles = [f for f in listdir(".") if isfile(join(".", f))]
		filetypestxt.write("Unknown Files: " + str(len(unkfiles)) + "\n")
		os.chdir(ROOT_DIR + "/exifdata/html/")
		filetypestxt.write("Total Files: ")
		listtotal = os.listdir(".")
		numberoftotalfiles = str(len(listtotal))
		filetypestxt.write(numberoftotalfiles + "\n")
		filetypestxt.close()

	except:
		print("Error: Filetype chart generation failed: ", sys.exc_info() )

	#FILE SIZE CHART
	#Stats about the top 10 largest files
	mediadir = (ROOT_DIR + "/media")
	
	try:
		os.chdir(mediadir)
		subprocess.run("du -k * | sort -nr > filesizes.txt", shell=True, check=True)
		shutil.move(mediadir +"/" + "filesizes.txt", statsdir)

	except:
		print("Error: Filesize chart generation failed: ", sys.exc_info() )


	#GEOLOCATION CHARTS
	#Filters through media to find only files with geolocation data
	jsonalldir = (ROOT_DIR + "/exifdata/json/all/")
	geolocationsdir = (ROOT_DIR + "/exifdata/stats/geolocations/")
	geotags=("Composite:GPSPosition","EXIF:GPSAltitude", "EXIF:GPSLongitude", "EXIF:GPSLatitude")


	try: 
		os.chdir(jsonalldir)
		for gfile in os.listdir("."):
			with open(gfile) as ogfile:
				baseg = os.path.basename(gfile)
				with open(os.path.splitext(baseg)[0]+".txt", "w") as geolocationfile:	
					for ogline in ogfile:
						for tag in geotags:
							if tag in ogline:
								geolocationfile.write(ogline+ "\n")

		os.chdir(jsonalldir)						
		for geofile in os.listdir("."):
			if ".txt" in geofile:
				shutil.move(jsonalldir + geofile, geolocationsdir)

		os.chdir(geolocationsdir)		
		for geofile in os.listdir("."):
			if os.path.exists(geofile) and os.path.getsize(geofile) == 0:
				os.remove(geofile)

	except:
		print("Error: Geolocation chart generation failed: ", sys.exc_info() )



	# AUTHOR,ORG,COMPANY AND CREATORS CHART
	# Filters through media to find only files with above info 

	authortags=("XMP:Creator", "XML:Company","FlashPix:Author","FlashPix:Company","HTML:Author","XMP-dc:Creator","PDF:Creator",
		"PDF:Producer", "PDF:Author","EXE:LegalCopyright","EXE:CompanyName","Torrent:Creator")

	authordir=(ROOT_DIR + "/exifdata/stats/authors/")

	try:
		os.chdir(jsonalldir)
		for authorfile in os.listdir("."):
			with open(authorfile) as oauthorfile:
				baseauthor = os.path.basename(authorfile)
				with open(os.path.splitext(baseauthor)[0]+".txt", "w") as authoretcfile:
					for authorline in oauthorfile:
						for authortag in authortags:
							if authortag in authorline:
								authoretcfile.write(authorline+ "\n")

		os.chdir(jsonalldir)
		for authorfile in os.listdir("."):
			if ".txt" in authorfile:
				shutil.move(jsonalldir + authorfile, authordir)

		os.chdir(authordir)
		for authorfile in os.listdir("."):
			if os.path.exists(authorfile) and os.path.getsize(authorfile) == 0:
				os.remove(authorfile)


	except:
		print("Error: Author/Creator/etc chart generation failed: ", sys.exc_info() )



	#SOFTWARE CHARTS
	#Filters through media to find only files with Software data		

	softwaredir = (ROOT_DIR + "/exifdata/stats/software/")
	softwaretags = ("EXIF:Software","PNG:Software","FlashPix:Software","XML:Application", 
		"FlashPix:Software", "PDF:Producer",  "RIFF:Software")

	try:
		os.chdir(jsonalldir)
		for sfile in os.listdir("."):
			with open(sfile) as osfile:
				bases = os.path.basename(sfile)
				with open(os.path.splitext(bases)[0]+".txt", "w") as softwarefile:	
					for osline in osfile:
						for sotag in softwaretags:
							if sotag in osline:
								softwarefile.write(osline + "\n")

		os.chdir(jsonalldir)						
		for softfile in os.listdir("."):
			if ".txt" in softfile:
				shutil.move(jsonalldir + softfile, softwaredir)

		os.chdir(softwaredir)		
		for softfile in os.listdir("."):
			if os.path.exists(softfile) and os.path.getsize(softfile) == 0:
				os.remove(softfile)

	except:
		print("Error: Software chart generation failed: ", sys.exc_info() )

	#DEVICE/MODELS CHARTS
	#Filters through media to find only files with Device and Model data		

	devicedir = (ROOT_DIR + "/exifdata/stats/devices/")
	devicetags = ("ICC-header:DeviceAttributes", "ICC_Profile:DeviceModel", 
		"ICC_Profile:DeviceMfgDesc", "ICC_Profile:DeviceModelDesc", "ExifIFD:LensModel", "EXIF:Model")

	try:
		os.chdir(jsonalldir)
		for devfile in os.listdir("."):
			with open(devfile) as odevfile:
				based = os.path.basename(devfile)
				with open(os.path.splitext(based)[0]+".txt", "w") as devicefile:	
					for odevline in odevfile:
						for devtag in devicetags:
							if devtag in odevline:
								devicefile.write(odevline + "\n")

		os.chdir(jsonalldir)						
		for devfile in os.listdir("."):
			if ".txt" in devfile:
				shutil.move(jsonalldir + devfile, devicedir)

		os.chdir(devicedir)		
		for devfile in os.listdir("."):
			if os.path.exists(devfile) and os.path.getsize(devfile) == 0:
				os.remove(devfile)

	except:
		print("Error: Device/Model chart generation failed: ", sys.exc_info() )

	# CUSTOM CHART
	# CUSTOM TAGS WILL BE HERE
	customdir = (ROOT_DIR + "/exifdata/stats/custom/")

	try:
		os.chdir(jsonalldir)
		for customfile in os.listdir("."):
			with open(customfile) as ocustomfile:
				basecustom = os.path.basename(customfile)
				with open(os.path.splitext(basecustom)[0]+".txt", "w") as thecustomfile:	
					for customline in ocustomfile:
						for customtag in customtags:
							if customtag in customline:
								thecustomfile.write(customline + "\n")

		os.chdir(jsonalldir)						
		for customfile in os.listdir("."):
			if ".txt" in customfile:
				shutil.move(jsonalldir + customfile, customdir)

		os.chdir(customdir)		
		for customfile in os.listdir("."):
			if os.path.exists(customfile) and os.path.getsize(customfile) == 0:
				os.remove(customfile)

	except:
		print("Error: Custom chart generation failed: ", sys.exc_info() )


	# FILTERED DATA VS RAW EXIF
	# Count the number of lines in all filtered and all raw
	# Use jsonalldir for raw metadata

	try:

		filterdir = (ROOT_DIR + "/exifdata/filtered/")
		os.chdir(jsonalldir)
		subprocess.run("cat * > all_lines.txt", shell=True, check=True)
		shutil.move(jsonalldir + "all_lines.txt", statsdir)
		os.chdir(filterdir)
		subprocess.run("cat * > all_filter.txt", shell=True, check=True)
		shutil.move(filterdir + 'all_filter.txt', statsdir)
		allnum_lines = 0
		allfilter_lines = 0
		linestatstxt= open(statsdir + "linestats.txt","w+")
		os.chdir(statsdir)
		with open("all_lines.txt", "r") as alllinestxt:
			for al_line in alllinestxt:
				allnum_lines += 1
		linestatstxt.write("Number of lines before filtering metadata: " + str(allnum_lines) + "\n")
		with open("all_filter.txt", "r") as allfiltertxt:
			for fi_line in allfiltertxt:
				allfilter_lines +=1
		linestatstxt.write("Number of lines after filtering metadata: " + str(allfilter_lines))
		linestatstxt.close()
		os.remove(statsdir + 'all_filter.txt')
		os.remove(statsdir + 'all_lines.txt')

	except:
		print("Error: Filtered vs Raw chart generation failed: ", sys.exc_info() )



	# START STAT HTML REPORT GEN----------------------------------------------------------------
	# HTML REPORT GENERATION
	# THIS MAKES THE INDEX/STATS PAGE
	os.chdir(ROOT_DIR)
	doc = dominate.document(title='Metaforge')

	#Creates <head>
	with doc.head:
		link(rel='stylesheet', href="template_data/css/main.css")
		script(type='text/javascript', src="template_data/js/main.js")
		
	#Creates <body>
	with doc:
		h1("Metaforge")
		h3("Home/Statistics")
		with div(id='metaforge-credits'):
			p("Created Chris Morris and Collin Mockbee")
			p("https://github.com/chriswmorris/Metaforge")
		br()
		with div(id= 'wrapper'):
			with div(id='navbar').add(ul()):
				with div(id='nav-li'):
					a('Home/Stats', href='index.html' % ['index'])
					a('Filtered_Metadata', href='filters.html' % ['filters'])
					a('All_Metadata', href='rawmeta.html' % ['rawmeta'])
					a('Hexadecimal_View', href='hexdump.html' % ['hexdump'])

			with div(id='toprow'):
				with div(id='filetypechart'):
					h4("Number of Files in each Filetype")	
					with div(id='filetypechart-box'):
						filetype_stat = open(ROOT_DIR + "/exifdata/stats/filetypes.txt")
						filetyperead = filetype_stat.readlines()
						for fline in filetyperead:
							p(fline)
							br()
							br()

				with div(id='sizechart'):
					h4("Top 5 Largest Files")
					h5("File Size in Kilobytes")
					with div(id='size-box'):
						sizechart_stat = open(ROOT_DIR + "/exifdata/stats/filesizes.txt")
						asizechartread = sizechart_stat.readline()
						bsizechartread = sizechart_stat.readline()
						csizechartread = sizechart_stat.readline()
						dsizechartread = sizechart_stat.readline()
						esizechartread = sizechart_stat.readline()
						p(asizechartread)
						p(bsizechartread)
						p(csizechartread)
						p(dsizechartread)
						p(esizechartread)
						br()

				with div(id='comparechart'):
					h4("Raw Metadata vs Filtered Metadata")
					h5("Actual lines of metadata vs. Amount of filtered metadata")	
					with div(id='comparechart-box'):
						linestats_stat = open(ROOT_DIR + "/exifdata/stats/linestats.txt")
						linestatsread = linestats_stat.readlines()
						for lsline in linestatsread:
							p(lsline)
						br()
						br()

			br()			
			hr()		
			with div(id='secondrow'):
				with div(id='geolocationschart'):
					h4("Geolocations")
					with div(id='geolocation-box'):
						os.chdir(geolocationsdir)
						for geolocationfile in os.listdir("."):
							geofilename = os.path.splitext(geolocationfile)[0]
							gfile_read = open(geolocationfile, 'r')
							h4(geofilename)
							p(gfile_read.readline())
							for g_line in gfile_read:
								p(gfile_read.readlines(1))
							br()
					os.chdir(ROOT_DIR)	

				with div(id='authorchart'):
					h4("Authors/Companies/etc")
					with div (id='author-box'):
						os.chdir(authordir)
						for authorfile in os.listdir("."):
							authorfilename = os.path.splitext(authorfile)[0]
							author_read = open(authorfile, 'r')
							h4(authorfilename)
							p(author_read.readline())
							for auth_line in author_read:
								p(author_read.readlines(1))
							br()

				with div(id='softwarechart'):
					h4("Software")
					with div(id='software-box'):
						os.chdir(softwaredir)
						for softwfile in os.listdir("."):
							softfilename = os.path.splitext(softwfile)[0]
							sfile_read = open(softwfile, 'r')
							h4(softfilename)
							p(sfile_read.readline())
							for soft_line in sfile_read:
								p(sfile_read.readlines(8))
							br()
					os.chdir(ROOT_DIR)

			with div(id='thirdrow'):
				with div(id='devicechart'):
					h4("Devices/Models")
					with div(id='device-box'):
						os.chdir(devicedir)
						for softwfile in os.listdir("."):
							softfilename = os.path.splitext(softwfile)[0]
							sfile_read = open(softwfile, 'r')
							h4(softfilename)
							p(sfile_read.readline())
							for soft_line in sfile_read:
								p(sfile_read.readlines(8))
							br()
					os.chdir(ROOT_DIR)

				with div(id='customchart'):
					h4("Custom Tags")
					with div(id='custom-box'):
						os.chdir(customdir)
						for customfile in os.listdir("."):
							customfilename = os.path.splitext(customfile)[0]
							custom_read = open(customfile, 'r')
							h4(customfilename)
							p(custom_read.readline())
							for custom_line in custom_read:
								p(custom_read.readlines(8))
							br()
					os.chdir(ROOT_DIR)



	with open('index.html', 'w') as index:
		index.write(doc.render()) 





def filtershtml():
	os.chdir(ROOT_DIR)
	doc = dominate.document(title='Metaforge')

	#Creates <head>
	with doc.head:
		link(rel='stylesheet', href="template_data/css/main.css")
		script(type='text/javascript', src="template_data/js/main.js")
		
	#Creates <body>
	with doc:
		h1("Metaforge")
		h3("Filtered Metadata")
		with div(id='metaforge-credits'):
			p("Created Chris Morris and Collin Mockbee")
			p("https://github.com/chriswmorris/Metaforge")
		br()
		with div(id= 'wrapper'):
			with div(id='navbar').add(ul()):
				with div(id='nav-li'):
					a('Home/Stats', href='index.html' % ['index'])
					a('Filtered_Metadata', href='filters.html' % ['filters'])
					a('All_Metadata', href='rawmeta.html' % ['rawmeta'])
					a('Hexadecimal_View', href='hexdump.html' % ['hexdump'])
	
			with span(id='filtered'):
				p(b("This section contains a shortened view of all of the metadata from all files."))
				p("We went through the tags of each individual filetype and selected only noteworthy and important tags so you don't have to look through useless meta ;)")
				br()
				br()
				br()

				#loop through all exifoutputs
				os.chdir(ROOT_DIR +"/exifdata/filtered/")
				for file in os.listdir("."):
					filename = os.path.splitext(file)[0]
					file_read = open(file, 'r')
					h3(filename)
					for line in file_read:
						p(file_read.readlines(1))
					br()
			os.chdir(ROOT_DIR)
						
	with open('filters.html', 'w') as filters:
		filters.write(doc.render())


def rawmetahtml():
	#This creates HTML document with dominate 
	os.chdir(ROOT_DIR)
	doc = dominate.document(title='Metaforge')

	#Creates <head>
	with doc.head:
		link(rel='stylesheet', href="template_data/css/main.css")
		script(type='text/javascript', src="template_data/js/main.js")
		
	#Creates <body>
	with doc:
		h1("Metaforge")
		h3("All Metadata")
		with div(id='metaforge-credits'):
			p("Created Chris Morris and Collin Mockbee")
			p("https://github.com/chriswmorris/Metaforge")
		br()
		with div(id= 'wrapper'):
			with div(id='navbar').add(ul()):
				with div(id='nav-li'):
					a('Home/Stats', href='index.html' % ['index'])
					a('Filtered_Metadata', href='filters.html' % ['filters'])
					a('All_Metadata', href='rawmeta.html' % ['rawmeta'])
					a('Hexadecimal_View', href='hexdump.html' % ['hexdump'])

			with span(id='exifraw'):
				#loop through all exifoutputs
				os.chdir(ROOT_DIR +"/exifdata/html/")
				for filename in os.listdir("."):
					raw_filename = os.path.splitext(filename)[0]
					h3(raw_filename)
					iframe(src="exifdata/html/" + filename,  width="500", height="500")
					br()
			os.chdir(ROOT_DIR)
	with open('rawmeta.html', 'w') as rawmeta:
		rawmeta.write(doc.render()) 


def hexmetahtml():
	os.chdir(ROOT_DIR)
	doc = dominate.document(title='Metaforge')

	#Creates <head>
	with doc.head:
		link(rel='stylesheet', href="template_data/css/main.css")
		script(type='text/javascript', src="template_data/js/main.js")
		
	#Creates <body>
	with doc:
		h1("Metaforge")
		h3("Hexadecimal View of the Metadata")
		with div(id='metaforge-credits'):
			p("Created Chris Morris and Collin Mockbee")
			p("https://github.com/chriswmorris/Metaforge")
		br()
		with div(id= 'wrapper'):
			with div(id='navbar').add(ul()):
				with div(id='nav-li'):
					a('Home/Stats', href='index.html' % ['index'])
					a('Filtered_Metadata', href='filters.html' % ['filters'])
					a('All_Metadata', href='rawmeta.html' % ['rawmeta'])
					a('Hexadecimal_View', href='hexdump.html' % ['hexdump'])

			with span(id='exifhexdump'):
				#loop through all exifoutputs
				os.chdir(ROOT_DIR +"/exifdata/hex_html/")
				for filename in os.listdir("."):
					raw_filename = os.path.splitext(filename)[0]
					h3(raw_filename)
					iframe(src="exifdata/hex_html/" + filename,  width="700", height="500")
					br()
			os.chdir(ROOT_DIR)
					
	with open('hexdump.html', 'w') as hexdump:
		hexdump.write(doc.render()) 

