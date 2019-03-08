#!/usr/bin/env python3

from definitions import ROOT_DIR
from os.path import basename
import os, sys
import shutil

'''
These will filter the JSON files and sort them into useful categories.
Each function is a file extension.

1) Load Filter
2) Load Metadata
3) Compare each line of Metadata to Filter (tuple)
4) Print Similarities

IMPORTANT: Always include the name of the file in the filtered tags as a tuple
https://www.miniwebtool.com/remove-line-breaks/
'''

def JPEGfilter():
	#Load list of tags as a tuple 
	jpegtags = ('Adobe:APP14Flags0',  'Adobe:DCTEncodeVersion',  'Composite:CircleOfConfusion',  'Composite:FocalLength35efl',
	  'Composite:FOV',  'Composite:GPSDateTime',  'Composite:GPSLatitude',  'Composite:GPSLongitude',  'Composite:GPSPosition', 
	  'Composite:HyperfocalDistance',  'Composite:ImageSize',  'Composite:LensID',  'Composite:ShutterSpeed',  'Composite:SubSecCreateDate',  
	  'Composite:SubSecDateTimeOriginal',	  'Composite:SubSecModifyDate',  'Ducky:Quality',  'EXIF:ApertureValue',  'EXIF:Copyright',  
	  'EXIF:CreateDate',  'EXIF:CustomRendered',  'EXIF:DateTimeOriginal',  'EXIF:ExposureProgram',  'EXIF:FileSource',  'EXIF:Flash',  
	  'EXIF:FlashpixVersion',  'EXIF:FocalLength',  'EXIF:FocalLengthIn35mmFormat',  'EXIF:Gamma',  'ExifIFD:CreateDate',  'ExifIFD:DateTimeOriginal',
	  'ExifIFD:ExposureProgram',  'ExifIFD:FileSource',  'ExifIFD:Flash',  'ExifIFD:FlashpixVersion',  'ExifIFD:FocalLength',  
	  'ExifIFD:FocalLengthIn35mmFormat',  'ExifIFD:Gamma',  'ExifIFD:ISO',  'ExifIFD:LensInfo',  'ExifIFD:LensMake',	  'ExifIFD:LensModel',  
	  'ExifIFD:LightSource',  'ExifIFD:MaxApertureValue',  'ExifIFD:Saturation',  'ExifIFD:SceneCaptureType',  'ExifIFD:SceneType',  
	  'ExifIFD:SensingMethod',  'ExifIFD:Sharpness',  'ExifIFD:ShutterSpeedValue',  'ExifIFD:SubjectDistance',  'ExifIFD:SubjectDistanceRange',  
	  'EXIF:ISO',  'EXIF:LensInfo',  'EXIF:LensMake',	  'EXIF:LensModel',  'EXIF:LightSource',  'EXIF:Make',  'EXIF:MaxApertureValue',  
	  'EXIF:Model',  'EXIF:ModifyDate',  'EXIF:Saturation',  'EXIF:SceneCaptureType',  'EXIF:SceneType',  'EXIF:SensingMethod',  'EXIF:Sharpness',  
	  'EXIF:ShutterSpeedValue',  'EXIF:Software',  'EXIF:SubjectDistance',  'EXIF:SubjectDistanceRange',  'ExifTool:Warning',  'File:Comment',  
	  'FOV',  'GPS:GPSAltitude',  'GPS:GPSDateStamp',  'GPS:GPSDOP',  'GPS:GPSLatitude',  'GPS:GPSLatitudeRef',  'GPS:GPSLongitude',  
	  'GPS:GPSLongitudeRef',  'GPS:GPSTimeStamp',  'ICC-header:DeviceAttributes'  'ICC-header:PrimaryPlatform',  'ICC-header:ProfileCreator',  
	  'ICC-header:ProfileDateTime',  'ICC-header:RenderingIntent',  'ICC-meas:MeasurementObserver',  'ICC_Profile:ProfileCopyright',  
	  'ICC_Profile:ProfileDescription',  'ICC_Profile:Technology',  'IFD0:Copyright',  'IFD0:ImageDescription',  'IFD0:Orientation',  
	  'InternalSerialNumber',  'IPTC:By-line',  'IPTC:Caption-Abstract',  'IPTC:CodedCharacterSet',  'IPTC:CopyrightNotice',  'IPTC:Credit',  
	  'IPTC:ObjectName',  'IPTC:Source',  'IPTC:SpecialInstructions',  'JFIF:JFIFVersion',  'Macro',  'MakerNotes:AFMode',  'MakerNotes:FacesDetected',
	  'MakerNotes:FocusMode',  'MakerNotes:FujiFlashMode',  'MakerNotes:InternalSerialNumber',  'MakerNotes:PictureMode',  'MakerNotes:Quality',  
	  'MakerNotes:Sharpness',  'Photoshop:PhotoshopFormat',  'Photoshop:ProgressiveScans',  'Photoshop:ReaderName',  'Photoshop:URL_List', 
	  'Photoshop:WriterName',  'Quality',  'System:FileInodeChangeDate',  'System:FileModifyDate',  'XMP:About',  'XMP:CreatorTool',  
	  'XMP:DateAcquired',  'XMP-dc:Creator',  'XMP-dc:Rights',  'XMP:DocumentID',  'XMP-exif:UserComment',  'XMP:InstanceID',  
	  'XMP-photoshop:DateCreated',  'XMP-xmp:CreatorTool',  'XMP-xmpMM:DerivedFromDocumentID',  'XMP:XMPToolkit',  'XMP-x:XMPToolkit')
	
	#Load files then compare to list of tags
	jpegdest = ROOT_DIR + "/exifdata/filtered/"
	jpegsrc = ROOT_DIR + "/exifdata/json/jpeg/"

	os.chdir(jpegsrc)
	for jpegfile in os.listdir("."):
		with open(jpegfile) as ofilejson:
			basejpeg = os.path.basename(jpegfile)
			with open(os.path.splitext(basejpeg)[0]+".txt","w") as jpeg_filename:
				for line in ofilejson:
					for tag in jpegtags:
						if tag in line:
							jpeg_filename.write(line)

	#Move the outputs to filtered directory						
	os.chdir(ROOT_DIR + "/exifdata/json/jpeg")						
	for jpegfile in os.listdir("."):
		if ".txt" in jpegfile:
			shutil.move(jpegsrc + jpegfile, jpegdest)



def PNGfilter():

	pngtags = ('File:FileModifyDate','Composite:CircleOfConfusion',  'Composite:FocalLength35efl',  'Composite:FOV',  'Composite:GPSDateTime',  'Composite:GPSLatitude',
	  'Composite:GPSLongitude',  'Composite:GPSPosition',  'Composite:HyperfocalDistance',  'Composite:ImageSize',  'Composite:LensID',  
	  'Composite:ShutterSpeed',  'Composite:SubSecCreateDate',  'Composite:SubSecDateTimeOriginal',	  'Composite:SubSecModifyDate',  'Ducky:Quality',  
	  'File:Comment',  'File:FileAccessDate',  'File:FileInodeChangeDate', 'GPSAltitude',  'GPSDateStamp',  'GPSDOP',  'GPSLatitude',  
	  'GPSLatitudeRef',  'GPSLongitude',  'GPSLongitudeRef',  'GPSTimeStamp',  'ICC-header:DeviceAttributes'  'ICC-header:PrimaryPlatform',  
	  'ICC-header:ProfileCreator',  'ICC-header:ProfileDateTime',  'ICC-header:RenderingIntent',  'ICC-meas:MeasurementObserver',  
	  'ICC_Profile:DeviceMfgDesc',  'ICC_Profile:DeviceModel',  'ICC_Profile:DeviceModelDesc',  'ICC_Profile:MakeAndModel',  
	  'ICC_Profile:MeasurementIlluminant',  'ICC_Profile:MeasurementObserver',  'ICC_Profile:PrimaryPlatform',  'ICC_Profile:ProfileCMMType',  
	  'ICC_Profile:ProfileCopyright',  'ICC_Profile:ProfileCreator'  'ICC_Profile:ProfileDateTime',  'ICC_Profile:ProfileDescription',  
	  'ICC_Profile:ProfileFileSignature',  'ICC_Profile:ProfileID',  'ICC_Profile:RenderingIntent',  'ICC_Profile:Technology',  'ICC_Profile:ViewingCondDesc',
	  'PNG:Copyright',  'PNG:CreationTime',  'PNG:datecreate',  'PNG:datemodify',  'PNG:Filter',  'PNG:ModifyDate',  'PNG:Palette',  'PNG:ProfileName',
	  'PNG:Software',  'PNG:SRGBRendering',  'PNG:VirtualPageUnits',  'XMP:About',  'XMP:Compression',  'XMP:CreateDate',  'XMP:CreatorTool',  
	  'XMP:DateAcquired',  'XMP:DateCreated',  'XMP-dc:Creator',  'XMP-dc:Rights',  'XMP:DerivedFromDocumentID',  'XMP:DerivedFromInstanceID',  
	  'XMP:DerivedFromOriginalDocumentID',  'XMP:DocumentID',  'XMP-exif:UserComment',  'XMP:HistoryAction',  'XMP:HistoryChanged',  
	  'XMP:HistoryInstanceID',  'XMP:HistoryParameters',  'XMP:HistorySoftwareAgent',  'XMP:HistoryWhen',  'XMP:ICCProfileName',  'XMP:InstanceID',  
	  'XMP:Marked',  'XMP:MetadataDate',  'XMP:ModifyDate',  'XMP:Orientation',  'XMP-photoshop:DateCreated',  'XMP:Title',  'XMP:TransmissionReference',
	  'XMP:UserComment',  'XMP-xmp:CreatorTool',  'XMP-xmpMM:DerivedFromDocumentID',  'XMP:XMPToolkit',  'XMP:XMPToolkit',  'XMP-x:XMPToolkit')

	pngdest = ROOT_DIR + "/exifdata/filtered"
	pngsrc = ROOT_DIR + "/exifdata/json/png/"

	os.chdir(pngsrc)
	for pngfile in os.listdir("."):
		with open(pngfile) as opngfile:
			basepng = os.path.basename(pngfile)
			with open(os.path.splitext(basepng)[0]+".txt","w") as png_filename:
				for line in opngfile:
					for tag in pngtags:
						if tag in line:
							png_filename.write(line)

	os.chdir(pngsrc)						
	for pngfile in os.listdir("."):
		if ".txt" in pngfile:
			shutil.move(pngsrc + pngfile, pngdest)						


def GIFfilter():
	
	giftags =("File:FileModifyDate","File:Comment" ,"HTML:HTTPEquivXUaCompatible","HTML:viewport","HTML:twitterAccount_id","HTML:twitterCard",
	"HTML:twitterTitle","HTML:twitterCreator","HTML:twitterSite","HTML:twitterDescription","HTML:twitterImageSrc","HTML:twitterDomain",
	"HTML:twitterPlayer","HTML:Rating","HTML:Description","HTML:Author","HTML:Keywords","HTML:pinterest","HTML:Title","GIF:GIFVersion",
	"GIF:AnimationIterations","GIF:FrameCount","GIF:Duration","HTML:Copyright","HTML:msapplicationTileColor","HTML:msapplicationTileImage",
	"HTML:pDomain_verify")

	gifdest = ROOT_DIR + "/exifdata/filtered"
	gifsrc = ROOT_DIR + "/exifdata/json/gif/"

	os.chdir(gifsrc)
	for giffile in os.listdir("."):
		with open(giffile) as ogiffile:
			basegif = os.path.basename(giffile)
			with open(os.path.splitext(basegif)[0]+".txt","w") as gif_filename:
				for line in ogiffile:
					for tag in giftags:
						if tag in line:
							gif_filename.write(line)

	os.chdir(gifsrc)						
	for giffile in os.listdir("."):
		if ".txt" in giffile:
			shutil.move(gifsrc + giffile, gifdest)



def DOCXfilter():

	docxtags=("File:FileModifyDate","File:MIMEType","ZIP:ZipModifyDate","XML:Template","XML:TotalEditTime","XML:Application",
	"XML:Paragraphs","XML:LastPrinted","XML:CreateDate","XML:RevisionNumber","XMP:Creator","XML:ModifyDate","XMP:Creator",
	"XMP:Language","XML:Words","XML:Pages","XML:CharactersWithSpaces","XMP:Description","XMP:Subject","XMP:Title","XML:Characters",
	"XML:DocSecurity","XML:Keywords","XML:Lines","XML:Company","XML:SharedDoc","XML:AppVersion","XML:LastModifiedBy","FlashPix:Title",
	"FlashPix:Subject","FlashPix:Author","FlashPix:LastModifiedBy","FlashPix:RevisionNumber","FlashPix:Software",
	"FlashPix:TotalEditTime","FlashPix:LastPrinted","FlashPix:CreateDate","FlashPix:Pages","FlashPix:Words","FlashPix:Characters",
	"FlashPix:Security","FlashPix:CodePage","FlashPix:Company","FlashPix:Lines","FlashPix:Paragraphs","FlashPix:CharCountWithSpaces",
	"FlashPix:SharedDoc","FlashPix:CompObjUserType","FlashPix:Comments","FlashPix:Bytes","FlashPix:Slides","FlashPix:Notes",
	"FlashPix:HiddenSlides","FlashPix:AppVersion")

	docxdest = ROOT_DIR + "/exifdata/filtered"
	docxsrc = ROOT_DIR + "/exifdata/json/docx/"

	os.chdir(docxsrc)
	for docxfile in os.listdir("."):
		with open(docxfile) as odocxfile:
			basedocx = os.path.basename(docxfile)
			with open(os.path.splitext(basedocx)[0]+".txt","w") as docx_filename:
				for line in odocxfile:
					for tag in docxtags:
						if tag in line:
							docx_filename.write(line)

	os.chdir(docxsrc)						
	for docxfile in os.listdir("."):
		if ".txt" in docxfile:
			shutil.move(docxsrc + docxfile, docxdest)
	

def EXEfilter():

	exetags=("File:FileType","File:FileModifyDate","EXE:MachineType","EXE:TimeStamp","EXE:PEType","EXE:LinkerVersion",
	"EXE:OSVersion","EXE:Subsystem","EXE:ProductName","EXE:OriginalFileName","EXE:LegalCopyright","EXE:InternalName",
	"EXE:FileVersion","EXE:FileDescription","EXE:CompanyName","EXE:CharacterSet","EXE:LanguageCode","EXE:FileOS",
	"EXE:ProductVersionNumber","EXE:EntryPoint","EXE:SquirrelAwareVersion","EXE:ProductVersion","EXE:CharacterSet",
	"EXE:Comments","EXE:ObjectFileType","EXE:FileVersionNumber","EXE:FileFlags","EXE:InitializedDataSize")

	exedest = ROOT_DIR + "/exifdata/filtered"
	exesrc = ROOT_DIR + "/exifdata/json/exe/"

	os.chdir(exesrc)
	for exefile in os.listdir("."):
		with open(exefile) as oexefile:
			baseexe = os.path.basename(exefile)
			with open(os.path.splitext(baseexe)[0]+".txt","w") as exe_filename:
				for line in oexefile:
					for tag in exetags:
						if tag in line:
							exe_filename.write(line)

	os.chdir(exesrc)						
	for exefile in os.listdir("."):
		if ".txt" in exefile:
			shutil.move(exesrc + exefile, exedest)

	
def MKVfilter():
	mkvtags=("File:FileModifyDate","Matroska:MuxingApp","Matroska:WritingApp","Matroska:Duration","Matroska:TrackType","Matroska:Title","Matroska:AudioSampleRate",
	"Matroska:VideoFrameRate","Matroska:VideoCodecID","Matroska:ImageWidth","Matroska:ImageHeight","Composite:ImageSize","Composite:Megapixels")

	mkvdest = ROOT_DIR + "/exifdata/filtered"
	mkvsrc = ROOT_DIR + "/exifdata/json/mkv/"

	os.chdir(mp3src)
	for mkvfile in os.listdir("."):
		with open(mkvfile) as omkvfile:
			basemkv = os.path.basename(mkvfile)
			with open(os.path.splitext(basemkv)[0]+".txt","w") as mkv_filename:
				for line in omkvfile:
					for tag in mkvtags:
						if tag in line:
							mkv_filename.write(line)

	os.chdir(mkvsrc)						
	for mkvfile in os.listdir("."):
		if ".txt" in mkvfile:
			shutil.move(mkvsrc + mkvfile, mkvdest)




def MP3filter():
	
	mp3tags=('File:ID3Size','MPEG:MPEGAudioVersion','MPEG:AudioLayer','MPEG:AudioBitrate','MPEG:SampleRate',
		'MPEG:ChannelMode','MPEG:MSStereo','MPEG:IntensityStereo','MPEG:CopyrightFlag','MPEG:OriginalMedia','MPEG:Emphasis',
		'ID3:Title','ID3:Artist','ID3:Album','ID3:Year','ID3:Comment','ID3:Genre','Composite:DateTimeOriginal','Composite:Duration')


	mp3dest = ROOT_DIR + "/exifdata/filtered"
	mp3src = ROOT_DIR + "/exifdata/json/mp3/"

	os.chdir(mp3src)
	for mp3file in os.listdir("."):
		with open(mp3file) as omp3file:
			basemp3 = os.path.basename(mp3file)
			with open(os.path.splitext(basemp3)[0]+".txt","w") as mp3_filename:
				for line in omp3file:
					for tag in mp3tags:
						if tag in line:
							mp3_filename.write(line)

	os.chdir(mp3src)						
	for mp3file in os.listdir("."):
		if ".txt" in mp3file:
			shutil.move(mp3src + mp3file, mp3dest)


def MP4filter():
	mp4tags=("QuickTime:CreateDate","QuickTime:Duration","QuickTime:GraphicsMode","QuickTime:CompressorName","QuickTime:MajorBrand","QuickTime:MediaLanguageCode",
	"QuickTime:HandlerDescription","QuickTime:HandlerVendorID","XMP:CreateDate","XMP:VideoFieldOrder","XMP:HistorySoftwareAgent","XMP:XMPToolkit",
	"XMP:PantryHistorySoftwareAgent","XMP:WindowsAtomUncProjectPath","XMP:CreatorTool","XMP:MacAtomPosixProjectPath")


	mp4dest = ROOT_DIR + "/exifdata/filtered"
	mp4src = ROOT_DIR + "/exifdata/json/mp4/"

	os.chdir(mp4src)
	for mp4file in os.listdir("."):
		with open(mp4file) as omp4file:
			basemp4 = os.path.basename(mp4file)
			with open(os.path.splitext(basemp4)[0]+".txt","w") as mp4_filename:
				for line in omp4file:
					for tag in mp4tags:
						if tag in line:
							mp4_filename.write(line)

	os.chdir(mp4src)						
	for mp4file in os.listdir("."):
		if ".txt" in mp4file:
			shutil.move(mp4src + mp4file, mp4dest)
	

def HTMLfilter():

	htmltags=("HTML:Title","HTML:Description","HTML:twitterCard","HTML:Robots","HTML:twitterTitle","HTML:twitterDescription","HTML:twitterUrl","HTML:twitterImage",
	"HTML:googleSiteVerification","HTML:swiftPageName","HTML:msapplicationTileImage","HTML:hostname","HTML:googleAnalytics","HTML:requestId","HTML:userLogin",
	"HTML:expectedHostname","HTML:jsProxySiteDetectionPayload","HTML:enabledFeatures","HTML:browserStatsUrl","HTML:browserErrorsUrl","HTML:themeColor","HTML:mobileWebAppCapable",
	"HTML:Keywords","HTML:csrfToken","HTML:themeColor")


	htmldest = ROOT_DIR + "/exifdata/filtered"
	htmlsrc = ROOT_DIR + "/exifdata/json/html/"

	os.chdir(htmlsrc)
	for htmlfile in os.listdir("."):
		with open(htmlfile) as ohtmlfile:
			basehtml = os.path.basename(htmlfile)
			with open(os.path.splitext(basehtml)[0]+".txt","w") as html_filename:
				for line in ohtmlfile:
					for tag in htmltags:
						if tag in line:
							html_filename.write(line)

	os.chdir(htmlsrc)						
	for htmlfile in os.listdir("."):
		if ".txt" in htmlfile:
			shutil.move(htmlsrc + htmlfile, htmldest)

def ODPfilter():

	odptags=("XMP:Creation-date","XMP:Date","XMP:Editing-duration","XMP:Editing-cycles","XMP:Generator",
	"XMP:Document-statisticObject-count","XMP:Language","XMP:Print-date","XMP:Creator","XMP:User-definedName",
	"XMP:XMPToolkit","XMP:Description","XMP:Title","XMP:CreationDate--Text","XMP:Producer","XMP:CreatorTool",
	"XMP:ModifyDate","XMP:About","XMP:CreatorTool","XMP:DateAcquired","XMP-dc:Creator","XMP-dc:Rights","XMP:DocumentID",
	"XMP-exif:UserComment","XMP:InstanceID","XMP-photoshop:DateCreated","XMP-xmp:CreatorTool","XMP-xmpMM:DerivedFromDocumentID",
	"XMP:XMPToolkit","XMP-x:XMPToolkit")


	odpdest = ROOT_DIR + "/exifdata/filtered"
	odpsrc = ROOT_DIR + "/exifdata/json/odp/"

	os.chdir(odpsrc)
	for odpfile in os.listdir("."):
		with open(odpfile) as oodpfile:
			baseodp = os.path.basename(odpfile)
			with open(os.path.splitext(baseodp)[0]+".txt","w") as odp_filename:
				for line in oodpfile:
					for tag in odptags:
						if tag in line:
							odp_filename.write(line)

	os.chdir(odpsrc)						
	for odpfile in os.listdir("."):
		if ".txt" in odpfile:
			shutil.move(odpsrc + odpfile, odpdest)



def PPTXfilter():
	pptxtags = ('File:FileModifyDate',  'File:FileAccessDate',  'File:FileInodeChangeDate',  'FlashPix:CurrentUser',  
		'FlashPix:Title',  'FlashPix:Author',  'FlashPix:Template',  'FlashPix:LastModifiedBy',  'FlashPix:RevisionNumber',  'FlashPix:Software',
		'FlashPix:TotalEditTime',  'FlashPix:CreateDate',  'FlashPix:ModifyDate',  'FlashPix:Words',  'FlashPix:PresentationTarget', 
		'FlashPix:Company',  'FlashPix:Bytes',  'FlashPix:Paragraphs',  'FlashPix:Slides',  'FlashPix:Notes',  'FlashPix:HiddenSlides',  
		'FlashPix:MMClips',  'FlashPix:AppVersion',  'FlashPix:ScaleCrop',  'FlashPix:LinksUpToDate',  'FlashPix:SharedDoc',  
		'FlashPix:HyperlinksChanged',  'FlashPix:TitleOfParts',  'FlashPix:HeadingPairs',  'FlashPix:CodePage',  'FlashPix:Hyperlinks',  
		'FlashPix:ContentType',  'FlashPix:HyperlinkBase',  'XML:TitlesOfParts',  'ZIP:ZipRequiredVersion',  'ZIP:ZipFileName',  
		'ZIP:ZipModifyDate',  'XML:Template',  'XML:TotalEditTime',  'XML:Words',  'XML:Application',  'XML:PresentationFormat',  
		'XML:Paragraphs',  'XML:Slides',  'XML:Notes',  'XML:HiddenSlides',  'XML:MMClips',  'XML:ScaleCrop',  'XML:HeadingPairs',  
		'XML:LinksUpToDate',  'XML:SharedDoc',  'XML:HyperlinksChanged',  'XML:AppVersion',  'XML:LastModifiedBy',  'XML:RevisionNumber',  
		'XML:CreateDate',  'XML:ModifyDate',  'XML:KSOProductBuildVer',  'XMP:Title',  'XMP:Creator',  'XML:Company',  'XML:LastPrinted')

	pptxdest = ROOT_DIR + "/exifdata/filtered"
	pptxsrc = ROOT_DIR + "/exifdata/json/pptx/"

	os.chdir(pptxsrc)
	for pptxfile in os.listdir("."):
		with open(pptxfile) as opptxfile:
			basepptx = os.path.basename(pptxfile)
			with open(os.path.splitext(basepptx)[0]+".txt","w") as pptx_filename:
				for line in opptxfile:
					for tag in pptxtags:
						if tag in line:
							pptx_filename.write(line)

	os.chdir(pptxsrc)						
	for pptxfile in os.listdir("."):
		if ".txt" in pptxfile:
			shutil.move(pptxsrc + pptxfile, pptxdest)


def ODSfilter():
	odstags=("XMP:About","XMP:CreatorTool","XMP:DateAcquired","XMP-dc:Creator","XMP-dc:Rights","XMP:DocumentID","XMP-exif:UserComment","XMP:InstanceID",
	"XMP-photoshop:DateCreated","XMP-xmp:CreatorTool","XMP-xmpMM:DerivedFromDocumentID","XMP:XMPToolkit","XMP-x:XMPToolkit","XMP:Creator","XMP:Compression",
	"XMP:CreateDate","XMP:CreatorTool","XMP:DateAcquired","XMP:DateCreated","XMP-dc:Creator","XMP-dc:Rights","XMP:DerivedFromDocumentID","XMP:DerivedFromInstanceID",
	"XMP:DerivedFromOriginalDocumentID","XMP:DocumentID","XMP-exif:UserComment","XMP:HistoryAction","XMP:HistoryChanged","XMP:HistoryInstanceID","XMP:HistoryParameters",
	"XMP:HistorySoftwareAgent","XMP:HistoryWhen","XMP:ICCProfileName","XMP:InstanceID","XMP:Marked","XMP:MetadataDate","XMP:ModifyDate","XMP:Orientation","XMP-photoshop:DateCreated","XMP:Title",
	"XMP:TransmissionReference","XMP:UserComment","XMP-xmp:CreatorTool","XMP-xmpMM:DerivedFromDocumentID","XMP:XMPToolkit","XMP:XMPToolkit","XMP-x:XMPToolkit",
	"XMP:Date","XMP:Editing-duration","XMP:Editing-cycles","XMP:Document-statisticTable-count","XMP:Document-statisticCell-count","XMP:Document-statisticObject-count",
	"XMP:Generator")


	odsdest = ROOT_DIR + "/exifdata/filtered"
	odssrc = ROOT_DIR + "/exifdata/json/ods/"

	os.chdir(odssrc)
	for odsfile in os.listdir("."):
		with open(odsfile) as oodsfile:
			baseods = os.path.basename(odsfile)
			with open(os.path.splitext(baseods)[0]+".txt","w") as ods_filename:
				for line in oodsfile:
					for tag in odstags:
						if tag in line:
							ods_filename.write(line)

	os.chdir(odssrc)						
	for odsfile in os.listdir("."):
		if ".txt" in odsfile:
			shutil.move(odssrc + odsfile, odsdest)

def PDFfilter():

	pdftags=("PDF:PageCount","PDF:PDFVersion","PDF:Author","PDF:CreationDate--Text","PDF:CreateDate","PDF:Creator","PDF:ModifyDate","PDF:Producer",
	"PDF:Subject","PDF:Title","XMP:XMPToolkit","XMP:Creator","XMP:Description","XMP:Title","XMP:CreationDate--Text","XMP:Producer","XMP:CreatorTool",
	"XMP:ModifyDate","XMP:About","XMP:CreatorTool","XMP:DateAcquired","XMP-dc:Creator","XMP-dc:Rights","XMP:DocumentID","XMP-exif:UserComment",
	"XMP:InstanceID","XMP-photoshop:DateCreated","XMP-xmp:CreatorTool","XMP-xmpMM:DerivedFromDocumentID","XMP:XMPToolkit","XMP-x:XMPToolkit",
	"PDF:PageCount","PDF:Language","PDF:PTEX_Fullbanner","PDF:PXCViewerInfo")


	pdfdest = ROOT_DIR + "/exifdata/filtered"
	pdftsrc = ROOT_DIR + "/exifdata/json/pdf/"

	os.chdir(pdfsrc)
	for pdffile in os.listdir("."):
		with open(pdffile) as opdffile:
			basepdf = os.path.basename(pdffile)
			with open(os.path.splitext(basepdf)[0]+".txt","w") as pdf_filename:
				for line in opdffile:
					for tag in pdftags:
						if tag in line:
							pdf_filename.write(line)

	os.chdir(pdfsrc)						
	for pdffile in os.listdir("."):
		if ".txt" in pdffile:
			shutil.move(pdfsrc + pdffile, pdfdest)



def SVGfilter():
	svgtags=("SVG:Xmlns","SVG:ID","SVG:ImageHeight","SVG:ImageWidth","SVG:Version","SVG:Docname","SVG:Output_extension","SVG:Export-filename","SVG:MetadataID",
	"XMP:WorkFormat","XMP:WorkType","XMP:WorkDescription","XMP:WorkTitle","XMP:WorkPublisherAgentTitle","XMP:WorkCreatorAgentTitle","XMP:WorkRightsAgentTitle",
	"XMP:WorkLicense","XMP:WorkLanguage","XMP:About","XMP:LicensePermits")


	svgdest = ROOT_DIR + "/exifdata/filtered"
	svgsrc = ROOT_DIR + "/exifdata/json/svg/"

	os.chdir(svgsrc)
	for svgfile in os.listdir("."):
		with open(svgfile) as osvgfile:
			basesvg = os.path.basename(svgfile)
			with open(os.path.splitext(basesvg)[0]+".txt","w") as svg_filename:
				for line in osvgfile:
					for tag in svgtags:
						if tag in line:
							svg_filename.write(line)

	os.chdir(svgsrc)						
	for svgfile in os.listdir("."):
		if ".txt" in svgfile:
			shutil.move(svgsrc + svgfile, svgdest)
	

def TORRENTfilter():

	torrenttags = ('Torrent:Announce','Torrent:CreateDate','Torrent:Length','Torrent:Name','Torrent:PieceLength','Torrent:Comment','Torrent:Creator','Torrent:URLList',
	'Torrent:Private','Torrent:AnnounceList','Torrent:File','Torrent:FileLength')

	torrentdest = ROOT_DIR + "/exifdata/filtered"
	torrentsrc = ROOT_DIR + "/exifdata/json/torrent/"

	os.chdir(torrentsrc)
	for torrentfile in os.listdir("."):
		with open(torrentfile) as otorrentfile:
			basetorrent = os.path.basename(torrentfile)
			with open(os.path.splitext(basetorrent)[0]+".txt","w") as torrent_filename:
				for line in otorrentfile:
					for tag in torrenttags:
						if tag in line:
							torrent_filename.write(line)

	os.chdir(torrentsrc)						
	for torrentfile in os.listdir("."):
		if ".txt" in torrentfile:
			shutil.move(torrentsrc + torrentfile, torrentdest)

def WAVfilter():
	wavtags=("File:FileModifyDate","RIFF:Encoding","RIFF:SampleRate","RIFF:AvgBytesPerSec","RIFF:Description","RIFF:Originator","RIFF:DateTimeOriginal",
	"RIFF:OriginatorReference","Composite:Duration","RIFF:Software","RIFF:Title","RIFF:Artist","RIFF:Comment","RIFF:DateCreated")

	wavdest = ROOT_DIR + "/exifdata/filtered"
	wavsrc = ROOT_DIR + "/exifdata/json/wav/"

	os.chdir(wavsrc)
	for wavfile in os.listdir("."):
		with open(wavfile) as owavfile:
			basewav = os.path.basename(wavfile)
			with open(os.path.splitext(basewav)[0]+".txt","w") as wav_filename:
				for line in owavfile:
					for tag in wavtags:
						if tag in line:
							wav_filename.write(line)

	os.chdir(wavsrc)						
	for wavfile in os.listdir("."):
		if ".txt" in wavfile:
			shutil.move(wavsrc + wavfile, wavdest)


def ZIPfilter():
	
	ziptags=("File:FileModifyDate","ZIP:ZipRequiredVersion","ZIP:ZipModifyDate","ZIP:ZipFileName","ZIP:ZipUncompressedSize","ZIP:ZipCompressedSize","ZIP:ZipCRC")

	zipdest = ROOT_DIR + "/exifdata/filtered"
	zipsrc = ROOT_DIR + "/exifdata/json/zip/"

	os.chdir(zipsrc)
	for zipfile in os.listdir("."):
		with open(zipfile) as ozipfile:
			basezip = os.path.basename(zipfile)
			with open(os.path.splitext(basezip)[0]+".txt","w") as zip_filename:
				for line in ozipfile:
					for tag in ziptags:
						if tag in line:
							zip_filename.write(line)

	os.chdir(zipsrc)						
	for zipfile in os.listdir("."):
		if ".txt" in zipfile:
			shutil.move(zipsrc + zipfile, zipdest)

def DLLfilter():

	dlltags=("File:FileType","File:FileModifyDate","EXE:MachineType","EXE:TimeStamp","EXE:PEType","EXE:LinkerVersion","EXE:OSVersion",
	"EXE:Subsystem","EXE:ProductName","EXE:OriginalFileName","EXE:LegalCopyright","EXE:InternalName","EXE:FileVersion","EXE:FileDescription",
	"EXE:CompanyName","EXE:CharacterSet","EXE:LanguageCode","EXE:FileOS","EXE:ProductVersionNumber","EXE:EntryPoint","EXE:SquirrelAwareVersion",
	"EXE:ProductVersion","EXE:CharacterSet","EXE:Comments","EXE:ObjectFileType","EXE:FileVersionNumber","EXE:FileFlags","EXE:InitializedDataSize")

	dlldest = ROOT_DIR + "/exifdata/filtered"
	dllsrc = ROOT_DIR + "/exifdata/json/dll/"

	os.chdir(dllsrc)
	for dllfile in os.listdir("."):
		with open(dllfile) as odllfile:
			basedll = os.path.basename(dllfile)
			with open(os.path.splitext(basedll)[0]+".txt","w") as dll_filename:
				for line in odllfile:
					for tag in dlltags:
						if tag in line:
							dll_filename.write(line)

	os.chdir(dllsrc)						
	for dllfile in os.listdir("."):
		if ".txt" in dllfile:
			shutil.move(dllsrc + dllfile, dlldest)


	

def XLSXfilter():

	xlsxtags=("XML:LastModifiedBy","XML:CreateDate","XML:ModifyDate","XML:Application","XML:DocSecurity","XML:HeadingPairs",
	"XML:TitlesOfParts","XML:SharedDoc","XML:AppVersion","XML:Keywords","XML:Company","XMP:Title","XMP:Subject","XMP:Creator",
	"XMP:Description","FlashPix:Author","FlashPix:CodePage","FlashPix:LastModifiedBy","FlashPix:Software","FlashPix:CreateDate",
	"FlashPix:ModifyDate","FlashPix:Security","FlashPix:Company","FlashPix:TitleOfParts","FlashPix:HeadingPairs","FlashPix:SharedDoc",
	"FlashPix:AppVersion","FlashPix:Tag_EmailSubject","FlashPix:Tag_AuthorEmail","FlashPix:Tag_AuthorEmailDisplayName","XML:Application")

	xlsxdest = ROOT_DIR + "/exifdata/filtered"
	xlsxsrc = ROOT_DIR + "/exifdata/json/xlsx/"

	os.chdir(xlsxsrc)
	for xlsxfile in os.listdir("."):
		with open(xlsxfile) as oxlsxfile:
			basexlsx = os.path.basename(xlsxfile)
			with open(os.path.splitext(basexlsx)[0]+".txt","w") as xlsx_filename:
				for line in oxlsxfile:
					for tag in xlsxtags:
						if tag in line:
							xlsx_filename.write(line)

	os.chdir(xlsxsrc)						
	for xlsxfile in os.listdir("."):
		if ".txt" in xlsxfile:
			shutil.move(xlsxsrc + xlsxfile, xlsxdest)


def ODTfilter():

	odttags=("File:FileModifyDate","XMP:Creation-date","XMP:Date","XMP:Editing-duration","XMP:Editing-cycles","XMP:Generator",
	"XMP:Document-statisticObject-count","XMP:Language","XMP:Print-date","XMP:User-definedName","XMP:XMPToolkit",
	"XMP:Creator","XMP:Description","XMP:Title","XMP:CreationDate--Text","XMP:Producer","XMP:CreatorTool","XMP:ModifyDate",
	"XMP:About","XMP:DateAcquired","XMP-dc:Creator","XMP-dc:Rights","XMP:DocumentID","XMP-exif:UserComment","XMP:InstanceID",
	"XMP-photoshop:DateCreated","XMP-xmp:CreatorTool","XMP-xmpMM:DerivedFromDocumentID","XMP:XMPToolkit","XMP-x:XMPToolkit")

	odtdest = ROOT_DIR + "/exifdata/filtered"
	odtsrc = ROOT_DIR + "/exifdata/json/odt/"

	os.chdir(odtsrc)
	for odtfile in os.listdir("."):
		with open(odtfile) as oodtfile:
			baseodt = os.path.basename(odtfile)
			with open(os.path.splitext(baseodt)[0]+".txt","w") as odt_filename:
				for line in oodtfile:
					for tag in odttags:
						if tag in line:
							odt_filename.write(line)

	os.chdir(odtsrc)						
	for odtfile in os.listdir("."):
		if ".txt" in odtfile:
			shutil.move(odtsrc + odtfile, odtdest)


	

def filterexec():
	try:
		ODPfilter()
	except:
		pass
	
	try:
		MP3filter()
	except:
		pass

	try:
		DLLfilter()
	except:
		pass

	try:
		TORRENTfilter()
	except:
		pass

	try:
		PPTXfilter()
	except:
		pass

	try:
		ODSfilter()
	except:
		pass

	try:
		ZIPfilter()
	except:
		pass

	try:
		EXEfilter()
	except:
		pass

	try:
		XLSXfilter()
	except:
		pass
	
	try:
		SVGfilter()
	except:
		pass

	try:
		PDFfilter()
	except:
		pass

	try:
		MP4filter()
	except:
		pass

	try:
		HTMLfilter()
	except:
		pass

	try:
		DOCXfilter()
	except:
		pass
	
	try:
		GIFfilter()
	except:
		pass
	try:
		WAVfilter()
		
	except:
		pass

	try:
		JPEGfilter()
	except:
		pass

	try:
		MKVfilter()
	except:
		pass
	
	try:
		PNGfilter()
	except:
		pass

	try:
		ODTfilter()
	except:
		pass
		
