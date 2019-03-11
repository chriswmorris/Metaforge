# Metaforge #

<img src="https://raw.githubusercontent.com/chriswmorris/Metaforge/master/Template_Data/img/logo.png" width="250 height=300" title="Metaforge Logo">


*"An OSINT tool that analyzes metadata and creates dynamic reports"*
<br><br>
https://chriswmorris.github.io/Metaforge/

**Senior Design Project 2019 - By Chris Morris and Collin Mockbee**

A Python3 Application for Unix-based Operating Systems

**Note: Metaforge requires at least python version 3.5 to work!**

<br>

**Supported Filetypes** 

dll | docx | doc  |
exe | gif  | html |
jpeg| mkv  | mp3  |
mp4 | odp  | ods  |
odt | pdf  | png  | 
pptx| ppt  | svg  |
torrent|wav | xlsx |
xls  |zip |

<br>

## Setup ## 

### Install exiftool ###


**Debian-based**

<code>apt install libimage-exiftool-perl</code>

**RHEL-based**

<code>yum install perl-Image-ExifTool</code>

**Arch Linux**

<code>pacman -S perl-image-exiftool</code>

**Mac OSX**

<code>brew install exiftool </code>


### Install dependencies ###

<code> pip3 install -r requirements.txt </code>

<hr>



## Running Metaforge ##

1) Place the files you wish to analyze in the **/media** directory

2) Run metaforge.py

<code> python3 metaforge.py </code>


<br>




When Metaforge is finished running, check the User_Projects folder and look for the name of the project you entered. Click on the index.html file to view your generated report.





**Thanks to...**


Exiftool: https://www.sno.phy.queensu.ca/~phil/exiftool/

progress: https://pypi.org/project/progress/

dominate: https://pypi.org/project/dominate/

colorama: https://pypi.org/project/colorama/

pyexifinfo: https://pypi.org/project/pyexifinfo/
