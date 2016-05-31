#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi

import cgitb
cgitb.enable()

#HTML_HEADER = 'Content-type: text/html'

import os
import tempfile

userInput = cgi.FieldStorage()
docFormat = userInput['format'].value
author = userInput['authname'].value
title = userInput['title'].value
date =  userInput['date'].value
starter = userInput['starter'].value
starterText = userInput['starterText'].value
bodyText = userInput['body'].value
fxn = userInput['function'].value
landscape = userInput['landscape'].value
paperstyle = userInput['paperStyle'].value
qCorrect = userInput['qCorrect'].value
affiliationN = userInput['AffiliationCHOOSER'].value
affiliation = userInput['Affiliation'].value
abstract = userInput['Abstract'].value
fontsize = userInput['fSize'].value

# Text variable clearers:
if not affiliatioN=="True":
	affiliation=""

latexc = tempfile.NamedTemporaryFile() # DO NOT Erase this line. Temporary file for LaTeX storage.
#try:
#    print 'temp:', temp
#    print 'temp.name:', temp.name
fileName=latexc.name

# An MLA Name Breaker:
def namebreak():
	namelist=author.split(' ') # This assumes that the name is separated properly by spaces.
	fname=' '.join(namelist[:-1]) # This assumes that the first name(s) is (are) supplied first in the query page.
	lname=namelist[-1] # This assumes that the last name is next and last.
if starter=="MLA":
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
			if type(string[x+1])==type("a"):
				1+1 #Set a descriptor-allowing syntax here! To-Do!
			# More to do! Using this new syntax, set up a section namer!

mlapackager=""
mla=""
maketitle="\maketitle"
mlastop=""
apaAffiliation=""
documentclassb=""

# Document Formatting Changes:
if starter=="Standard":
	articleclass="article"
	documentclassb=fontsize+", oneside"
if starter=="Turabian (standard)":
	articleclass="turabian-formatting"
	documentclassb=fontsize
if starter=="Turabian (Research Paper)":
	articleclass="turabian-researchpaper"
	documentclassb=fontsize
if starter=="Turabian (Thesis or Dissertation)":
	articleclass="turabian-thesis"
	documentclassb=fontsize
if starter=="APA":
	articleclass="apa6" # http://ctan.mackichan.com/macros/latex/contrib/apa6/apa6.pdf
	apaAffiliation="\affiliation{"+affiliation+"}"
	apaAbstract="\abstract{"+abstract+"}" #Warning! New abstract needs to be added to query page!
	apaKeywords="\keywords{"+keywords+"}"
if starter=="MLA":
	articleclass="article"
	mlapackager="\usepackage{mla}"
	mla="\begin{mla}{"+fname+"}{"+lname+"}{"+Plname+"}{"+Classname+"}{"+date+"}{"+title+"}"
	#Warning!: Professor name (Plname) needs to be added to query page!
	maketitle=""
	mlastop="\end{mla}"
	
#Important edits for documentclass:
if not documentclassb=="":
	documentclassb="["+documentclassb+"]"
	
#Landscaping:
if landscape=="True":
	lsss=""
else:
	lsss="%"

# Begin paragraphs with an empty line rathen than an intent:
if parseSkip=="True":
	psss=''
else:
	psss="%"

# Quotation marks corrections
if qCorrect=="True":
	qcorrecter(author)
	qcorrecter(title)
	qcorrecter(date)
	qcorrecter(starterText)
	qcorrecter(bodyText)
	# Any more fields need to have quotation marks corrected?

lbasic='''
\documentclass'''+documentclassb+'''{'''+articleclass+'''}   	% use "amsart" instead of "article" for AMSLaTeX format
\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
\geometry{'''+paperstyle+'''}                   		% ... or a4paper or a5paper or ... 
'''+lsss+'''\geometry{landscape}                		% Activate for rotated page geometry
'''+psss+'''\usepackage[parfill]{parskip}    		% Activate to begin paragraphs with an empty line rather than an indent
\usepackage{graphicx}				% Use pdf, png, jpg, or epsÂ§ with pdflatex; use eps in DVI mode
								% TeX will automatically convert eps --> pdf in pdflatex		
\usepackage{amssymb}

%SetFonts

%SetFonts


\title{'''+title+'''}
\author{'''+author+'''}
'''+apaAffiliation+'''
\date{'''+date+'''}							% Activate to display a given date or no date

'''+mlapackager+'''

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
latexc.close()
# print 'Exists after close:', os.path.exists(temp.name)

#subprocess.call(['shell scripts/convertToPDF.sh', str(fileName)])
# above statement will need the temp file as fileName for it to be passed to the shell script

# Document Handling:
if fxn=="TeX Code":
	print(lbasic)

def main():
	#print HTML_HEADER
	#print HEAD
	#print END
    stuff = 'stuff to avoid throwing exception'
main()
