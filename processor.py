#! /usr/bin/python

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


latexc = tempfile.NamedTemporaryFile() # DO NOT Erase this line. Temporary file for LaTeX storage.
#try:
#    print 'temp:', temp
#    print 'temp.name:', temp.name

# An MLA Name Breaker:
def namebreak():
	namelist=author.split(' ') # This assumes that the name is separated properly by spaces.
	fname=' '.join(namelist[:-1]) # This assumes that the first name(s) is (are) supplied first in the query page.
	lname=namelist[-1] # This assumes that the last name is next and last.
if starter="MLA":
	namebreak()

# Quotation mark Correcter:
def qcorrecter(string):
	for x in string:
		if x=='"':
			#To-Do~
		

# Document Formatting Changes:
if starter="Standard (recommended)":
	articleclass="article"
if starter="Turabian":
	## ADD NEW QUERY
if starter="APA":
	articleclass="apa"
if starter="MLA":
	articleclass="article"
	mlapackager="\usepackage{mla}"
	mla="\begin{mla}{"+fname+"}{"+lname+"}{"+Plname+"}{"+Classname+"}{"+date+"}{"+title+"}"
	#Warning!: Professor name (Plname) needs to be added to query page!
	maketitle=""
	mlastop="\end{mla}"
if not starter="MLA":
	mlapackager=""
	mla=""
	maketitle="\maketitle"
	mlastop=""
#Landscaping:
if landscape=True:
	lsss=""
else:
	lsss="%"

# Begin paragraphs with an empty line rathen than an intent:
if parseSkip=True:
	psss=''
else:
	psss="%"

# Quotation marks corrections
if qCorrect=True:
	qcorrecter()

lbasic='''
\documentclass[11pt, oneside]{'''articleclass'''}   	% use "amsart" instead of "article" for AMSLaTeX format
\usepackage{geometry}                		% See geometry.pdf to learn the layout options. There are lots.
\geometry{'''paperstyle'''}                   		% ... or a4paper or a5paper or ... 
'''lsss'''\geometry{landscape}                		% Activate for rotated page geometry
'''psss'''\usepackage[parfill]{parskip}    		% Activate to begin paragraphs with an empty line rather than an indent
\usepackage{graphicx}				% Use pdf, png, jpg, or epsÂ§ with pdflatex; use eps in DVI mode
								% TeX will automatically convert eps --> pdf in pdflatex		
\usepackage{amssymb}

%SetFonts

%SetFonts


\title{'''+title'''}
\author{'''+author+'''}
\date{'''+date+'''}							% Activate to display a given date or no date

'''
+mlapackager+
'''

\begin{document}
'''+maketitle+'''
'''+mla+'''
%\section{}
%\subsection{}
'''+bodyText+'''

'''
+mlastop+
'''
\end{document}  	
'''
finally:
    # Automatically cleans up the file
    latexc.close()
# print 'Exists after close:', os.path.exists(temp.name)

#subprocess.call(['shell scripts/convertToPDF.sh', str(fileName)])
# above statement will need the temp file as fileName for it to be passed to the shell script


def main():
	#print HTML_HEADER
	#print HEAD
	#print END
main()
