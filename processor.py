#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi

import cgitb
cgitb.enable()

HTML_HEADER = 'Content-type: text/html\n'
#texplainheader = "Content-Type: text/plain"

import os
import os.path
from subprocess
import tempfile
import string
import random

userInput = cgi.FieldStorage()
docFormat = userInput['format'].value
author = userInput['authname'].value
title = userInput['title'].value
date =  userInput['date'].value
#starter = userInput['starter'].value
#starterText = userInput['starterText'].value
bodyText = userInput['body'].value
fxn = userInput['function'].value
landscape = userInput['landscape'].value
paperstyle = userInput['paperStyle'].value
qCorrect = userInput['qCorrect'].value
affiliation = ""
if userInput.getvalue('AfflationCHOOSER'):
    affiliation = userInput['Affiliation'].value
#affiliationN = userInput['AffiliationCHOOSER'].value
abstract = userInput['Abstract'].value
try:
    fontsize = userInput['fSize'].value
except:
    fontsize=''
parseSkip = userInput['parseSkip'].value
keywords = userInput['Keywords'].value
Plname = userInput['Plname'].value
Classname = userInput['Classname'].value

# Text variable clearers:  

latexc = tempfile.NamedTemporaryFile() # DO NOT Erase this line. Temporary file for LaTeX storage.
#try:
#    print 'temp:', temp
#    print 'temp.name:', temp.name
fileName=latexc.name

latextextfile=open('output.tex','w')
# Important! To prevent file permissions error, create output.tex file and give all permissions to all users
#            modify both processor.py and output.tex -> This is not secure, but things work smoothly this way.
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
def checkIfFile():
    global filePath
    filePath = 'pages/'+id_generator()+'.html'
    if os.path.isfile(filePath):
        return checkIfFile()
    else:
        return filePath       
    
latexhtmlfile=open(checkIfFile(),'w')
# Important! To prevent file permissions error, create output.html file and give all permissions to all users
#            modify both processor.py and output.html -> This is not secure, but things work smoothly this way.

# An MLA Name Breaker:
def namebreak():
	namelist=author.split(' ') # This assumes that the name is separated properly by spaces.
	global fname
	fname=' '.join(namelist[:-1]) # This assumes that the first name(s) is (are) supplied first in the query page.
	global lname
	lname=namelist[-1] # This assumes that the last name is next and last.
	if fname=="":
		fname="FirstName?"
if docFormat == "MLA":
	namebreak()

# Quotation mark Correcter:
def qcorrecter(string):
	yandex0=False
	yandex1=False
	for x in string:
		if x == '"' and yandex0==False:
			string.replace(x,"``")
			yandex0=True
		if x == '"' and yandex0==True:
			string.replace(x,"''")
			yandex0=False
		if x == '“':
			string.replace(x,"``")
		if x == '”':
			string.replace(x,"''")
		if x == "'" and yandex1==False:
			string.replace(x,"`")
			yandex1=True
		if x == "'" and yandex1==True:
			yandex1=False
		if x == "‘":
			string.replace(x,"`")
		if x == "’":
			string.replace(x,"'")

def easyMark(string):
	for x in range(len(string)):
		if string[x]=="~":
			# Making Lists:
			if string[x:x+11]=="~start-list":
				string=string[:x]+"\begin{enumerate}"+string[x+11:]
			if string[x:x+9]=="~end-list":
				string=string[:x]+"\end{enumerate}"+string[x+9:]
			if string[x:x+2]=="~ ":
				string=string[:x]+"\item "+string[x+2:]
			if string[x:x+14]=="~start-bullets":
				string=string[:x]+"\begin{itemize}"+string[x+14:]
			if string[x:x+12]=="~end-bullets":
				string=string[:x]+"\end{itemize}"+string[x+12:]
			if string[x:x+18]=="~start-custom-list":
				string=string[:x]+"\begin{description}"+string[x+18:]
			if string[x:x+16]=="~end-custom-list":
				string=string[:x]+"\end{description}"+string[x+16:]
			# Structuring Your Paper:
			if string[x:x+10]=="~chapter [":
				yandexf=string.find("]", x+10)
				string=string[:x]+"\chapter{"+string[x+10:yandexf]+"}"+string[yandexf+1:]
			# easyMark is failing in actually working!
	return(string)

mlapackager=""
mla=""
maketitle="\maketitle"
mlastop=""
apaAffiliation=""
documentclassb=""
graphicxstopper=""

articleclass="article"
# Document Formatting Changes:
if docFormat == "Standard":
	documentclassb=fontsize+", oneside"
if docFormat == "Turabian (Standard)":
	articleclass="turabian-formatting"
	documentclassb=fontsize
if docFormat == "Turabian (Research Paper)":
	articleclass="turabian-researchpaper"
	documentclassb=fontsize
if docFormat == "Turabian (Thesis or Dissertation)":
	articleclass="turabian-thesis"
	documentclassb=fontsize
if docFormat == "APA":
	articleclass="apa6" # http://ctan.mackichan.com/macros/latex/contrib/apa6/apa6.pdf
	apaAffiliation=r"\affiliation{"+affiliation+"}"
	apaAbstract="\abstract{"+abstract+"}" #Warning! New abstract needs to be added to query page!
	apaKeywords="\keywords{"+keywords+"}"
if docFormat == "MLA":
	articleclass="article"
	mlapackager="\usepackage{mla}"
	mla=r"\begin{mla}{"+fname+"}{"+lname+"}{"+Plname+"}{"+Classname+"}{"+date+"}{"+title+"}"
	#Warning!: Professor name (Plname) needs to be added to query page!
	maketitle=""
	mlastop="\end{mla}"
	graphicxstopper="%"

#Important edits for documentclass:
if not documentclassb=="":
	documentclassb="["+documentclassb+"]"
	
#Landscaping:
if landscape=="True":
	lsss=""
else:
	lsss="%"

# Begin paragraphs with an empty line rathen than an indent:
if parseSkip=="True":
	psss=''
else:
	psss="%"

# Quotation marks corrections
if qCorrect=="True":
	qcorrecter(author)
	qcorrecter(title)
	qcorrecter(date)
	#qcorrecter(starterText)
	qcorrecter(bodyText)
	# Any more fields need to have quotation marks corrected?

lbasic='''
\documentclass'''+documentclassb+'''{'''+articleclass+'''}   	% use "amsart" instead of "article" for AMSLaTeX format
\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
\geometry{'''+paperstyle+'''}                   		% ... or a4paper or a5paper or ... 
'''+lsss+'''\geometry{landscape}                		% Activate for rotated page geometry
'''+psss+'''\usepackage[parfill]{parskip}    		% Activate to begin paragraphs with an empty line rather than an indent
'''+graphicxstopper+'''\usepackage{graphicx}				% Use pdf, png, jpg, or epsÂ§ with pdflatex; use eps in DVI mode
								% TeX will automatically convert eps --> pdf in pdflatex		
\usepackage{amssymb}

%SetFonts

%SetFonts


'''+r"\title{"+title+r'''}
\author{'''+author+'''}
'''+apaAffiliation+r'''
\date{'''+date+'''}							% Activate to display a given date or no date

'''+mlapackager+r'''

\begin{document}
'''+maketitle+'''
'''+mla+'''
%\section{}
%\subsection{}
'''+bodyText+'''

'''+mlastop+'''
\end{document}  	
'''
# string concatenation needs to be on the same line!

#finally:     got rid of finally because that's not needed unless an exception is thrown and if an exception if thrown and you want to use finally you need a try statement
    # Automatically cleans up the file

# print 'Exists after close:', os.path.exists(temp.name)

#subprocess.call(['shell scripts/convertToPDF.sh', str(fileName)])
# above statement will need the temp file as fileName for it to be passed to the shell script

stuff = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>'''+title+'''</title>
        <meta name="author" content="'''+author+'''">
        <meta name="description" content="'''+abstract+'''">
        <meta name="keywords" content="'''+keywords+'''">
        <script src='https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'></script>
        <script src="js/renderer.js"></script>
        <style>
            @font-face { font-family: latex; src: url('../fonts/cmunrm.ttf'); }
            body { font-family: latex, serif; }
            h1, h2 {
                text-align: center;
            }
        </style>    
    </head>
    <body>
<<<<<<< HEAD
'''+'<h1>'+title+'</h1>'+'<h2>'+author+'<br>'+keywords+'</h2>'+bodyText+'''
=======
'''+'<h1>'+title+'</h1>'+'<h2>'+author+'<br>'+date+'</h2>'+bodyText+'''
>>>>>>> origin/master
    </body>
</html>    
'''

latexc.write(lbasic)
latextextfile.write(lbasic)
latextextfile.close()
latexhtmlfile.write(stuff)
latexhtmlfile.close()
# def makepdf():
#     subprocess.Popen("pdflatex output", shell=True)
if fxn=="pdf":
    subprocess.Popen("pdflatex output", shell=True)
    print "Location: output.pdf\r\n"

easystuff = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Generated</title>
        <meta charset="UTF-8">    
'''

morestuff = '''
    </head>
    <body>
    </body>
</html>    
'''


# Requires JavaScript? Can be avoided! see megatex()
redirectTEX = '<script>window.location.href="output.tex";</script>'
redirectPDF = '<script>window.location.href="output.pdf";</script>'
redirectHTML = '<script>window.location.href="output.html";</script>'

# Document Handling:
# !! texman() is depreceated.
'''def texman():
    print HTML_HEADER
    if fxn == "tex":
        g = open('output.tex', 'w')
        g.write(lbasic)
        g.close()
        TELE = redirectTEX+morestuff
        print TELE
    if fxn == "pdf":
        g = open('output.tex', 'w')
        g.write(lbasic)
        g.close()
        subprocess.call(["./convertToPDF.sh"])
        TELE = redirectPDF+morestuff
        print TELE
    else:
        g = open('output.html', 'wU')
        g.write(stuff)
        TELE = redirectHTML+morestuff
        print TELE
'''        
    #print texplainheader
	# Or, use the latexc file that has lbasic written in.
#texman()
## !! texman() is deprecated.

def megatex():
    print "Location: output.tex\r\n"
if fxn=="tex":
    megatex()
<<<<<<< HEAD
# def pdftex():
#     subprocess.call(["./convertToPDF.sh"])
#     print "Location: output.pdf\r\n"
# if fxn=="pdf":
#     pdftex()
=======
def pdftex():
    subprocess.Popen("pdflatex output", shell=True)
    print "Location: output.pdf"
if fxn=="pdf":
    pdftex()
>>>>>>> origin/master
def htmltex():
    print "Location: "+filePath+"\r\n"
if fxn=="webpage" and lbasic.find('<script') == -1 and lbasic.find('<iframe') == -1:
    htmltex()
<<<<<<< HEAD
else:
    print "<!DOCTYPE html><head><title>You dun goofed.</title></head><body>Your query was messed up or you tried to do stuff you weren't supposed to do.</body></html>"

# def pdftex():
#     print "Location: google.com\r\n"
# if fxn=="pdf":
#     pdftex()
=======
if fxn=="webpage" and lbasic.find('<script') != -1 or lbasic.find('<iframe') == -1:
    print HTML_HEADER
    print "<!DOCTYPE html><head><title>You dun goofed.</title></head><body>Your query was messed up or you tried to do stuff you weren't supposed to do.<br><br>if you tried to include the following:<br><ul><li>script tags</li><li>iframes</li></ul><br>then your request was rejected.</body></html>"
>>>>>>> origin/master

# Let's close this file at the very end:
latexc.close()
